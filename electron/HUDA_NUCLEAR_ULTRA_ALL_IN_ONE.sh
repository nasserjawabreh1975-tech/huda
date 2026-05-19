#!/bin/bash

clear

echo "=================================================="
echo "       HUDA NUCLEAR ULTRA RECOVERY ENGINE"
echo "=================================================="
echo ""

BASE="$HOME/HUDA_NUCLEAR_DESKTOP/electron"

echo "[1] ENTERING PLATFORM..."
cd "$BASE" || exit

echo ""
echo "[2] PURGING BROKEN SYSTEM..."
rm -rf node_modules
rm -rf package-lock.json
rm -rf ~/.npm
rm -rf ~/.npm/_npx
rm -rf ~/.cache/electron
rm -rf ~/.cache/electron-builder

echo ""
echo "[3] REMOVING BROKEN NODE..."
sudo apt remove -y nodejs npm
sudo apt autoremove -y

echo ""
echo "[4] INSTALLING NODE 18 LTS..."
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs build-essential

echo ""
echo "[5] VERIFYING SYSTEM..."
node -v
npm -v

echo ""
echo "[6] CLEANING CACHE..."
npm cache clean --force

echo ""
echo "[7] INSTALLING PLATFORM CORE..."
npm install --legacy-peer-deps

echo ""
echo "[8] INSTALLING ELECTRON..."
npm install electron@28 --save-dev --force

echo ""
echo "[9] INSTALLING ELECTRON BUILDER..."
npm install electron-builder --save-dev --force

echo ""
echo "[10] PATCHING PACKAGE..."

node <<PATCH

const fs = require('fs');

const pkg = JSON.parse(fs.readFileSync('package.json'));

pkg.name = pkg.name || "huda-nuclear-ai";
pkg.version = pkg.version || "1.0.0";
pkg.main = pkg.main || "main.js";

pkg.scripts = pkg.scripts || {};

pkg.scripts.start = "npx electron .";
pkg.scripts["build-linux"] = "npx electron-builder --linux";
pkg.scripts["build-win"] = "npx electron-builder --win";

pkg.devDependencies = pkg.devDependencies || {};

pkg.devDependencies.electron = "^28.0.0";
pkg.devDependencies["electron-builder"] = "^24.13.3";

pkg.build = {
  appId: "com.huda.nuclear.ai",
  productName: "HUDA Nuclear AI",
  linux: {
    target: ["AppImage"],
    category: "Development"
  },
  win: {
    target: ["nsis"]
  }
};

fs.writeFileSync('package.json', JSON.stringify(pkg,null,2));

console.log("PACKAGE PATCHED SUCCESSFULLY");

PATCH

echo ""
echo "[11] REINSTALLING FULL PLATFORM..."
npm install --force

echo ""
echo "[12] TESTING ELECTRON..."
npx electron --version

echo ""
echo "[13] STARTING DESKTOP AI..."
npm start &

sleep 8

echo ""
echo "[14] BUILDING LINUX APPIMAGE..."
npm run build-linux

echo ""
echo "[15] BUILDING WINDOWS EXE..."
npm run build-win

echo ""
echo "=================================================="
echo "         HUDA NUCLEAR AI READY"
echo "=================================================="
echo ""

echo "LINUX OUTPUT:"
echo "$BASE/dist"

echo ""
echo "WINDOWS EXE:"
echo "$BASE/dist"

echo ""
echo "START PLATFORM:"
echo "cd $BASE && npm start"

echo ""
echo "DONE."


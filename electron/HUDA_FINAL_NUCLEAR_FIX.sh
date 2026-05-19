#!/bin/bash

clear

echo "======================================================"
echo "        HUDA FINAL NUCLEAR ELECTRON FIX"
echo "======================================================"
echo ""

BASE="$HOME/HUDA_NUCLEAR_DESKTOP/electron"

echo "[1] ENTERING PLATFORM..."
cd "$BASE" || exit

echo ""
echo "[2] DESTROYING BROKEN ELECTRON..."
rm -rf node_modules/electron
rm -rf node_modules/.cache
rm -rf node_modules
rm -rf package-lock.json
rm -rf ~/.cache/electron
rm -rf ~/.cache/electron-builder
rm -rf ~/.npm/_npx

echo ""
echo "[3] CLEANING NPM..."
npm cache clean --force

echo ""
echo "[4] VERIFY NODE..."
node -v
npm -v

echo ""
echo "[5] INSTALLING CORE..."
npm install --legacy-peer-deps --force

echo ""
echo "[6] INSTALLING ELECTRON STABLE..."
npm install electron@28.3.3 --save-dev --force

echo ""
echo "[7] INSTALLING ELECTRON BUILDER..."
npm install electron-builder@24.13.3 --save-dev --force

echo ""
echo "[8] PATCHING PACKAGE..."

node <<PATCH

const fs = require('fs');

const pkg = JSON.parse(fs.readFileSync('package.json'));

pkg.name = "huda-nuclear-ai";
pkg.version = "1.0.0";
pkg.main = pkg.main || "main.js";

pkg.scripts = {
  "start": "npx electron .",
  "build-linux": "npx electron-builder --linux",
  "build-win": "npx electron-builder --win"
};

pkg.devDependencies = pkg.devDependencies || {};

pkg.devDependencies.electron = "28.3.3";
pkg.devDependencies["electron-builder"] = "24.13.3";

pkg.build = {
  appId: "com.huda.nuclear.ai",
  productName: "HUDA Nuclear AI",
  directories: {
    output: "dist"
  },
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
echo "[9] REINSTALLING FULL PLATFORM..."
npm install --force

echo ""
echo "[10] VERIFY ELECTRON..."
npx electron --version

echo ""
echo "[11] STARTING AI DESKTOP..."
npm start &

sleep 10

echo ""
echo "[12] BUILDING LINUX APPIMAGE..."
npm run build-linux

echo ""
echo "[13] BUILDING WINDOWS EXE..."
npm run build-win

echo ""
echo "======================================================"
echo "           HUDA NUCLEAR AI READY"
echo "======================================================"
echo ""

echo "OUTPUT:"
echo "$BASE/dist"

echo ""
echo "START:"
echo "cd $BASE && npm start"

echo ""
echo "DONE."


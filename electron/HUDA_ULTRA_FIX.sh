#!/bin/bash

clear

echo "==============================================="
echo "      HUDA ULTRA ELECTRON RECOVERY ENGINE"
echo "==============================================="
echo ""

BASE="$HOME/HUDA_NUCLEAR_DESKTOP/electron"

cd "$BASE" || exit

echo "[1] PURGING BROKEN INSTALL..."
rm -rf node_modules
rm -rf package-lock.json
rm -rf ~/.npm
rm -rf ~/.cache/electron
rm -rf ~/.cache/electron-builder

echo ""
echo "[2] CLEANING SYSTEM..."
sudo apt update
sudo apt install -f -y
sudo dpkg --configure -a

echo ""
echo "[3] FIXING NODE..."
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs

echo ""
echo "[4] VERIFY..."
node -v
npm -v

echo ""
echo "[5] INSTALLING CORE..."
npm install --legacy-peer-deps

echo ""
echo "[6] INSTALLING ELECTRON..."
npm install electron@32.2.0 --save-dev --force

echo ""
echo "[7] INSTALLING ELECTRON BUILDER..."
npm install electron-builder --save-dev --force

echo ""
echo "[8] PATCHING PACKAGE.JSON..."

node <<PATCH

const fs = require('fs');

const pkg = JSON.parse(fs.readFileSync('package.json'));

pkg.main = pkg.main || "main.js";

pkg.scripts = pkg.scripts || {};

pkg.scripts.start = "npx electron .";
pkg.scripts["build-linux"] = "npx electron-builder --linux";
pkg.scripts["build-win"] = "npx electron-builder --win";

pkg.devDependencies = pkg.devDependencies || {};

pkg.devDependencies.electron = "^32.2.0";
pkg.devDependencies["electron-builder"] = "^24.13.3";

fs.writeFileSync('package.json', JSON.stringify(pkg,null,2));

console.log("PACKAGE PATCHED");

PATCH

echo ""
echo "[9] REINSTALLING CLEAN..."
npm install --force

echo ""
echo "[10] STARTING AI PLATFORM..."
npm start

echo ""
echo "==============================================="
echo "        HUDA AI DESKTOP READY"
echo "==============================================="
echo ""


#!/bin/bash

clear

echo "=================================================="
echo "        HUDA NUCLEAR ELECTRON RECOVERY"
echo "=================================================="

BASE="$HOME/HUDA_NUCLEAR_DESKTOP/electron"

cd "$BASE" || exit

echo ""
echo "[1] CLEANING BROKEN FILES..."
rm -rf node_modules
rm -rf package-lock.json
rm -rf ~/.cache/electron
rm -rf ~/.cache/electron-builder
rm -rf ~/.npm/_npx
rm -rf dist

echo ""
echo "[2] FIXING NPM..."
npm cache clean --force

echo ""
echo "[3] INSTALLING DEPENDENCIES..."
npm install

echo ""
echo "[4] INSTALLING ELECTRON..."
npm install electron@28 electron-builder@26 --save-dev

echo ""
echo "[5] VERIFY ELECTRON..."
npx electron --version

echo ""
echo "[6] STARTING DESKTOP AI..."
npm start &

sleep 8

echo ""
echo "[7] BUILDING LINUX APPIMAGE..."
npx electron-builder --linux AppImage

echo ""
echo "[8] BUILDING WINDOWS EXE..."
npx electron-builder --win portable

echo ""
echo "=================================================="
echo "              HUDA AI READY"
echo "=================================================="

echo ""
echo "OUTPUT:"
echo "$BASE/dist"

echo ""
echo "APPIMAGE:"
find dist -name "*.AppImage"

echo ""
echo "WINDOWS EXE:"
find dist -name "*.exe"

echo ""
echo "START SYSTEM:"
echo "cd $BASE && npm start"

echo ""
echo "DONE."


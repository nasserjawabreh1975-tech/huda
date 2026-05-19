#!/bin/bash

clear

echo "======================================"
echo " HUDA ELECTRON FINAL RECOVERY"
echo "======================================"

BASE="$HOME/HUDA_NUCLEAR_DESKTOP/electron"

cd "$BASE" || exit

echo ""
echo "[1] CLEANING BROKEN ELECTRON CACHE..."
rm -rf ~/.cache/electron
rm -rf ~/.cache/electron-builder
rm -rf ~/.npm/_npx
rm -rf node_modules/electron

echo ""
echo "[2] REINSTALLING ELECTRON..."
npm install electron@28.3.3 --save-dev --force

echo ""
echo "[3] VERIFYING ELECTRON..."
./node_modules/.bin/electron --version

echo ""
echo "[4] STARTING HUDA AI..."
./node_modules/.bin/electron . &

sleep 8

echo ""
echo "[5] BUILDING LINUX APPIMAGE..."
./node_modules/.bin/electron-builder --linux AppImage

echo ""
echo "[6] BUILDING WINDOWS EXE..."
./node_modules/.bin/electron-builder --win portable

echo ""
echo "======================================"
echo " HUDA AI FINALIZED"
echo "======================================"

echo ""
echo "OUTPUT:"
echo "$BASE/dist"

echo ""
echo "APPIMAGE:"
find dist -name "*.AppImage"

echo ""
echo "WINDOWS EXE:"
find dist -name "*.exe"


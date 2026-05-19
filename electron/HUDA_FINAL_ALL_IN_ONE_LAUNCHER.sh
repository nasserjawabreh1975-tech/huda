#!/bin/bash

clear

echo "======================================================="
echo "          HUDA FINAL AI DESKTOP LAUNCHER"
echo "======================================================="
echo ""

BASE="$HOME/HUDA_NUCLEAR_DESKTOP/electron"

echo "[1] ENTERING PLATFORM..."
cd "$BASE" || exit

echo ""
echo "[2] VERIFY NODE..."
node -v
npm -v

echo ""
echo "[3] VERIFY ELECTRON..."
npx electron --version

echo ""
echo "[4] STARTING HUDA AI DESKTOP..."
npm start &

sleep 8

echo ""
echo "[5] BUILDING LINUX APPIMAGE..."
npm run build-linux

echo ""
echo "[6] BUILDING WINDOWS EXE..."
npm run build-win

echo ""
echo "======================================================="
echo "              HUDA AI PLATFORM READY"
echo "======================================================="
echo ""

echo "DIST OUTPUT:"
echo "$BASE/dist"

echo ""
echo "LINUX APPIMAGE:"
find "$BASE/dist" -name "*.AppImage"

echo ""
echo "WINDOWS EXE:"
find "$BASE/dist" -name "*.exe"

echo ""
echo "START AGAIN:"
echo "cd $BASE && npm start"

echo ""
echo "DONE."


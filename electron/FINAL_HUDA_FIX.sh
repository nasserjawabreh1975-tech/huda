#!/bin/bash

clear

echo "=========================================="
echo "      HUDA FINAL ELECTRON RECOVERY"
echo "=========================================="

BASE="$HOME/HUDA_NUCLEAR_DESKTOP/electron"

cd "$BASE" || exit

echo ""
echo "[1] FULL CLEAN..."
rm -rf node_modules
rm -rf package-lock.json
rm -rf dist
rm -rf ~/.cache/electron
rm -rf ~/.cache/electron-builder
rm -rf ~/.npm/_npx

echo ""
echo "[2] CLEAN CACHE..."
npm cache clean --force

echo ""
echo "[3] INSTALL CORE..."
npm install

echo ""
echo "[4] INSTALL ELECTRON STACK..."
npm install --save-dev \
electron@28.3.3 \
electron-builder@24.13.3 \
@electron/rebuild

echo ""
echo "[5] REBUILD..."
npx electron-rebuild

echo ""
echo "[6] VERIFY..."
npx electron --version
npx electron-builder --version

echo ""
echo "[7] START AI..."
npm start &

sleep 10

echo ""
echo "[8] BUILD LINUX..."
npx electron-builder --linux AppImage

echo ""
echo "[9] BUILD WINDOWS EXE..."
npx electron-builder --win portable

echo ""
echo "=========================================="
echo "          HUDA PLATFORM READY"
echo "=========================================="

echo ""
echo "DIST:"
echo "$BASE/dist"

echo ""
echo "APPIMAGE:"
find dist -name "*.AppImage"

echo ""
echo "WINDOWS EXE:"
find dist -name "*.exe"

echo ""
echo "START:"
echo "cd $BASE && npm start"

echo ""
echo "DONE"


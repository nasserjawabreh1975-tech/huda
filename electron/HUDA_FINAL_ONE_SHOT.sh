#!/bin/bash

clear

echo "=============================================="
echo "     HUDA FINAL ELECTRON RECOVERY"
echo "=============================================="

echo ""
echo "[1] CREATING 8GB SWAP..."
sudo swapoff /swapfile 2>/dev/null
sudo rm -f /swapfile

sudo fallocate -l 8G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

echo ""
echo "[2] MEMORY STATUS..."
free -h

echo ""
echo "[3] ENTERING PROJECT..."
cd ~/HUDA_NUCLEAR_DESKTOP/electron || exit

echo ""
echo "[4] FULL CLEAN..."
rm -rf node_modules
rm -rf package-lock.json
rm -rf ~/.npm
rm -rf ~/.cache/electron
rm -rf ~/.cache/electron-builder

echo ""
echo "[5] INSTALLING REQUIRED SYSTEM LIBS..."
sudo apt update

sudo apt install -y \
curl \
wget \
build-essential \
libgtk-3-0 \
libnotify4 \
libnss3 \
libxss1 \
libxtst6 \
xdg-utils \
libatspi2.0-0 \
libuuid1 \
libsecret-1-0 \
libasound2t64

echo ""
echo "[6] INSTALLING NODE 18 LTS..."
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -

sudo apt install -y nodejs

echo ""
echo "NODE VERSION:"
node -v

echo ""
echo "[7] INSTALLING PROJECT..."
npm install

echo ""
echo "[8] INSTALLING ELECTRON..."
npm install electron@28.3.3 \
electron-builder@24.13.3 \
@electron/get \
debug \
extract-zip \
--save-dev --force

echo ""
echo "[9] VERIFYING ELECTRON..."
ls node_modules/electron/dist

echo ""
echo "[10] STARTING HUDA DESKTOP..."
./node_modules/electron/dist/electron . &

sleep 10

echo ""
echo "[11] BUILDING LINUX APPIMAGE..."
./node_modules/.bin/electron-builder --linux AppImage

echo ""
echo "[12] BUILDING WINDOWS EXE..."
./node_modules/.bin/electron-builder --win portable

echo ""
echo "=============================================="
echo "         HUDA DESKTOP READY"
echo "=============================================="

echo ""
echo "DIST:"
echo ~/HUDA_NUCLEAR_DESKTOP/electron/dist

echo ""
echo "APPIMAGE:"
find dist -name "*.AppImage"

echo ""
echo "WINDOWS EXE:"
find dist -name "*.exe"


#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
if ! pkg-config --exists gtk4; then
  echo 'GTK4 development files are required to build the graphical display.' >&2
  echo 'On Debian/Ubuntu: sudo apt install libgtk-4-dev liblua5.4-dev libglib2.0-dev libncurses-dev' >&2
  exit 1
fi
# Recompile all objects to remove the terminal-only build flag.
make clean
make UI=gui LUA_VERSION=lua5.4 -j"$(nproc)"
echo 'Graphical executable: dist/x50ng'

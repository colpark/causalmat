#!/usr/bin/env bash
# Download MatMech v5 from figshare (10.6084/m9.figshare.29815979), verify MD5, extract to ./matmech
set -euo pipefail
cd "$(dirname "$0")/.."
curl -L -C - --retry 20 --retry-delay 10 --retry-all-errors -o matmech.zip https://ndownloader.figshare.com/files/60282110
echo "e56587094485d19b2595ee38339843e9  matmech.zip" | md5sum -c -
unzip -q -n matmech.zip
test "$(find matmech -name data.json | wc -l)" -eq 61766 && echo "61766 records extracted"

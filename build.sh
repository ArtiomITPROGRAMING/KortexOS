#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

mkdir -p profile out cache/pacman/pkg

clean_work() {
    echo "[*] Cleaning work directory..."
    rm -rf work/* 2>/dev/null || true
}

if [ "${1:-}" = "clean" ]; then
    clean_work
    echo "[*] Cleaning out directory..."
    rm -rf out/* 2>/dev/null || true
    echo "[+] Clean complete."
    exit 0
fi

clean_work

echo "[*] Building KortexOS ISO in privileged Docker container..."
docker run --rm --privileged \
    -v "$SCRIPT_DIR/profile:/workspace/profile" \
    -v "$SCRIPT_DIR/out:/workspace/out" \
    -v "$SCRIPT_DIR/cache/pacman/pkg:/var/cache/pacman/pkg" \
    -v /dev:/dev \
    archlinux:latest \
    bash -c '
        set -euo pipefail
        echo "[*] Installing/updating archiso in builder container..."
        pacman -Syu --noconfirm --needed archiso
        echo "[*] Running mkarchiso..."
        rm -rf /tmp/kortex-work
        mkdir -p /tmp/kortex-work
        mkarchiso -v -w /tmp/kortex-work -o /workspace/out /workspace/profile
        rm -rf /tmp/kortex-work
        
        echo "[*] Updating kortexos-latest.iso and kortexos-v1.0.0-x86_64.iso..."
        latest_iso=$(ls -t /workspace/out/kortexos-*.iso 2>/dev/null | grep -v "latest" | grep -v "v1.0.0" | head -n 1 || true)
        if [ -n "$latest_iso" ]; then
            cp -f "$latest_iso" /workspace/out/kortexos-latest.iso
            cp -f "$latest_iso" /workspace/out/kortexos-v1.0.0-x86_64.iso
            echo "[+] Successfully created kortexos-latest.iso and kortexos-v1.0.0-x86_64.iso from $latest_iso"
        fi
        echo "[*] Computing SHA256 and SHA512 checksums..."
        cd /workspace/out
        sha256sum kortexos-v1.0.0-x86_64.iso kortexos-latest.iso > SHA256SUMS.txt 2>/dev/null || true
        sha512sum kortexos-v1.0.0-x86_64.iso kortexos-latest.iso > SHA512SUMS.txt 2>/dev/null || true
        chown -R 1000:1000 /workspace/out 2>/dev/null || true
    '

echo "[+] Build finished successfully. ISO image available in ./out/kortexos-latest.iso"

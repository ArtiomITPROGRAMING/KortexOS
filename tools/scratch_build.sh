#!/usr/bin/env bash
set -euo pipefail

echo "[*] Cleaning work directory..."
tmux kill-session -t kortex_build 2>/dev/null || true
docker run --rm -v /home/developper/KortexOS:/workspace archlinux:latest rm -rf /workspace/work

echo "[*] Launching mkarchiso in tmux session 'kortex_build'..."
tmux new-session -d -s kortex_build "docker run --rm --privileged -v /home/developper/KortexOS:/workspace -v /home/developper/KortexOS/cache/pacman/pkg:/var/cache/pacman/pkg -v /dev:/dev archlinux:latest bash -c 'set -euo pipefail; pacman -Sy --noconfirm --needed archiso; mkarchiso -v -w /workspace/work -o /workspace/out /workspace/profile; chown -R 1000:1000 /workspace/out /workspace/work 2>/dev/null || true; echo [+] BUILD_SUCCESS'"

sleep 2
tmux ls

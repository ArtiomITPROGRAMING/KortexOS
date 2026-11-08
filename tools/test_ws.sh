#!/usr/bin/env bash
for d in /run/user/1000/hypr/*; do
    if [ -d "$d" ]; then
        export HYPRLAND_INSTANCE_SIGNATURE="$(basename "$d")"
        break
    fi
done
export XDG_RUNTIME_DIR="/run/user/1000"
export WAYLAND_DISPLAY="wayland-1"

hyprctl dispatch 'hl.dsp.focus({ workspace = 1 })'

#!/bin/bash
killall -9 kitty waybar 2>/dev/null
sleep 1
export XDG_RUNTIME_DIR=/run/user/1000
W_SOCK=$(find /run/user/1000 -maxdepth 1 -name "wayland-*" -type s 2>/dev/null | head -n1)
export WAYLAND_DISPLAY=$(basename "$W_SOCK")
HYPR_DIR=$(find /run/user/1000/hypr -maxdepth 1 -mindepth 1 -type d 2>/dev/null | head -n1)
export HYPRLAND_INSTANCE_SIGNATURE=$(basename "$HYPR_DIR")

echo "WAYLAND_DISPLAY=$WAYLAND_DISPLAY HYPRLAND_INSTANCE_SIGNATURE=$HYPRLAND_INSTANCE_SIGNATURE"

runuser -u kortex -- env XDG_RUNTIME_DIR=/run/user/1000 WAYLAND_DISPLAY=$WAYLAND_DISPLAY HYPRLAND_INSTANCE_SIGNATURE=$HYPRLAND_INSTANCE_SIGNATURE nohup waybar >/dev/null 2>&1 &
sleep 0.5
runuser -u kortex -- env XDG_RUNTIME_DIR=/run/user/1000 WAYLAND_DISPLAY=$WAYLAND_DISPLAY HYPRLAND_INSTANCE_SIGNATURE=$HYPRLAND_INSTANCE_SIGNATURE /usr/local/bin/kortex-grid-init

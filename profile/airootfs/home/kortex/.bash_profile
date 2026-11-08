# Auto-start Hyprland on tty1 login
if [[ -z "$DISPLAY" ]] && [[ $(tty) == "/dev/tty1" ]]; then
    rm -f ~/.config/hypr/hyprland.lua /home/kortex/.config/hypr/hyprland.lua /etc/skel/.config/hypr/hyprland.lua 2>/dev/null || true
    mkdir -p ~/.config/hypr /home/kortex/.config/hypr 2>/dev/null || true
    if [ -d /etc/skel/.config ]; then
        cp -rf /etc/skel/.config/* ~/.config/ 2>/dev/null || true
        cp -rf /etc/skel/.config/* /home/kortex/.config/ 2>/dev/null || true
    fi
    rm -rf ~/.cache/hyprland* /run/user/$(id -u)/hypr/* 2>/dev/null || true
    export HYPRLAND_CONFIG=/home/kortex/.config/hypr/hyprland.conf
    exec Hyprland -c /home/kortex/.config/hypr/hyprland.conf
fi

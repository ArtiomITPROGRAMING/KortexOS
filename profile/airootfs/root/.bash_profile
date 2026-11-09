# Auto-start Hyprland on tty1 login
if [[ -z "$DISPLAY" ]] && [[ $(tty) == "/dev/tty1" ]]; then
    mkdir -p ~/.config/hypr 2>/dev/null || true
    if [ -d /etc/skel/.config ] && [ ! -f ~/.config/hypr/hyprland.lua ]; then
        cp -rf /etc/skel/.config/* ~/.config/ 2>/dev/null || true
    fi
    rm -rf ~/.cache/hyprland* /run/user/$(id -u)/hypr/* 2>/dev/null || true
    exec /usr/bin/start-hyprland
fi

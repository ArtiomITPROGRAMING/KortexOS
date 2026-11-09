# Auto-start Hyprland on tty1 login
if [[ -z "$DISPLAY" ]] && [[ $(tty) == "/dev/tty1" ]]; then
    export XDG_RUNTIME_DIR="${XDG_RUNTIME_DIR:-/run/user/$(id -u)}"
    mkdir -p "$XDG_RUNTIME_DIR/hypr" ~/.config/hypr ~/.config/kortex 2>/dev/null || true
    if [ -d /etc/skel/.config ] && [ ! -f ~/.config/hypr/hyprland.lua ]; then
        cp -rf /etc/skel/.config/* ~/.config/ 2>/dev/null || true
    fi
    rm -f ~/.config/hypr/hyprland.conf 2>/dev/null || true
    rm -rf ~/.cache/hyprland* "$XDG_RUNTIME_DIR"/hypr/* 2>/dev/null || true
    exec /usr/bin/start-hyprland
fi

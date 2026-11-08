# ==============================================================================
# KORTEX-OS BASH CONFIGURATION
# Pure Cyberpunk Monochrome (eDEX-UI Style)
# ==============================================================================

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=never'
alias grep='grep --color=never'
alias ll='ls -lh'
alias la='ls -lha'

# Pure Monochrome Prompt
PS1='\[\e[1;37m\][\u@\h \W]\$ \[\e[0m\]'

# eDEX-UI Cyberpunk Boot Header (if in terminal)
if [ -z "${KORTEX_HEADER_PRINTED:-}" ]; then
    export KORTEX_HEADER_PRINTED=1
    echo -e "\e[1;37mKORTEX-OS v1.0.0 // ARCH-ZEN KERNEL // LOW-LATENCY SYSTEM\e[0m"
    echo -e "\e[1;37mBUILD TARGET: x86_64 // GRID ENGINE: HYPRLAND WAYLAND\e[0m"
    echo -e "\e[0;37m[    0.000000] system core: linux-zen low-latency kernel v7.2.14-zen\e[0m"
    echo -e "\e[0;37m[    0.012480] display server: hyprland wayland compositor [1920x1080@60]\e[0m"
    echo -e "\e[0;37m[    0.024190] kortex-intelligence-engine (KIS): telemetry daemon active\e[0m"
    echo -e "\e[0;37m[    0.038910] kortex-sys-panel: hardware telemetry & cpu monitor mounted\e[0m"
    echo -e "\e[0;37m[    0.045230] kortex-net-monitor: 3d braille globe & live traffic linked\e[0m"
    echo -e "\e[0;37m[    0.051870] kortex-file-grid: virtual workspace directory matrix loaded\e[0m"
    echo -e "\e[0;37m[    0.063120] kortex-keyboard: full-matrix qwerty hardware input ready\e[0m"
    echo -e "\e[0;37m[    0.080000] audio server: pipewire low-latency quantum configured\e[0m"
    echo -e "\e[0;37m[    0.100000] system initialized: all 5 modules active on workspace 1\e[0m"
    echo ""
fi

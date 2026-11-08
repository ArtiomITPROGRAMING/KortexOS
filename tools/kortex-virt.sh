if systemd-detect-virt --quiet 2>/dev/null; then
    export LIBGL_ALWAYS_SOFTWARE=1
    export WLR_RENDERER_ALLOW_SOFTWARE=1
fi

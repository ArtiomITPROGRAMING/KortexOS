#!/usr/bin/env bash
if systemd-detect-virt --quiet 2>/dev/null; then
    export AQ_NO_MODIFIERS=1
    export LIBGL_ALWAYS_SOFTWARE=1
    export WLR_RENDERER_ALLOW_SOFTWARE=1
    export WLR_NO_HARDWARE_CURSORS=1
fi

-- ==============================================================================
-- KORTEX-OS LIVE GENERATED HYPRLAND 0.57+ LUA THEME
-- Managed by Kortex Unified Design & Persistence Engine
-- ==============================================================================

hl.config({
    general = {
        border_size = 2,
        gaps_in = 6,
        gaps_out = 10,
        col = {
            active_border = { colors = {"rgb(00f0ff)", "rgb(0088cc)"}, angle = 45 },
            inactive_border = "rgb(1b2430)",
        },
    },
    decoration = {
        rounding = 6,
        active_opacity = 0.95,
        inactive_opacity = 0.85,
        shadow = {
            enabled = true,
            range = 15,
            render_power = 3,
            color = "rgba(00f0ff66)",
        },
        glow = {
            enabled = false,
            range = 15,
            render_power = 3,
            color = "rgba(00f0ff66)",
        },
        blur = {
            enabled = true,
            size = 8,
            passes = 3,
            new_optimizations = true,
            xray = false,
            vibrancy = 0.1696,
        },
    },
    animations = {
        enabled = true,
    },
    input = {
        kb_layout = "us,ru",
        kb_options = "grp:alt_shift_toggle",
    },
})

hl.animation({ leaf = "borderangle", enabled = false, speed = 28, bezier = "linear", style = "loop" })

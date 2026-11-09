-- ==============================================================================
-- KORTEX-OS HYPRLAND MASTER LUA CONFIGURATION (Hyprland 0.57+)
-- Modular Cyberpunk Tiling Grid & Classic Desktop Hybrid
-- ==============================================================================

------------------
---- MONITORS ----
------------------

hl.monitor({
    output   = "",
    mode     = "preferred",
    position = "auto",
    scale    = "auto",
})

-------------------------------
---- ENVIRONMENT VARIABLES ----
-------------------------------

hl.env("XDG_CURRENT_DESKTOP", "Hyprland")
hl.env("XDG_SESSION_TYPE", "wayland")
hl.env("XDG_SESSION_DESKTOP", "Hyprland")
hl.env("QT_QPA_PLATFORM", "wayland;xcb")
hl.env("GDK_BACKEND", "wayland,x11")
hl.env("SDL_VIDEODRIVER", "wayland")
hl.env("CLUTTER_BACKEND", "wayland")
hl.env("MOZ_ENABLE_WAYLAND", "1")
hl.env("WLR_NO_HARDWARE_CURSORS", "1")
hl.env("XCURSOR_SIZE", "24")
hl.env("HYPRCURSOR_SIZE", "24")

-----------------------
---- LOOK AND FEEL ----
-----------------------

hl.config({
    general = {
        gaps_in  = 6,
        gaps_out = 10,
        border_size = 2,
        col = {
            active_border   = "rgb(00f0ff)",
            inactive_border = "rgb(003344)",
        },
        layout = "dwindle",
        resize_on_border = true,
        allow_tearing = false,
    },

    decoration = {
        rounding       = 6,
        rounding_power = 2,
        active_opacity   = 0.95,
        inactive_opacity = 0.90,

        shadow = {
            enabled      = true,
            range        = 14,
            render_power = 2,
            color        = 0x3300f0ff,
        },

        blur = {
            enabled  = true,
            size     = 4,
            passes   = 2,
            vibrancy = 0.1696,
        },
    },

    animations = {
        enabled = true,
    },

    dwindle = {
        pseudotile = true,
        preserve_split = true,
    },

    misc = {
        disable_hyprland_logo   = true,
        disable_splash_rendering = true,
        force_default_wallpaper = 0,
    },

    input = {
        kb_layout  = "us,ru",
        kb_options = "grp:win_space_toggle",
        follow_mouse = 1,
        touchpad = {
            natural_scroll = true,
            tap-to-click   = true,
        },
        sensitivity = 0,
    },
})

--------------------
---- ANIMATIONS ----
--------------------

hl.curve("easeOutQuint",   { type = "bezier", points = { {0.23, 1},    {0.32, 1} } })
hl.curve("easeInOutCubic", { type = "bezier", points = { {0.65, 0.05}, {0.36, 1} } })
hl.curve("linear",         { type = "bezier", points = { {0, 0},       {1, 1}    } })
hl.curve("almostLinear",   { type = "bezier", points = { {0.5, 0.5},   {0.75, 1} } })
hl.curve("quick",          { type = "bezier", points = { {0.15, 0},    {0.1, 1}  } })
hl.curve("easy",           { type = "spring", mass = 1, stiffness = 238.1191, damping = 24.21279333 })

hl.animation({ leaf = "global",        enabled = true, speed = 10,   bezier = "default" })
hl.animation({ leaf = "border",        enabled = true, speed = 5.39, bezier = "easeOutQuint" })
hl.animation({ leaf = "windows",       enabled = true, speed = 4.79, spring = "easy" })
hl.animation({ leaf = "windowsIn",     enabled = true, speed = 4.1,  spring = "easy",         style = "popin 87%" })
hl.animation({ leaf = "windowsOut",    enabled = true, speed = 1.49, bezier = "linear",       style = "popin 87%" })
hl.animation({ leaf = "fadeIn",        enabled = true, speed = 1.73, bezier = "almostLinear" })
hl.animation({ leaf = "fadeOut",       enabled = true, speed = 1.46, bezier = "almostLinear" })
hl.animation({ leaf = "fade",          enabled = true, speed = 3.03, bezier = "quick" })
hl.animation({ leaf = "layers",        enabled = true, speed = 3.81, bezier = "easeOutQuint" })
hl.animation({ leaf = "workspaces",    enabled = true, speed = 1.94, bezier = "almostLinear", style = "fade" })

----------------------
---- WINDOW RULES ----
----------------------

-- Kortex Grid Modules
hl.window_rule({ match = { class = "kortex-pulse" }, float = true, move = "0.5% 4%", size = "19% 95%" })
hl.window_rule({ match = { class = "kortex-term" },  float = true, move = "20% 4%",   size = "57% 62%" })
hl.window_rule({ match = { class = "kortex-net" },   float = true, move = "77.5% 4%", size = "22% 62%" })
hl.window_rule({ match = { class = "kortex-files" }, float = true, move = "20% 67%",  size = "33% 32%" })
hl.window_rule({ match = { class = "kortex-kb" },    float = true, move = "53.5% 67%",size = "46% 32%" })

-- KIS System Dialogs
hl.window_rule({ match = { class = "kortex-install" },   float = true, move = "18% 12%", size = "64% 76%" })
hl.window_rule({ match = { class = "kortex-settings" },  float = true, move = "18% 12%", size = "64% 76%" })
hl.window_rule({ match = { class = "kortex-setting" },   float = true, move = "18% 12%", size = "64% 76%" })
hl.window_rule({ match = { class = "kortex-ai" },        float = true, move = "18% 12%", size = "64% 76%" })
hl.window_rule({ match = { class = "kortex-store" },     float = true, move = "18% 12%", size = "64% 76%" })
hl.window_rule({ match = { class = "kortex-net-guard" }, float = true, move = "18% 12%", size = "64% 76%" })
hl.window_rule({ match = { class = "kortex-link" },      float = true, move = "18% 12%", size = "64% 76%" })
hl.window_rule({ match = { class = "kortex-vault" },     float = true, move = "18% 12%", size = "64% 76%" })
hl.window_rule({ match = { class = "kortex-lock" },      fullscreen = true })

-- Dialogs & Utilities
hl.window_rule({ match = { class = "pavucontrol" },          float = true })
hl.window_rule({ match = { class = "nm-connection-editor" }, float = true })
hl.window_rule({ match = { class = "imv" },                  float = true })
hl.window_rule({ match = { class = "mpv" },                  float = true })
hl.window_rule({ match = { class = "kortex-oobe" },          float = true })
hl.window_rule({ match = { class = "kortex-tour" },          float = true, size = { 1000, 680 } })
hl.window_rule({ match = { class = "kortex-music" },         float = true, size = { 960, 620 } })

-------------------
---- AUTOSTART ----
-------------------

hl.on("hyprland.start", function()
    hl.exec_cmd("hyprpaper &")
    hl.exec_cmd("waybar &")
    hl.exec_cmd("/usr/lib/polkit-kde-authentication-agent-1 &")
    hl.exec_cmd("/usr/local/bin/kortex-audio-fx &")
    hl.exec_cmd("/usr/local/bin/kortex-link-daemon &")
    hl.exec_cmd("/usr/local/bin/kortex-theme-apply &")
    hl.exec_cmd("[ ! -f ~/.config/kortex/.setup_done ] && kitty --class kortex-oobe --title 'KORTEX-OS SETUP' -e /usr/local/bin/kortex-oobe &")
    hl.exec_cmd("sleep 0.5 && /usr/local/bin/kortex-grid-init &")
end)

---------------------
---- KEYBINDINGS ----
---------------------

local mainMod = "SUPER"

-- Core System & App Binds
hl.bind(mainMod .. " + Q", hl.dsp.window.close())
hl.bind("ALT + F4", hl.dsp.window.close())
hl.bind(mainMod .. " + F", hl.dsp.window.fullscreen({ action = "toggle" }))
hl.bind(mainMod .. " + V", hl.dsp.window.float({ action = "toggle" }))
hl.bind(mainMod .. " + Return", hl.dsp.exec_cmd("/usr/local/bin/kortex-launch kitty"))
hl.bind(mainMod .. " + Space", hl.dsp.exec_cmd("pkill rofi || /usr/local/bin/kortex-spotlight"))
hl.bind(mainMod .. " + D", hl.dsp.exec_cmd("pkill rofi || /usr/local/bin/kortex-menu"))
hl.bind(mainMod .. " + Tab", hl.dsp.exec_cmd("/usr/local/bin/kortex-layout next"))
hl.bind(mainMod .. " + B", hl.dsp.exec_cmd("/usr/local/bin/kortex-launch firefox || /usr/local/bin/kortex-launch chromium || kitty"))
hl.bind(mainMod .. " + E", hl.dsp.exec_cmd("kitty --class kortex-files -e yazi"))
hl.bind(mainMod .. " + G", hl.dsp.exec_cmd("/usr/local/bin/kortex-grid-init"))
hl.bind(mainMod .. " + F1", hl.dsp.exec_cmd("/usr/local/bin/kortex-help-hud"))
hl.bind(mainMod .. " + M", hl.dsp.exec_cmd("/usr/local/bin/kortex-open link"))

-- Kortex Subsystems
hl.bind(mainMod .. " + S", hl.dsp.exec_cmd("/usr/local/bin/kortex-open settings"))
hl.bind(mainMod .. " + A", hl.dsp.exec_cmd("/usr/local/bin/kortex-open ai"))
hl.bind(mainMod .. " + P", hl.dsp.exec_cmd("/usr/local/bin/kortex-open store"))
hl.bind(mainMod .. " + N", hl.dsp.exec_cmd("/usr/local/bin/kortex-open net-guard"))
hl.bind(mainMod .. " + L", hl.dsp.exec_cmd("/usr/local/bin/kortex-open lock"))
hl.bind(mainMod .. " + I", hl.dsp.exec_cmd("/usr/local/bin/kortex-open install"))

-- Navigation & Focus
hl.bind(mainMod .. " + left",  hl.dsp.focus({ direction = "left" }))
hl.bind(mainMod .. " + right", hl.dsp.focus({ direction = "right" }))
hl.bind(mainMod .. " + up",    hl.dsp.focus({ direction = "up" }))
hl.bind(mainMod .. " + down",  hl.dsp.focus({ direction = "down" }))
hl.bind(mainMod .. " + h",     hl.dsp.focus({ direction = "left" }))
hl.bind(mainMod .. " + l",     hl.dsp.focus({ direction = "right" }))
hl.bind(mainMod .. " + k",     hl.dsp.focus({ direction = "up" }))
hl.bind(mainMod .. " + j",     hl.dsp.focus({ direction = "down" }))

-- Workspaces 1-5
for i = 1, 5 do
    hl.bind(mainMod .. " + " .. i, hl.dsp.focus({ workspace = i }))
    hl.bind(mainMod .. " + SHIFT + " .. i, hl.dsp.window.move({ workspace = i }))
end

-- Mouse Bindings
hl.bind(mainMod .. " + mouse:272", hl.dsp.window.drag(), { mouse = true })
hl.bind(mainMod .. " + mouse:273", hl.dsp.window.resize(), { mouse = true })

-- Media & Brightness Controls
hl.bind("XF86AudioRaiseVolume", hl.dsp.exec_cmd("wpctl set-volume -l 1.5 @DEFAULT_AUDIO_SINK@ 5%+"), { locked = true, repeating = true })
hl.bind("XF86AudioLowerVolume", hl.dsp.exec_cmd("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-"), { locked = true, repeating = true })
hl.bind("XF86AudioMute",        hl.dsp.exec_cmd("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle"), { locked = true })
hl.bind("XF86MonBrightnessUp",  hl.dsp.exec_cmd("brightnessctl set +10%"), { locked = true, repeating = true })
hl.bind("XF86MonBrightnessDown",hl.dsp.exec_cmd("brightnessctl set 10%-"), { locked = true, repeating = true })

-- Screenshots
hl.bind("PRINT", hl.dsp.exec_cmd("grim ~/screenshot_$(date +%s).png"))
hl.bind(mainMod .. " + PRINT", hl.dsp.exec_cmd("grim ~/screenshot_$(date +%s).png"))
hl.bind(mainMod .. " + SHIFT + S", hl.dsp.exec_cmd("grim -g \"$(slurp)\" - | wl-copy"))

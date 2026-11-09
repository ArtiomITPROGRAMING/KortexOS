-- ==============================================================================
-- KORTEX-OS HYPRLAND MASTER LUA CONFIGURATION (Hyprland 0.57.1+)
-- Unified Design & Persistence Engine (MacBook UX + Cyber-Deck)
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
hl.env("QT_QPA_PLATFORMTHEME", "qt6ct")
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
            active_border   = { colors = {"rgb(00f0ff)", "rgb(0088cc)"}, angle = 45 },
            inactive_border = "rgb(1b2430)",
        },
        layout = "dwindle",
        resize_on_border = true,
        allow_tearing = false,
    },

    decoration = {
        rounding       = 6,
        rounding_power = 2,
        active_opacity   = 0.95,
        inactive_opacity = 0.85,

        shadow = {
            enabled      = true,
            range        = 15,
            render_power = 3,
            color        = "rgba(00f0ff66)",
        },

        glow = {
            enabled      = false,
            range        = 15,
            render_power = 3,
            color        = "rgba(00f0ff66)",
        },

        blur = {
            enabled           = true,
            size              = 8,
            passes            = 3,
            new_optimizations = true,
            xray              = false,
            vibrancy          = 0.1696,
        },
    },

    animations = {
        enabled = true,
    },

    dwindle = {
        preserve_split = true,
    },

    misc = {
        disable_hyprland_logo    = true,
        disable_splash_rendering = true,
        force_default_wallpaper  = 0,
    },

    debug = {
        vfr = true,
    },

    input = {
        kb_layout    = "us,ru",
        kb_options   = "grp:alt_shift_toggle",
        follow_mouse = 1,
        touchpad = {
            natural_scroll = true,
            tap_to_click   = true,
        },
        sensitivity = 0,
    },

    gestures = {
        workspace_swipe_distance = 300,
        workspace_swipe_invert   = true,
        workspace_swipe_cancel_ratio = 0.5,
    },
})

-- MacBook 3-Finger Horizontal Workspace Swipe Gesture
hl.gesture({
    fingers   = 3,
    direction = "horizontal",
    action    = "workspace",
})

--------------------
---- ANIMATIONS ----
--------------------

hl.curve("easeOutQuint",   { type = "bezier", points = { {0.23, 1},    {0.32, 1} } })
hl.curve("easeInOutCubic", { type = "bezier", points = { {0.65, 0.05}, {0.36, 1} } })
hl.curve("linear",         { type = "bezier", points = { {0, 0},       {1, 1}    } })
hl.curve("almostLinear",   { type = "bezier", points = { {0.5, 0.5},   {0.75, 1} } })
hl.curve("quick",          { type = "bezier", points = { {0.15, 0},    {0.1, 1}  } })
hl.curve("easy",           { type = "spring", mass = 1, stiffness = 320.0, damping = 28.0 })

hl.animation({ leaf = "global",      enabled = true,  speed = 10,   bezier = "default" })
hl.animation({ leaf = "border",      enabled = true,  speed = 4.2,  bezier = "easeOutQuint" })
hl.animation({ leaf = "borderangle", enabled = false, speed = 28,   bezier = "linear", style = "loop" })
hl.animation({ leaf = "windows",     enabled = true,  speed = 5.5,  spring = "easy" })
hl.animation({ leaf = "windowsIn",   enabled = true,  speed = 5.8,  spring = "easy",         style = "popin 90%" })
hl.animation({ leaf = "windowsOut",  enabled = true,  speed = 3.2,  bezier = "quick",        style = "popin 90%" })
hl.animation({ leaf = "fadeIn",      enabled = true,  speed = 3.0,  bezier = "almostLinear" })
hl.animation({ leaf = "fadeOut",     enabled = true,  speed = 2.8,  bezier = "almostLinear" })
hl.animation({ leaf = "fade",        enabled = true,  speed = 4.5,  bezier = "quick" })
hl.animation({ leaf = "layers",      enabled = true,  speed = 4.5,  bezier = "easeOutQuint" })
hl.animation({ leaf = "workspaces",  enabled = true,  speed = 3.5,  bezier = "almostLinear", style = "fade" })

----------------------
---- WINDOW RULES ----
----------------------

-- Kortex Cyber-Deck 5-Module Grid
hl.window_rule({ match = { class = "kortex-pulse" }, float = true, move = "0.5% 4%",  size = "19% 95%" })
hl.window_rule({ match = { class = "kortex-term" },  float = true, move = "20% 4%",   size = "57% 62%" })
hl.window_rule({ match = { class = "kortex-net" },   float = true, move = "77.5% 4%", size = "22% 62%" })
hl.window_rule({ match = { class = "kortex-files" }, float = true, move = "20% 67%",  size = "33% 32%" })
hl.window_rule({ match = { class = "kortex-kb" },    float = true, move = "53.5% 67%",size = "46% 32%" })

-- OOBE Initial Setup Wizard (Fullscreen)
hl.window_rule({ match = { class = "kortex-oobe" }, fullscreen = true })

-- KIS System Dialogs
hl.window_rule({ match = { class = "kortex-install" },   float = true, move = "15% 10%", size = "70% 80%" })
hl.window_rule({ match = { class = "kortex-settings" },  float = true, move = "15% 10%", size = "70% 80%" })
hl.window_rule({ match = { class = "kortex-setting" },   float = true, move = "15% 10%", size = "70% 80%" })
hl.window_rule({ match = { class = "kortex-ai" },        float = true, move = "18% 12%", size = "64% 76%" })
hl.window_rule({ match = { class = "kortex-store" },     float = true, move = "18% 12%", size = "64% 76%" })
hl.window_rule({ match = { class = "kortex-net-guard" }, float = true, move = "18% 12%", size = "64% 76%" })
hl.window_rule({ match = { class = "kortex-link" },      float = true, move = "18% 12%", size = "64% 76%" })
hl.window_rule({ match = { class = "kortex-vault" },     float = true, move = "18% 12%", size = "64% 76%" })
hl.window_rule({ match = { class = "kortex-lock" },      fullscreen = true })

-- Utilities
hl.window_rule({ match = { class = "kortex-taskmgr" },       float = true, move = "15% 10%", size = "70% 80%" })
hl.window_rule({ match = { class = "pavucontrol" },          float = true })
hl.window_rule({ match = { class = "nm-connection-editor" }, float = true })
hl.window_rule({ match = { class = "imv" },                  float = true })
hl.window_rule({ match = { class = "mpv" },                  float = true })
hl.window_rule({ match = { class = "kortex-tour" },          float = true, size = { 1000, 680 } })
hl.window_rule({ match = { class = "kortex-music" },         float = true, size = { 960, 620 } })

-- Load persistent live theme override if present
pcall(dofile, (os.getenv("HOME") or "/home/kortex") .. "/.config/hypr/theme.lua")

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
    hl.exec_cmd("/usr/local/bin/kortex-grid-init &")
end)

---------------------
---- KEYBINDINGS ----
---------------------

local mainMod = "SUPER"

-- Core System & App Binds (Windows + Mac Hybrid Ergonomics)
hl.bind(mainMod .. " + Q",      hl.dsp.window.close())
hl.bind("ALT + F4",             hl.dsp.window.close())
hl.bind("ALT + Tab",            hl.dsp.exec_cmd("pkill rofi || rofi -show window -p '⇄ ОКНА / ALT+TAB' -theme ~/.config/rofi/kortex-start.rasi"))
hl.bind("CTRL + SHIFT + Escape",hl.dsp.exec_cmd("kitty --class kortex-taskmgr --title 'Task Manager (btop)' -e btop"))
hl.bind("CTRL + ALT + Delete",  hl.dsp.exec_cmd("kitty --class kortex-taskmgr --title 'Task Manager (btop)' -e btop"))
hl.bind(mainMod .. " + F",      hl.dsp.window.fullscreen({ action = "toggle" }))
hl.bind(mainMod .. " + V",      hl.dsp.window.float({ action = "toggle" }))
hl.bind(mainMod .. " + Return", hl.dsp.exec_cmd("/usr/local/bin/kortex-launch kitty"))
hl.bind(mainMod .. " + Space",  hl.dsp.exec_cmd("pkill rofi || /usr/local/bin/kortex-spotlight"))
hl.bind(mainMod .. " + R",      hl.dsp.exec_cmd("pkill rofi || /usr/local/bin/kortex-spotlight"))
hl.bind(mainMod .. " + C",      hl.dsp.exec_cmd("pkill rofi || /usr/local/bin/kortex-control-center"))
hl.bind(mainMod .. " + X",      hl.dsp.exec_cmd("pkill rofi || /usr/local/bin/kortex-control-center"))
hl.bind(mainMod .. " + D",      hl.dsp.exec_cmd("pkill rofi || /usr/local/bin/kortex-menu"))
hl.bind(mainMod .. " + Tab",    hl.dsp.exec_cmd("/usr/local/bin/kortex-layout next"))
hl.bind(mainMod .. " + B",      hl.dsp.exec_cmd("/usr/local/bin/kortex-launch firefox || /usr/local/bin/kortex-launch chromium || kitty"))
hl.bind(mainMod .. " + E",      hl.dsp.exec_cmd("kitty --class kortex-files -e yazi"))
hl.bind(mainMod .. " + G",      hl.dsp.exec_cmd("/usr/local/bin/kortex-grid-init --force-grid"))
hl.bind(mainMod .. " + F1",     hl.dsp.exec_cmd("/usr/local/bin/kortex-help-hud"))
hl.bind(mainMod .. " + M",      hl.dsp.exec_cmd("/usr/local/bin/kortex-open link"))

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
    hl.bind(mainMod .. " + " .. i,         hl.dsp.focus({ workspace = i }))
    hl.bind(mainMod .. " + SHIFT + " .. i, hl.dsp.window.move({ workspace = i }))
end

-- Mouse Bindings
hl.bind(mainMod .. " + mouse:272", hl.dsp.window.drag(),   { mouse = true })
hl.bind(mainMod .. " + mouse:273", hl.dsp.window.resize(), { mouse = true })

-- Media & Brightness Controls
hl.bind("XF86AudioRaiseVolume",  hl.dsp.exec_cmd("wpctl set-volume -l 1.5 @DEFAULT_AUDIO_SINK@ 5%+"), { locked = true, repeating = true })
hl.bind("XF86AudioLowerVolume",  hl.dsp.exec_cmd("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-"),        { locked = true, repeating = true })
hl.bind("XF86AudioMute",         hl.dsp.exec_cmd("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle"),       { locked = true })
hl.bind("XF86MonBrightnessUp",   hl.dsp.exec_cmd("brightnessctl set +10%"),                           { locked = true, repeating = true })
hl.bind("XF86MonBrightnessDown", hl.dsp.exec_cmd("brightnessctl set 10%-"),                           { locked = true, repeating = true })

-- Screenshots
hl.bind("PRINT",                   hl.dsp.exec_cmd("grim ~/screenshot_$(date +%s).png"))
hl.bind(mainMod .. " + PRINT",     hl.dsp.exec_cmd("grim ~/screenshot_$(date +%s).png"))
hl.bind(mainMod .. " + SHIFT + S", hl.dsp.exec_cmd("grim -g \"$(slurp)\" - | wl-copy"))

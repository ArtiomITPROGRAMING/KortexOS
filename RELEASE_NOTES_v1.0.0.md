# KortexOS v1.0.0 — Stable Release ("Unified Cyber-Deck")

We are proud to announce the first stable release of **KortexOS (v1.0.0)** — an ultra-responsive, highly customizable Linux operating system engineered on **Arch Linux**, the high-performance **Zen Kernel (`linux-zen`)**, and the next-generation **Hyprland Wayland Compositor**.

KortexOS bridges the gap between sci-fi aesthetics and everyday productivity, providing a cohesive experience for both keyboard-centric developers and mouse-oriented power users.

---

## 🌟 Key Highlights & Innovations

### 1. Unified Interface Philosophy Switcher (`kortex-layout`)
Switch between 3 distinct interface modes instantly via `Super + Tab` or the Waybar layout pill:
- **`Cyber-Deck (eDEX Grid)`**: Signature 5-module workstation (Telemetry Pulse, Interactive Shell, 3D Network Matrix, File Grid, Virtual Keyboard).
- **`MacBook Pro Mode (Glass & Dock)`**: Frosted glass floating windows with titlebar controls `[ _ ] [ □ ] [ X ]`, an island floating dock, and smooth touchpad gestures (`workspace_swipe = true`).
- **`Pure Tiling (Dev Mode)`**: Strict, distraction-free Hyprland dwindle tiling across all workspaces with zero padding.

### 2. Fullscreen First-Run OOBE Wizard (`kortex-oobe`)
- Interactive setup guiding language/keyboard selection (`EN`, `RU`, `RO`, `DE`), Wi-Fi/Bluetooth connections, interface philosophy, themes, and hardware power profiles.
- **One-Click Live Persistence Transfer**: Installing to disk (`kortex-install`) automatically copies all configured themes, wallpapers, and hotkeys directly to `/mnt/home/<user>/.config/`.

### 3. Layered Theme Studio Pro (`kortex-theme-apply` & `kortex-settings`)
- Fine-tune 7 distinct color layers: Base Background, Surface Layer, Primary Accent, Secondary Accent, Active Border Edge, Inactive Border, and Critical Alerts.
- 7 built-in high-contrast presets:
  - `Cyber Cyan` (#00f0ff — Tron Electric Glow)
  - `Tokyo Night` (#7aa2f7 — Indigo & Neon Lavender)
  - `Dracula` (#bd93f9 — Gothic Violet & Pink)
  - `Matrix Phosphor` (#00ff41 — Emerald Hacker Terminal)
  - `Amber CRT` (#ffb000 — 1980s Retro Phosphor)
  - `Mono Tron` (#ffffff — Stark High-Contrast Monochrome)
  - `Crimson Alert` (#ff003c — Tactical Combat HUD)
- Border effects: `Solid`, `Dual Gradient` (with 0–360° angle), `Animated Neon Loop`, and `Glow Shadow`.
- Atomic multi-process hot-reload: Hyprland, Waybar, Kitty, Rofi, and GTK-3/4 synchronized in under 3.5 seconds.

### 4. Per-App Wallpaper Engine (`kortex-wallpaper`)
- High-resolution bundled wallpapers (`cyber_grid.png`, `cyber_glass.png`, `pitch_black.png`) managed via `hyprpaper`/`swww`.
- Dedicated Kitty terminal background rendering with custom dimming/tint levels (`background_tint 0.0 - 0.95`).

### 5. Kortex Spotlight (`kortex-spotlight`)
- Bound to `Super + Space`.
- Global application launcher, file search, real-time command executor (`theme <name>`, `layout <name>`), and built-in safe math calculator (`sqrt(144)`, `42*8`, `(100+25)*4`).

### 6. Hardware Optimization & ZRAM
- Pre-configured `zram-generator` with `zstd` compressed swap, doubling effective memory headroom on 4GB/8GB systems.
- Power profile governor switching (`Balanced`, `Overdrive`, `Eco`).
- Fully automated offline live boot with pre-compiled Plymouth boot splash.

---

## 📦 Download & Verification

| Asset | Size | Description |
| :--- | :--- | :--- |
| `kortexos-v1.0.0-x86_64.iso` | ~2.0 GB | Standard bootable live ISO image (BIOS & UEFI) |
| `SHA256SUMS.txt` | 1 KB | SHA-256 verification hash |
| `SHA512SUMS.txt` | 1 KB | SHA-512 verification hash |

### Integrity Verification
```bash
# Verify SHA256 checksum
sha256sum -c SHA256SUMS.txt
```

---

## ⌨️ Essential Keyboard Shortcuts

| Shortcut | Action |
| :--- | :--- |
| `Super + Space` | **Kortex Spotlight** (Apps, Math, Quick Settings) |
| `Super + Tab` | **Cycle Layouts** (`Grid` ⇄ `MacBook` ⇄ `Tiling`) |
| `Super + Q` / `Alt + F4` | **Close Active Window** |
| `Super + Return` | Launch Terminal (Kitty) |
| `Super + D` | Kortex Start Menu (Rofi) |
| `Super + B` | Launch Web Browser |
| `Super + E` | Open File Explorer (Yazi) |
| `Super + F1` | System Keybinds Cheatsheet HUD |
| `Super + S` | Open Kortex Settings Studio Pro |
| `Super + Shift + S` | Screen Area Capture (Screenshot) |

---
*Created by the KortexOS Team. Powered by Arch Linux, Linux-Zen, and Hyprland.*

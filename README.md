# KortexOS 🌌
### The High-Performance Cyberpunk & Glassmorphism Linux Operating System

[![Version](https://img.shields.io/badge/version-1.0.0--stable-00f0ff.svg?style=for-the-badge)](https://github.com/ArtiomITPROGRAMING/KortexOS/releases)
[![Base](https://img.shields.io/badge/Arch%20Linux-Rolling-1793d1.svg?style=for-the-badge&logo=arch-linux)](https://archlinux.org)
[![Kernel](https://img.shields.io/badge/Kernel-Linux--Zen-ff003c.svg?style=for-the-badge&logo=linux)](https://github.com/zen-kernel/zen-kernel)
[![Compositor](https://img.shields.io/badge/Compositor-Hyprland%20Wayland-00ff41.svg?style=for-the-badge)](https://hyprland.org)
[![License](https://img.shields.io/badge/License-GPL--3.0-ffb000.svg?style=for-the-badge)](LICENSE)

---

## ⚡ Overview

**KortexOS** is an ultra-modern, rolling-release operating system built upon **Arch Linux**, the low-latency **Linux-Zen Kernel**, and the accelerated **Hyprland Wayland Compositor**. 

Designed for developers, cyber-security researchers, and everyday power users alike, KortexOS fuses the immersive aesthetics of a **cyberpunk cyber-deck** with the fluid, ergonomic polish of **macOS glassmorphism**.

```
       __ _____  ____ _____ _____ _  __  ____   _____
      / //_/ _ \/ __//_  _// __// // / / __ \ / ___/
     / ,< / // // _/   / / / _/ / _  / / /_/ /_\__ \ 
    /_/|_|\___//___/  /_/ /___//_//_/  \____//____/  
   >> UNIFIED DESIGN & PERSISTENCE ENGINE v1.0.0 <<
```

---

## 📸 Screenshots

| Cyber-Deck Grid (eDEX Station) | Kortex Settings Studio Pro |
| :---: | :---: |
| ![Cyber-Deck Desktop](docs/screenshots/desktop_cyberdeck.png) | ![Settings Studio](docs/screenshots/settings_studio.png) |

---

## 🔮 Three Unified Interface Philosophies

Switch between interface philosophies on the fly using **`Super + Tab`** or via the Waybar layout switcher:

1. **Cyber-Deck (eDEX Grid)**: A 5-pane modular cockpit designed for multi-tasking (Live CPU/RAM pulse, Interactive command shell, 3D network telemetry, File Explorer, and Virtual keyboard).
2. **MacBook Pro Mode (Glass & Dock)**: Rounded frosted-glass windows with interactive mouse controls `[ _ ] [ □ ] [ X ]`, an island dock, and 3-finger touchpad gestures.
3. **Pure Tiling (Dev Mode)**: Fullscreen dynamic bsp/dwindle tiling with zero distractions and instant window cycling.

---

## 🚀 Key Features

- **Fullscreen OOBE First-Run Wizard (`kortex-oobe`)**: Automatic first-boot wizard configuring languages (`EN`, `RU`, `RO`, `DE`), Wi-Fi/Bluetooth, display scaling, theme presets, and power profiles.
- **One-Click Live Persistence (`kortex-install`)**: Customizations configured in the Live ISO environment automatically transfer to the installed disk (`/mnt/home/<user>/.config/`).
- **Layered Theme Studio Pro (`kortex-settings`)**:
  - Independent 7-layer HEX color engine (Base, Surface, Primary Accent, Secondary Accent, Active Border, Inactive Border, Alerts).
  - 7 Built-in curated palettes: `Cyber Cyan`, `Tokyo Night`, `Dracula`, `Matrix Phosphor`, `Amber CRT`, `Mono Tron`, and `Crimson Alert`.
  - Border geometry engine: `Solid`, `Dual Gradient` (0–360°), `Animated Neon Loop`, and `Glow Shadow`.
  - Sub-4-second atomic hot-reload across Hyprland, Waybar, Kitty, Rofi, and GTK-3/4.
- **Per-App Wallpaper Engine (`kortex-wallpaper`)**: Independent high-res desktop wallpapers (`hyprpaper`/`swww`) and dimmable Kitty terminal backgrounds.
- **Kortex Spotlight (`kortex-spotlight`)**: Instant search and math calculator bound to `Super + Space`.
- **ZRAM Compressed Memory Engine**: Pre-configured `zstd` compressed RAM swap for smooth execution on 4GB and 8GB RAM machines.
- **Portable Profile Backups (`kortex-profile`)**: Export, import, and share your complete desktop setup as a portable `.kortex` bundle.

---

## 💻 Hardware Requirements

| Component | Minimum | Recommended |
| :--- | :--- | :--- |
| **CPU** | 64-bit x86-64 Dual-Core (1.8 GHz) | Quad-Core 2.5 GHz+ (Intel 8th+ Gen / AMD Ryzen) |
| **RAM** | 3.5 GB (with ZRAM enabled) | 8 GB+ DDR4 / DDR5 |
| **Storage** | 20 GB free disk space | 40 GB+ NVMe SSD |
| **GPU** | Intel HD Graphics / AMD Radeon / NVIDIA | Intel Iris Xe / AMD Radeon Vega/RDNA / modern GPU |
| **Display** | 1280 × 720 (720p) | 1920 × 1080 (1080p 60Hz/120Hz/144Hz) |

---

## 📥 Download Stable Release

Pre-compiled ISO images are available on the [GitHub Releases Page](https://github.com/ArtiomITPROGRAMING/KortexOS/releases):

- **Latest Stable ISO:** [`kortexos-v1.0.0-x86_64.iso`](https://github.com/ArtiomITPROGRAMING/KortexOS/releases/download/v1.0.0/kortexos-v1.0.0-x86_64.iso)
- **SHA-256 Checksums:** [`SHA256SUMS.txt`](https://github.com/ArtiomITPROGRAMING/KortexOS/releases/download/v1.0.0/SHA256SUMS.txt)
- **SHA-512 Checksums:** [`SHA512SUMS.txt`](https://github.com/ArtiomITPROGRAMING/KortexOS/releases/download/v1.0.0/SHA512SUMS.txt)

### Checksum Verification
```bash
# Verify integrity using SHA256:
sha256sum -c SHA256SUMS.txt
```

---

## 🛠️ Flashing & Installation

### Option 1: Using Ventoy (Recommended)
1. Install [Ventoy](https://www.ventoy.net) on a USB drive.
2. Drag and drop `kortexos-v1.0.0-x86_64.iso` onto the USB partition.
3. Reboot and select KortexOS.

### Option 2: Flashing via `dd` (Linux/macOS)
```bash
sudo dd if=kortexos-v1.0.0-x86_64.iso of=/dev/sdX bs=4M status=progress oflag=sync
```
*(Replace `/dev/sdX` with your USB drive identifier).*

### Option 3: Flashing via Rufus or BalenaEtcher (Windows)
1. Download [Rufus](https://rufus.ie) or [BalenaEtcher](https://etcher.balena.io).
2. Select `kortexos-v1.0.0-x86_64.iso` and your USB drive.
3. Flash using **DD Mode**.

---

## ⌨️ Hotkeys & Control Reference

| Shortcut | Description |
| :--- | :--- |
| `Super + Space` | **Kortex Spotlight** (Search apps, calculate, commands) |
| `Super + Tab` | **Cycle Layouts** (Cyber-Deck ⇄ MacBook ⇄ Tiling) |
| `Super + Q` / `Alt + F4` | **Close Active Window** |
| `Super + Return` | Launch Terminal (Kitty) |
| `Super + D` | Kortex Start Menu (Rofi) |
| `Super + B` | Launch Web Browser (Firefox) |
| `Super + E` | Open File Explorer (Yazi) |
| `Super + S` | Open Kortex Settings Studio Pro |
| `Super + F1` | System Keybinds Cheatsheet HUD |
| `Super + Shift + S` | Screen Area Capture (Screenshot) |
| `Super + L` | Lock Screen |

---

## 🏗️ Building from Source

To build your own custom KortexOS ISO using Docker on Linux or WSL2:

```bash
# Clone the repository
git clone https://github.com/ArtiomITPROGRAMING/KortexOS.git
cd KortexOS

# Build privileged Docker ArchISO image
./build.sh

# The finished ISO will be created in:
ls -lh out/kortexos-latest.iso
```

---

## 📄 License

KortexOS is distributed under the terms of the **GNU General Public License v3.0 (GPL-3.0)**. See [LICENSE](LICENSE) for details.

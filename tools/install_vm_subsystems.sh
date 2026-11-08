#!/bin/bash
set -e

echo "[*] Installing binaries..."
mv /tmp/kortex-settings /tmp/kortex-setting /tmp/kortex-ai /tmp/kortex-ai-daemon /tmp/kortex-install /usr/local/bin/
chmod +x /usr/local/bin/kortex-*

echo "[*] Installing Kortex AI systemd service..."
mv /tmp/kortex-ai.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable --now kortex-ai.service

echo "[*] Installing Plymouth theme..."
mkdir -p /usr/share/plymouth/themes /etc/plymouth
rm -rf /usr/share/plymouth/themes/kortex-tron
mv /tmp/kortex-tron /usr/share/plymouth/themes/
mv /tmp/plymouthd.conf /etc/plymouth/

plymouth-set-default-theme kortex-tron

echo "[*] Updating mkinitcpio hooks..."
echo "HOOKS=(base udev plymouth autodetect microcode modconf kms keyboard keymap consolefont block filesystems fsck)" > /etc/mkinitcpio.conf.d/kortex.conf

echo "[*] Updating GRUB cmdline..."
if [ -f /etc/default/grub ]; then
    sed -i 's/GRUB_CMDLINE_LINUX_DEFAULT=.*/GRUB_CMDLINE_LINUX_DEFAULT="quiet splash loglevel=3 rd.udev.log_level=3 vt.global_cursor_default=0 udev.log_priority=3"/' /etc/default/grub
    grub-mkconfig -o /boot/grub/grub.cfg
fi

echo "[*] Rebuilding initramfs..."
mkinitcpio -P

echo "[*] Updating desktop user configs..."
mkdir -p /home/kortex/.config/hypr /home/kortex/.config/waybar
cp /tmp/hyprland.conf /home/kortex/.config/hypr/hyprland.conf
cp /tmp/config /home/kortex/.config/waybar/config
chown -R 1000:1000 /home/kortex/.config

systemctl enable plymouth-start.service plymouth-quit.service 2>/dev/null || true
echo "[SUCCESS] Subsystems installed in VM!"

# dotfiles and config

In this guide im gonna explain how to install my dotfiles and configuration for Qtile, the arch tiling window manager. If you follow this guide make sure you know a little bit of basic linux commands. Finally, you have to install a clean distro of arch linux by using the **[Arch Wiki](https://wiki.archlinux.org/index.php/Installation_guide)**.

# after arch installation

After the clean installation of arch, make sure you have internet. 

```bash
pacman -S networkmanager
systemctl enable NetworkManager
```

Now you can install a bootloader and test it "safely", this is how to do it on modern hardware, assuming you've mounted the efi partition on [/boot](https://wiki.archlinux.org/index.php/Installation_guide#Example_layouts):

```bash
pacman -S grub efibootmgr os-prober
grub-install --target=x86_64-efi --efi-directory=/boot
os-prober
grub-mkconfig -o /boot/grub/grub.cfg
```

Now create a user:

```bash
useradd -m username
passwd username
usermod -aG wheel,video,audio,storage username
```

To have root privileges we need sudo:

```bash
pacman -S sudo
```

Edit /etc/sudoers with nano or vim by uncommenting this line:

```bash
## Uncomment to allow members of group wheel to execute any command
# %wheel ALL=(ALL) ALL
```

Now you can reboot:

```bash
exit
umount -R /mnt
reboot
```

After loggin in, you may have working internet if your computer is plugged in. If your can't connect to an ethernet cable you need the NetworkManager that we installed before.

```bash
# List all available networks
nmcli device wifi list
# Connect to your network
nmcli device wifi connect YOUR_SSID password YOUR_PASSWORD
```

# Installing the window manager

First, we're gonna install some usefull programs like a browser and a terminal so let's first install **[lighdm](https://wiki.archlinux.org/index.php/LightDM)**
and **[qtile](https://wiki.archlinux.org/index.php/Qtile)**. Lightdm will not
work unless we install a **[greeter](https://wiki.archlinux.org/index.php/LightDM#Greeter)**.
We also need
**[xterm](https://wiki.archlinux.org/index.php/Xterm)** because that's the
terminal emulator qtile will open by default, until we change the config file.
Then, a text editor is necessary for editing config files, you can use
**[vscode](https://wiki.archlinux.org/index.php/Visual_Studio_Code)** or jump
straight into **[neovim](https://wiki.archlinux.org/index.php/Neovim)** if you
have previous experience, otherwise I wouldn't suggest it. Last but not least,
we need a browser.

```bash
sudo pacman -S lightdm lightdm-gtk-greeter qtile xterm code firefox
```

Enable *lightdm* service and restart your computer, you should be able to log into
Qtile through *lightdm*.

```bash
sudo systemctl enable lightdm
reboot
```

# Basic qtile configuration

Now that you are in qtile, you have to know some of the default keybindings.

**mod + return**   | launch xterm               
**mod + k**        | next window                
**mod + j**        | previous window            
**mod + w**        | kill window                
**mod + [1]**     | go to workspace [1] 
**mod + ctrl + r** | restart qtile              
**mod + ctrl + q** | logout                     


# Dotfiles and config

In this guide im gonna explain how to install my dotfiles and configuration for Qtile, the arch tiling window manager. If you follow this guide make sure you know a little bit of basic linux commands. Finally, you have to install a clean distro of arch linux by using the **[Arch Wiki](https://wiki.archlinux.org/index.php/Installation_guide)**.

# After arch installation

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
**mod + [1]**      | go to workspace [1] 
**mod + ctrl + r** | restart qtile              
**mod + ctrl + q** | logout                     

You may need to change the keybord layout using the *setxkbmap*, for example if you have it in spanish: (open a terminal using **mod + return**)

```bash
setxkbmap es
```

Note that this change is not permanent, if you reboot you have to type that
command again. See [this section](#xprofile) for making it permanent, or
follow the natural order of this guide if you have enough time.

You may see there's not a menu by default, so you have to launch programs using *xterm*. At this point, you can pick your terminal emulator of choice and install a program launcher.

```bash
# Install another terminal emulator if you want
sudo pacman -S alacritty
```

Open the config file:

```python
code ~/.config/qtile/config.py
```

Now let's install a program laucher like **[rofi](https://wiki.archlinux.org/index.php/Rofi)**:

```bash
sudo pacman -S rofi
```

Then add keybindings for that program:

```python
Key([mod], "r", lazy.spawn("rofi -show run")),
Key([mod, 'shift'], "r", lazy.spawn("rofi -show")),
```

Now restart Qtile with **mod + control + r**. You should be able to open your
menu and terminal emulator with keybindings. If you picked rofi, you can
change its theme like so:

```bash
sudo pacman -S which
rofi-theme-selector
```

Now you can start editing the config file and make it your own.
Checkout my custom Qtile config
[here](https://github.com/tryiing/dotfiles/tree/master/.config/qtile).
But before that I would recommend configuring basic utilities like audio,
battery, mounting drives, etc.

# Basic system utilities

Let's install all you need to have a usefull system, configurating audio, wallpaper, network, storage, etc.

## All the programs

Install all of this programs for all tje usefull tools:

```bash
sudo pacman -S nitrogen pulseaudio pavucontrol volumeicon udiskie ntfs-3g scrot redshift libnotify notification-daemon ranger geeqie vlc ttf-dejavu ttf-liberation noto-fonts xorg-xinit arandr
```

Nitrogen - Wallpaper
Pulseaudio - Audio
Pavucontrol - Audio graphical interface 
Volumeicon - Audio icon
Udiskie - Mount external disks
Ntfs-3g - Mount ntfs formated external disks
Scrot - Screenshot
Redshift - Take care of your eyes 
Libnotify - Notifications
Notification-daemon - Icon notifications
Ranger - Terminal file manager
Geeqie - Image
Vlc - Video
Ttf-dejavu ttf-liberation noto-fonts - Default fonts
Xorg-xinit - Xprofile config
Arandr - Monitors

## Fonts

To list all available fonts:

```bash
fc-list
```

## Wallpaper

Use nitrogen to personalize your wallpaper.

```bash
# Create a file to save your wallpapers
mkdir ~/Wallpapers
# Dowload your wallpaper and use it like this:
nitrogen /Wallpapers
# Select your's
```

## Audio

There is no audio at this point, we need
**[pulseaudio](https://wiki.archlinux.org/index.php/PulseAudio)**.
I suggest also installing a graphical program to control audio like
**[pavucontrol](https://www.archlinux.org/packages/extra/x86_64/pavucontrol/)**,
because we don't have keybindings for that yet:

On Arch,
[pulseaudio is enabled by default](https://wiki.archlinux.org/index.php/PulseAudio#Running),
but you might need to reboot in order for it to actually start. After rebooting,
you can open *pavucontrol* through *rofi*, unmute the audio, and you should be
just fine.

Now you can set up keybindings for *pulseaudio*, open Qtile's config.py and add
these keys:

```python
# Volume
Key([], "XF86AudioLowerVolume", lazy.spawn(
    "pactl set-sink-volume @DEFAULT_SINK@ -5%"
)),
Key([], "XF86AudioRaiseVolume", lazy.spawn(
    "pactl set-sink-volume @DEFAULT_SINK@ +5%"
)),
Key([], "XF86AudioMute", lazy.spawn(
    "pactl set-sink-mute @DEFAULT_SINK@ toggle"
)),
```

## Storage

Another basic utility you might need is automounting external hard drives or
USBs. For that I use **[udisks](https://wiki.archlinux.org/index.php/Udisks)**
and **[udiskie](https://www.archlinux.org/packages/community/any/udiskie/)**.
*udisks* is a dependency of *udiskie*, so we only need to install the last one.
Install also **[ntfs-3g](https://wiki.archlinux.org/index.php/NTFS-3G)**
package to read and write NTFS formated drives.

## Network

I use 
**[nm-applet](https://wiki.archlinux.org/index.php/NetworkManager#nm-applet)**, to make sure i have internet.

## Notifications

I like having desktop notifications as well, for that you need to install
[**libnotify**](https://wiki.archlinux.org/index.php/Desktop_notifications#Libnotify)
and [**notification-daemon**](https://www.archlinux.org/packages/community/x86_64/notification-daemon/):

For a tiling window manager,
[this is how you can get notifications](https://wiki.archlinux.org/index.php/Desktop_notifications#Standalone):

```bash
# Create this file with nano or vim
sudo nano /usr/share/dbus-1/services/org.freedesktop.Notifications.service
# Paste these lines
[D-BUS Service]
Name=org.freedesktop.Notifications
Exec=/usr/lib/notification-daemon-1.0/notification-daemon
```

Test it like so:

```bash
notify-send "Hello World"
```

## Monitors

If you have a multi-monitor system, you surely want to use all your screens.
Here's how **[xrandr](https://wiki.archlinux.org/index.php/Xrandr)** CLI works:

```bash
# List all available outputs and resolutions
xrandr
# Common setup for a laptop and a monitor
xrandr --output eDP-1 --primary --mode 1920x1080 --pos 0x1080 --output HDMI-1 --mode 1920x1080 --pos 0x0
```

We need to specify the position for each output, otherwise it will default to
0x0, and all your outputs will be overlapped. Now if you don't want to calculate pixels
and stuff you need a GUI like
**[arandr](https://www.archlinux.org/packages/community/any/arandr/)**:

Open it with *rofi*, arrange your screens however you want, and then you can
save that layout, which will basically give you a shell script with the exact
*xrandr* command that you need. Save that script, but don't click "apply" just
yet.

For a multi-monitor system, it's recommended to create an instance of a
*Screen* object for each monitor in your Qtile config.

You'll find an array called *screens* which contains only one object
initialized with a bar at the bottom. Inside that bar you can see the default
widgets that come with it.

Add as many screens as you have and copy-paste all widgets, later you can
customize them. Now you can go back to arandr, click *apply*, and then restart
Qtile.

Now your multi-monitor system should work.

## Xprofile

As I have mentioned before, all these changes are not permanent. In order to
make them permanent, we need a couple things. First, install
**[xinit](https://wiki.archlinux.org/index.php/Xinit)**:

Now you can use *~/.xprofile* to run programs before your window manager starts:

```bash
touch ~/.xprofile
```

For example, if you place this in *~.xprofile*:

```bash
# Env vars
export PATH=$HOME/.local/bin:$PATH
export _JAVA_AWT_WM_NONREPARENTING=1
export QT_STYLE_OVERRIDE=kvantum

# Screens
hdmi=`xrandr | grep ' connected' | grep 'HDMI' | awk '{print $1}'`

if [ "$hdmi" = "HDMI-1" ]; then
  xrandr --output eDP-1 --primary --mode 1366x768 --pos 276x1080 --output HDMI-1 --mode 1920x1080 --pos 0x0 &
else
  xrandr --output eDP-1 --primary --mode 1366x768 --pos 0x0 --rotate normal --output HDMI-1 --off --output DP-1 --off &
fi

# Automount Devices
udiskie -t &

# Network
nm-applet &

# Keyboard Layout
setxkbmap es &

# Wallpaper
nitrogen --restore &

# Audio
volumeicon &
```

Every time you login you will have all systray utilities, your keyboard layout
and monitors set.

# Further configuration and tools

## AUR helper

Now that you have some software that allows you tu use your computer without
losing your patience, it's time to do more interesting stuff. First, install an
**[AUR helper](https://wiki.archlinux.org/index.php/AUR_helpers)**, I use
**[yay](https://github.com/Jguer/yay)**:

```bash
sudo pacman -S base-devel git
cd /opt/
sudo git clone https://aur.archlinux.org/yay-git.git
sudo chown -R username:username yay-git/
cd yay-git
makepkg -si
```

With an *Arch User Repository helper*, you can basically install
any piece of software on this planet that was meant to run on Linux.

## File Manager

We've done all files stuff through a terminal up to this point, but you can
install graphical or terminal based file managers.
For a graphical one, I suggest
**[thunar](https://wiki.archlinux.org/index.php/Thunar)**
and for a terminal based one,
**[ranger](https://wiki.archlinux.org/index.php/Ranger)**, although this one
is very vim-like, only use it if you know how to move in vim.

```bash
sudo pacman -S thunar ranger
```

## Trash

If you don't want to *rm* all the time and potentially lose files, you need a
trashing system. Luckily, that's pretty easy to do, using
[some of these tools](https://wiki.archlinux.org/index.php/Trash_management#Trash_creation)
such as **[glib2](https://www.archlinux.org/packages/core/x86_64/glib2/)**,
and for GUIs like *thunar* you need **[gvfs](https://www.archlinux.org/packages/extra/x86_64/gvfs/)**:

```bash
sudo pacman -S glib2 gvfs
# CLI usage
gio trash path/to/file
# Empty trash
gio trash --empty
```

With *thunar* you can open the trash clicking on the left panel, but on the command
line you can use:

```bash
ls ~/.local/share/Trash/files
```

## Windows

| Key                     | Action                           |
| ----------------------- | -------------------------------- |
| **mod + j**             | next window (down)               |
| **mod + k**             | next window (up)                 |
| **mod + shift + h**     | decrease master                  |
| **mod + shift + l**     | increase master                  |
| **mod + shift + j**     | move window down                 |
| **mod + shift + k**     | move window up                   |
| **mod + shift + f**     | toggle floating                  |
| **mod + tab**           | change layout                    |
| **mod + [1-9]**         | Switch to workspace N (1-9)      |
| **mod + shift + [1-9]** | Send Window to workspace N (1-9) |
| **mod + period**        | Focus next monitor               |
| **mod + comma**         | Focus previous monitor           |
| **mod + w**             | kill window                      |
| **mod + ctrl + r**      | restart qtile                    |
| **mod + ctrl + q**      | quit                             |

The following keybindings will only work if you install all programs needed:

```bash
sudo pacman -S rofi thunar firefox alacritty redshift scrot
```

To set up *rofi*,
[check this README](https://github.com/antoniosarosi/dotfiles/tree/master/.config/rofi),
and for *alacritty*, [this one](https://github.com/antoniosarosi/dotfiles/tree/master/.config/alacritty).


## Apps

| Key                 | Action                        |
| ------------------- | ----------------------------- |
| **mod + r**         | launch rofi                   |
| **mod + shift + r** | window nav (rofi)             |
| **mod + b**         | launch browser (firefox)      |
| **mod + return**    | launch terminal (alacritty)   |
| **mod + r**         | redshift                      |
| **mod + shift + r** | stop redshift                 |
| **mod + s**         | screenshot (scrot)            |
| **mod + i**         | photos (geeqie)               |
| **mod + v**         | video (vlc)                   |
| **mod + d**         | discord                       |
| **mod + g**         | minecraft (gdlauncher)        |

I don't use thunar and the trash in my actual arch, it's just to say that I don't have thouse in my config.

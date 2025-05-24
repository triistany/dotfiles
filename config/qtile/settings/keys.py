from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "s", lazy.layout.down()),
    ([mod], "w", lazy.layout.up()),
    ([mod], "a", lazy.layout.left()),
    ([mod], "d", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "control"], "w", lazy.layout.grow()),
    ([mod, "control"], "s", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "s", lazy.layout.shuffle_down()),
    ([mod, "shift"], "w", lazy.layout.shuffle_up()),
    ([mod, "shift"], "d", lazy.layout.shuffle_right()),
    ([mod, "shift"], "a", lazy.layout.shuffle_left()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "q", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    # ([mod], "r", lazy.spawncmd()),


    # ------------ App Configs ------------

    # Menu
    ([mod], "n", lazy.spawn("rofi -show drun")),

    # Window Nav
    ([mod, "shift"], "n", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "b", lazy.spawn("firefox")),

    # File Explorer
    ([mod], "e", lazy.spawn("pcmanfm")),

    # Terminal
    ([mod], "Return", lazy.spawn("kitty")),

    # Music
    ([mod], "m", lazy.spawn("spotify")),

    # Minecraft
    ([mod], "g", lazy.spawn("./home/tristany/.GDLauncher/GDLauncher__2.0.24__linux__x64.AppImage")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 4500")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    ([mod, "shift"], "s", lazy.spawn("scrot 'screenshot_%Y-%m-%d-%T_$wx$h.png' -e 'mkdir -p ~/images/screenshots/ | mv $f ~/images/screenshots/'")),
    ([mod, "control"], "s", lazy.spawn("scrot -s")),


    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]

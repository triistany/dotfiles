from libqtile.config import Key, Group
from libqtile.lazy import lazy
from .keys import mod, keys

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

groups = [Group(" 󰈹  ", layout='tile'),
          Group("   ", layout='tile'),
          Group(" 󰨞  ", layout='tile'),
          Group("   ", layout='tile'),
          Group(" 󰢷  ", layout='tile'),
          Group("   ", layout='tile')]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

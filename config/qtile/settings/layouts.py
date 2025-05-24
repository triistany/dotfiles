from libqtile import layout
from libqtile.config import Match
from .theme import colors

layout_conf = {
    'border_focus': colors['color4'][0],
    'border_width': 2,
    'border_normal': colors['dark'][0],
    'margin': 4,
}

layouts = [
    layout.Tile(**layout_conf),
    layout.Max(**layout_conf),
    layout.RatioTile(**layout_conf),
    
    # layout.MonadTall(**layout_conf),
    # layout.Matrix(columns=2, **layout_conf),
    # layout.MonadWide(**layout_conf),
    # layout.Bsp(**layout_conf),
    # layout.Columns(**layout_conf),
    # layout.TreeTab(**layout_conf),
    # layout.VerticalTile(**layout_conf),
    # layout.Zoomy(**layout_conf),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    border_focus=colors["color4"][0]
)

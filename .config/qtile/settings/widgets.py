# Qtile widgets for the bar

from libqtile import widget
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)


# ---------------- Functions ---------------

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(bg='dark', fg='dark'), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=0
    )


# --------------- Workspaces ---------------

def workspaces(): 
    return [
        
        widget.GroupBox(
            **base(bg='trans'),
            font='UbuntuMono Nerd Font',
            fontsize=22,
            margin_y=3,
            padding_y=8,
            padding_x=5,
            borderwidth=0,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=True,
            highlight_color=colors['grey'],
            highlight_method='block',
            this_current_screen_border=colors['focus'],
        ),
        
        widget.WindowName(**base(bg='trans',fg='hola'), fontsize=14, padding=3),
        
    ]


# ------------- Widgets Config -------------

primary_widgets = [
    *workspaces(),

    

    powerline('color5', 'dark'),

    # Updates
    icon(bg="color5", text=' '), # Icon: nf-fa-download
    widget.CheckUpdates( 
        background=colors['color5'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    # Update using $ sudo pacman -Syu
    ),

    powerline('color4', 'color5'),

    # CPU (% usage)
    icon(bg="color4",text='  '),  # Icon: nf-oct-cpu
    widget.CPU(**base(bg='color4'), padding=0),

    powerline('color3','color4'),

    # Ram (memory usage)
    widget.TextBox(**base(bg='color3'), text='󰘚 '),
    widget.Memory(
        **base(bg='color3'),
        format = '{MemUsed:.2f}/16',
        measure_mem = 'G',
        measure_swap = 'G',
    ),

    powerline('color2', 'color3'),

    # Layout
    widget.CurrentLayout(**base(bg='color2'), padding=3),
    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    powerline('color1', 'color2'),

    # Clock + Date + Hour
    icon(bg="color1", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock
    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),
    
    powerline('dark', 'color1'),

    widget.Systray(background=colors['dark'], padding=5),
    icon(bg='dark', text=' '),
]


# -------- Widgets on other Screens --------

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    # Layout
    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),
    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),
    
    # Date
    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 16,
    'padding': 0,
}
extension_defaults = widget_defaults.copy()

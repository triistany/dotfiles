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
    return widget.Sep(
        **base(), 
        linewidth=0, 
        padding=0
    )

def icon(fg='text', bg='dark', fontsize=18, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=0
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="",
        fontsize=45,
        padding=1
    )


def workspaces(): 
    return [
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=24,
            margin_y=2,
            margin_x=10,
            padding_y=8,
            padding_x=0,
            borderwidth=5,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=True,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['dark'],
            this_current_screen_border=colors['current_screen'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        widget.WindowName(**base(fg='dark'), fontsize=0),
    ]


primary_widgets = [

    powerline('dark', 'dark'),

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
    ),

    powerline('color4', 'color5'),


    # CPU (% usage)
    icon(bg="color4",text='  '),  # Icon: nf-oct-cpu
    widget.CPU(**base(bg='color4'), padding=0),

    powerline('color3','color4'),


    # Ram (memory usage)
    widget.TextBox(**base(bg='color3'), fontsize=18, text='󰘚 '),
    widget.Memory(
        **base(bg='color3'),
        format = '{MemUsed:.2f}/32',
        measure_mem = 'G',
        measure_swap = 'G',
    ),

    powerline('color2', 'color3'),

   
    # Layout
    widget.CurrentLayout(**base(bg='color2'), padding=5),
    widget.CurrentLayoutIcon(**base(bg='color2', fg='dark'), scale=0.75),

    powerline('color1', 'color2'),


    # Time
    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),
    icon(bg="color1", fontsize=18, text=' '), # Icon: nf-mdi-calendar_clock

    powerline('color0', 'color1'),
    
    widget.Battery(**base(bg='color0'),
        fontsize=18,
        format='{char} {percent:2.0%}',
        notify_below=20,
        low_percentage=0.2,
        low_foreground='#ff0000',
        full_char=' 󱐋',
        charge_char=' ',
        discharge_char=' 󰁾',
        empty_char=' ',
        update_interval=15,
    ),

    powerline('dark', 'color0'),

    widget.Systray(background=colors['dark'], padding=5),

    powerline('dark', 'dark'),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.75),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 16,
    'padding': 0,
}
extension_defaults = widget_defaults.copy()

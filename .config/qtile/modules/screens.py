from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0, background="#2f343f"),
                widget.TextBox(
                    text='',
                    fontsize=28,
                    padding=0,
                    foreground="#fb0067",
                    background="#2f343f",
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn('rofi -show drun')
                        }),
                    widget.Sep(padding=0, linewidth=0, background="#2f343f"), 
                widget.GroupBox(
                                highlight_method='block',
                                this_screen_border="#fb0067",
                                this_current_screen_border="#fb0067",
                                active="#ffffff",
                                inactive="#848e96",
                                background="#2f343f",
                                disable_drag=True),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 30, 
                       foreground='#2f343f'
                       ),    
                widget.Prompt(),
                widget.Spacer(length=50),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    scale=0.75,
                    foreground="#fb0067"
                    ),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_yay",
                    display_format="{updates} Updates",
                    foreground="#ffffff",
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')
                    },
                    background="#2f343f"),
                widget.Systray(icon_size = 20),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#2f343f'
                       ), 
                volume,
                widget.TextBox(                                                                    
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#2f343f',
                       ),   
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#2f343f'
                       ),    
                widget.Clock(format=' %Y-%m-%d %a %I:%M %p',
                             background="#2f343f",
                             foreground='#9bd689'),
                                                widget.TextBox(                                                
                                                
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#2f343f',
                       ),   
                widget.TextBox(
                    text='',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground='#e39378'
                )
                
            ],
            30,  # height in px
            background="#404552"  # background color
        ), ),
]

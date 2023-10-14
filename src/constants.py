import pygame_menu

FPS = 30
LIGHT_BLUE = (16, 109, 191)
FONT = pygame_menu.font.FONT_OPEN_SANS

W_WIDTH_SIZE = 800
W_HEIGHT_SIZE = 448

CUSTOME_THEME = pygame_menu.Theme(
    background_color=(255, 255, 255),
    selection_color=LIGHT_BLUE,
    title_background_color=LIGHT_BLUE,
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_ADAPTIVE,
    title_font=FONT,
    title_font_antialias=True,
    title_font_color =(255,255,255),
    title_font_size=44,
    widget_font=FONT,
    widget_font_size=32,
    widget_margin=(0,8),
    widget_cursor=pygame_menu.locals.CURSOR_HAND,)
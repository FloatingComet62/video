from pyglet import *

from equation_renderer import EquationRenderer

BUILD = False
LAST_FRAME = None

window = window.Window()
er = EquationRenderer(window, [
    "y=mx+c",
    "y-c=mx",
    "\\frac{y-c}{m}=x"
])
gray_scale = 50/255
gl.glClearColor(gray_scale, gray_scale, gray_scale, 1)
i = 0


@window.event
def on_draw():
    global i
    if LAST_FRAME and i == LAST_FRAME:
        window.close()
        return
    window.clear()

    # Render after this
    i += 1
    er.draw()
    if BUILD:
        image.get_buffer_manager().get_color_buffer().save(f"frames/{i:>06}.png")


app.run()

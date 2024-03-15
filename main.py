from pyglet import *

from equation_renderer import EquationRenderer

BUILD = False
LAST_FRAME = None

window = window.Window()
EquationRenderer.is_pre_renderer = True
EquationRenderer.padding = 20
EquationRenderer.title_preserve = 80
er = EquationRenderer(window, [
    "y=mx+c",
    "y-c=mx",
    "\\frac{y-c}{m}=x",
    "\\frac{y-c_1}{m}=x",
    "y=mx+c",
    "y-c=mx",
    "\\frac{y-c}{m}=x",
    "\\frac{y-c_1}{m}=x",
    "y=mx+c",
    "y-c=mx",
    "\\frac{y-c}{m}=x",
    "\\frac{y-c_1}{m}=x",
])
gray_scale = 50/255
gl.glClearColor(gray_scale, gray_scale, gray_scale, 1)
s = shapes.Rectangle(window.width//2 - 1, window.height//2 - 1, 2, 2, (255, 0, 0, 255))
i = 0


@window.event
def on_draw():
    global i
    if LAST_FRAME and i == LAST_FRAME:
        window.close()
        return
    window.clear()

    # Render after this
    if i and i % 100 == 0:
        er.pop_first_eqn()
    i += 1
    er.draw()
    s.draw()
    if BUILD:
        image.get_buffer_manager().get_color_buffer().save(f"frames/{i:>06}.png")


app.run()

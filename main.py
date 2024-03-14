from sympy import preview
from pyglet import *
from numpy import sin, cos
options = ['-D', '240', '-bg', 'Transparent', '-fg', 'rgb 1 1 1']
BUILD = True
LAST_FRAME = 350

window = window.Window()
preview("""
$$\\pi = \\int_{-\\infty}^{\\infty}\\frac{1}{1+x^2}dx$$
""", viewer='file', filename='output.png', dvioptions=options)
gray_scale = 50/255
gl.glClearColor(gray_scale, gray_scale, gray_scale, 1)
batch = graphics.Batch()
img = resource.image('output.png')
i = 0
r = 100
k = 10
sprite = sprite.Sprite(
    img,
    window.width//2-img.width//2 + r*sin(i/k),
    window.height//2-img.height//2 + r*cos(i/k),
    batch=batch
)


@window.event
def on_draw():
    global i
    if i == LAST_FRAME:
        window.close()
        return
    sprite.update(
        window.width//2-img.width//2 + r*sin(i/k),
        window.height//2-img.height//2 + r*cos(i/k),
    )
    window.clear()
    batch.draw()
    i += 1
    if BUILD:
        image.get_buffer_manager().get_color_buffer().save(f"frames/{i:>06}.png")


app.run()

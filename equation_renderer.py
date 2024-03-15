from sympy import preview
from pyglet import resource, graphics, sprite

options = ['-D', '240', '-bg', 'Transparent', '-fg', 'rgb 1 1 1']
renderer_already_created = False


def figure_out_resolution(num_of_equations):
    try:
        if num_of_equations <= 0:
            raise IndexError
        return ['240', '200', '200'][num_of_equations - 1]
    except IndexError as _:
        return '100'


class EquationRenderer:
    def __init__(self, window, equations):
        global renderer_already_created
        global options

        if renderer_already_created:
            print("EquationRenderer will cause name conflicts")
            raise Exception
        renderer_already_created = True

        self.batch = graphics.Batch()
        self.sprites = []
        self.padding = 20
        images = []

        options[1] = figure_out_resolution(len(equations))

        for i, equation in enumerate(equations):
            preview(
                f"$${equation}$$",
                viewer='file',
                filename=f"equations/eqn_{i}.png",
                dvioptions=options
            )
        for i in range(len(equations)):
            images.append(resource.image(f"equations/eqn_{i}.png"))
        images.reverse()

        total_height = 0
        for image in images:
            total_height += image.height + self.padding

        current_height = 0
        for image in images:
            self.sprites.append(sprite.Sprite(
                image,
                window.width // 2 - image.width // 2,
                window.height // 2 - total_height // 2 + current_height,
                batch=self.batch
            ))
            current_height += image.height + self.padding

    def draw(self):
        self.batch.draw()

from sympy import preview
from pyglet import resource, graphics, sprite

options = ['-D', '240', '-bg', 'Transparent', '-fg', 'rgb 1 1 1']
renderer_already_created = False


class CometException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)


def figure_out_resolution(num_of_equations):
    try:
        if num_of_equations <= 0:
            raise IndexError
        return ['240', '200', '200'][num_of_equations - 1]
    except IndexError as _:
        return '180'


class EquationRenderer:
    is_pre_renderer = False
    padding = 20
    title_preserve = 80

    def __init__(self, window, equations):
        global renderer_already_created
        global options

        if renderer_already_created:
            raise CometException("EquationRenderer will cause name conflicts")
        renderer_already_created = True

        self.batch = graphics.Batch()
        self.sprites = []
        self.window = window
        images = []

        options[1] = figure_out_resolution(len(equations))

        if not self.is_pre_renderer:
            for i, equation in enumerate(equations):
                preview(
                    f"$${equation}$$",
                    viewer='file',
                    filename=f"equations/eqn_{i}.png",
                    dvioptions=options
                )
        try:
            for i in range(len(equations)):
                images.append(resource.image(f"equations/eqn_{i}.png"))
        except resource.ResourceNotFoundException:
            raise CometException(
                "Some Equation Renders are missing, please set the property \"is_pre_renderer\" to \"False\""
            )

        total_height = 0
        for image in images:
            total_height += image.height
        total_height += self.padding * (len(images) - 1)
        start_height = window.height // 2 + total_height // 2
        current_height = min(start_height, window.height - self.title_preserve)

        for image in images:
            self.sprites.append(sprite.Sprite(
                image,
                window.width // 2 - image.width // 2,
                current_height - image.height,
                batch=self.batch
            ))
            current_height -= image.height + self.padding

    def draw(self):
        self.batch.draw()

    def pop_first_eqn(self):
        if len(self.sprites) == 0:
            return
        self.sprites = self.sprites[1:]

        total_height = 0
        for s in self.sprites:
            total_height += s.height
        total_height += self.padding * (len(self.sprites) - 1)
        start_height = self.window.height // 2 + total_height // 2
        current_height = min(start_height, self.window.height - self.title_preserve)

        for s in self.sprites:
            s.update(
                self.window.width // 2 - s.width // 2,
                current_height - s.height,
            )
            current_height -= s.height + self.padding

import taichi as ti
from taichi.math import vec3


@ti.data_oriented
class Scene:
    def __init__(self, window, resolution):
        self.instance = window.get_canvas()
        self.resolution = resolution
        self.canvas = ti.Vector.field(3, ti.f32, resolution)
        self.background_color = vec3(1, 1, 1)

    def draw(self):
        self.rendering(self.background_color)
        self.instance.set_image(self.canvas)

    @ti.kernel
    def rendering(self, background_color: vec3):
        for i, j in self.canvas:
            u = i / self.resolution[0]
            v = j / self.resolution[1]
            self.canvas[i, j] = background_color

    def set_background(self, r, g, b):
        self.background_color = b
        print("background color:", self.background_color)

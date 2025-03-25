import random

import taichi as ti
from taichi.math import vec3

ti.init(arch=ti.gpu)


@ti.data_oriented
class Model:

    def __init__(self):
        self.rot = vec3(0, 0, 0)
        self.pos = vec3(0, 0, 0)
        self.scale = vec3(1, 1, 1)
        self.color = (0, 0, 0)
        self.radius = 0.1

    def create_cube(self, pos: vec3, rot: vec3, scale: vec3, color: vec3, precision: ti.i32):
        self.vert = ti.Vector.field(3, dtype=ti.f32, shape=precision * precision * precision)
        self.world_vert = ti.Vector.field(3, dtype=ti.f32, shape=precision * precision * precision)
        self.pos = pos
        self.rot = rot
        self.scale = scale
        self.color = (color.x, color.y, color.z)

        inv_pre = 0.2 / precision
        half_pre = (precision - 1) * 0.5

        flag = 0
        for i in range(precision):
            for j in range(precision):
                for k in range(precision):
                    self.vert[flag] = (vec3(i, j, k) - vec3(half_pre) + vec3(random.random())) * inv_pre
                    flag += 1

    @ti.func
    def test(self):
        pass



if __name__ == '__main__':

    q = Model()
    q.create_cube(
        pos = vec3(0, -1, 0),
        rot = vec3(0, -1, 0),
        scale = vec3(1, 1, 1),
        color = vec3(0, 0, 0.4),
        precision= 10
    )
    print(q.vert)
    window = ti.ui.Window("Taichi Cloth Simulation on GGUI", (1024, 1024),
                          vsync=True)
    canvas = window.get_canvas()
    canvas.set_background_color((1, 1, 1))
    scene = window.get_scene()
    camera = ti.ui.Camera()

    pass
    current_t = 0.0
    while window.running:
        q.update()
        camera.position(0.0, 0.0, 3)
        camera.lookat(0.0, 0.0, 0)
        scene.set_camera(camera)
        scene.point_light(pos=(0, 1, 2), color=(1, 1, 1))
        scene.ambient_light((0.5, 0.5, 0.5))

        scene.particles(
            q.vert,
            color=q.color,
            radius=0.01,
        )
        canvas.scene(scene)
        window.show()

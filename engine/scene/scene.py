import taichi as ti
from taichi.math import vec3

from engine.component.renderer.render_layer import RenderLayer


class Scene(RenderLayer):
    def __init__(self, window):
        super().__init__()
        self.instance = window.get_scene()

        self.window = window
        self.canvas = window.get_canvas()
        self.camera = ti.ui.Camera()

        self.ambient_power = (0, 0, 0)

        self.update_scene()

        self.center = ti.Vector.field(3, dtype=ti.f32, shape=(1,))
        self.center[0] = [0, 0, 0]
        self.radius = 0.5
        self.color = (0.2, 0.2, 0.2)

    def draw(self):
        self.instance.point_light(pos=(0, 1, 2), color=(1, 1, 1))
        self.instance.ambient_light(self.ambient_power)
        self.instance.particles(self.center, self.radius, self.color)
        super().draw()

    def set_camera_pos(self, x, y, z):
        self.camera.position(x, y, z)

    def set_camera_lookat(self, x, y, z):
        self.camera.lookat(x, y, z)
    def set_ambient(self, r, g, b):
        self.ambient_power = (r, g, b)

    def set_background(self, r, g, b):
        self.canvas.set_background_color((r, g, b))

    def _camera_control(self, window, speed, hold_keys):
        self.camera.track_user_inputs(window, movement_speed=speed, hold_key=hold_keys)

    def update_scene(self):
        tid = self.register(self._camera_control,self.window, 0.03, ti.ui.LMB)
        cid = self.register(self.instance.set_camera, self.camera)
        uid = self.register(self.canvas.scene, self.instance)
import numpy as np
import taichi as ti

from engine.component.renderer.render_layer import RenderLayer
from engine.physics.mpm_solver import MPMSolver


@ti.data_oriented
class Scene(RenderLayer):
    def __init__(self, window):
        super().__init__()
        self.instance = window.get_scene()

        self.window = window
        self.canvas = window.get_canvas()
        self.camera = ti.ui.Camera()

        self.mpm_solver = MPMSolver(res=(64, 64, 64), size=10, max_num_particles=2 ** 15, use_ggui=True)
        self.mpm_solver.add_cube(lower_corner=[2, 8, 3],
                     cube_size=[1, 1, 3],
                     material=MPMSolver.material_snow)
        self.mpm_solver.set_gravity((0, -50, 0))

        self.ambient_power = (0, 0, 0)

        self.update_scene()

    def draw(self):
        self.camera.track_user_inputs(self.window, movement_speed=0.03, hold_key=ti.ui.RMB)
        self.set_color(self.mpm_solver.color_with_alpha, material_type_colors, self.mpm_solver.material)
        self.instance.ambient_light(self.ambient_power)
        self.mpm_solver.step(4e-3)
        self.instance.particles(self.mpm_solver.x, per_vertex_color=self.mpm_solver.color_with_alpha, radius=0.03)

        super().draw()

    @ti.kernel
    def set_color(self, ti_color: ti.template(), material_color: ti.types.ndarray(), ti_material: ti.template()):
        for I in ti.grouped(ti_material):
            material_id = ti_material[I]
            color_4d = ti.Vector([0.0, 0.0, 0.0, 1.0])
            for d in ti.static(range(3)):
                color_4d[d] = material_color[material_id, d]
            ti_color[I] = color_4d

    def add_point_light(self, pos, color):
        return self.register(self._add_point_light, pos, color)

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

    def _add_point_light(self, pos, color):
        self.instance.point_light(pos=pos, color=color)

    def update_scene(self):
        tid = self.register(self._camera_control, self.window, 0.03, ti.ui.LMB)
        cid = self.register(self.instance.set_camera, self.camera)
        uid = self.register(self.canvas.scene, self.instance)


material_type_colors = np.array([
    [0.1, 0.1, 1.0, 0.8],
    [236.0 / 255.0, 84.0 / 255.0, 59.0 / 255.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 0.0, 1.0]
]
)

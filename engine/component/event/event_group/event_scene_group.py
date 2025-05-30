﻿from taichi.math import vec3

from engine.component.event.event_group.event_group_base import EventGroupBase
from engine.physics.mpm_solver import MPMSolver

class EventSceneGroup(EventGroupBase):
    def set_background_color(self, r, g, b):
        self.component.set_background(r, g, b)

    def set_camera_position(self, x, y, z):
        self.component.set_camera_pos(x, y, z)

    def set_camera_lookat(self, x, y, z):
        self.component.set_camera_lookat(x, y, z)
        
    def add_cube(self, lower_corner, size, physical_mat):
        print("add cube in event manager:", lower_corner, size, physical_mat)
        mat = MPMSolver.material_rigid
        if physical_mat.lower() in 'sand':
            mat = MPMSolver.material_sand
        if physical_mat.lower() in 'snow':
            mat = MPMSolver.material_snow
        if physical_mat.lower() in 'water':
            mat = MPMSolver.material_water
        if physical_mat.lower() in 'elastic':
            mat = MPMSolver.material_elastic
        self.component.register_once(self.component.add_cube, lower_corner, size, mat)
# self.register(self._add_point_light, pos, color)
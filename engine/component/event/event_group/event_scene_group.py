from taichi.math import vec3

from engine.component.event.event_group.event_group_base import EventGroupBase


class EventSceneGroup(EventGroupBase):
    def set_background_color(self, r, g, b):
        self.component.set_background(r, g, b)

    def set_camera_position(self, x, y, z):
        self.component.set_camera_pos(x, y, z)

    def set_camera_lookat(self, x, y, z):
        self.component.set_camera_lookat(x, y, z)
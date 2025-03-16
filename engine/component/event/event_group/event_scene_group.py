from taichi.math import vec3

from engine.component.event.event_group.event_group_base import EventGroupBase


class EventSceneGroup(EventGroupBase):
    def set_background_color(self, r, g, b):
        self.component.background_color = vec3(r, g, b)

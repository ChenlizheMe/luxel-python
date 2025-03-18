import taichi as ti
from taichi.math import vec3, vec4


@ti.dataclass
class Ray:
    origin: vec3
    direction: vec3
    color: vec4

    @ti.func
    def at(self, t: float) -> vec3:
        return self.origin + t * self.direction

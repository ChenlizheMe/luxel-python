import engine
import taichi as ti
from taichi.math import vec3

eg = engine.Engine(size=(1024, 1024), pos=(200, 150))

gui = eg.gui
s1, _ = gui.create_sub_window("My Sub Window", 0, 0, 0.3, 0.4)
t1 = gui[s1].add_text("Hello from inside sub window!")
t2 = gui[s1].add_button("Button inside sub window")
eg.scene.set_background(0.1, 0.1, 0.1)
eg.scene.set_camera_pos(0, 0, 4)
eg.scene.set_camera_lookat(0, 0, 0)
eg.run()

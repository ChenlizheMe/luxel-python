import engine
from engine.physics.mpm_solver import MPMSolver

eg = engine.Engine(size=(1024, 1024), pos=(200, 150))

gui = eg.gui
s1, _ = gui.create_sub_window("My Sub Window", 0, 0, 0.3, 0.4)
t1 = gui[s1].add_text("Hello from inside sub window!")

rigid_button = gui[s1].add_button("Add Test Rigid")
water_button = gui[s1].add_button("Add Test Water")
sand_button = gui[s1].add_button("Add Test Sand")
elastic_button = gui[s1].add_button("Add Test Elastic")
snow_button = gui[s1].add_button("Add Test Snow")

eg.scene.set_background(0.1, 0.1, 0.1)
eg.scene.set_camera_pos(4.389, 9.5, -9.5)
eg.scene.set_camera_lookat(4.25, 1.89, 1.7)
eg.scene.add_point_light((0, 1, 2), (1, 1, 1))

gui[s1].catch(rigid_button, eg.add_event, 'addcube', (0, 5, 0), (1, 1, 1), 'rigid')
gui[s1].catch(water_button, eg.add_event, 'addcube', (0, 5, 0), (1, 1, 1), 'water')
gui[s1].catch(sand_button, eg.add_event, 'addcube', (0, 5, 0), (1, 1, 1), 'sand')
gui[s1].catch(elastic_button, eg.add_event, 'addcube', (0, 5, 0), (1, 1, 1), 'elastic')
gui[s1].catch(snow_button, eg.add_event, 'addcube', (0, 5, 0), (1, 1, 1), 'snow')
eg.run()

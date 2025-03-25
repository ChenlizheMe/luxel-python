import engine

eg = engine.Engine(size=(1024, 1024), pos=(200, 150))

gui = eg.gui
s1, _ = gui.create_sub_window("My Sub Window", 0, 0, 0.3, 0.4)
t1 = gui[s1].add_text("Hello from inside sub window!")
t2 = gui[s1].add_button("Button inside sub window")

eg.scene.set_background(0.1, 0.1, 0.1)
eg.scene.set_camera_pos(4.389, 9.5, -9.5)
eg.scene.set_camera_lookat(4.25, 1.89, 1.7)
eg.scene.add_point_light((0, 1, 2), (1, 1, 1))

gui[s1].catch(t2, eg.add_event, 'setbackground', 0.5, 0.5, 0.5)
gui[s1].catch(t2, print, "success")
eg.run()

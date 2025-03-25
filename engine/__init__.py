from os import _exit

import taichi as ti

from engine.component.console import Console
from engine.component.event.event_mgr import EventMgr
from engine.core.threads_pool import ThreadPool
from engine.gui.gui import GUI
from engine.scene.scene import Scene
from engine.utils.log import Instance as log
from engine.physics.mpm_solver import MPMSolver

ti.init(arch=ti.cuda, device_memory_GB=4.0)


class Engine:
    def __init__(self, name="SceneManager", size=(512, 512), fps_limit=6000, pos=(512, 512)):
        import engine.utils.cleanup
        self.window = ti.ui.Window(name=name, res=size, fps_limit=fps_limit, pos=pos)

        # renderer
        self.scene = Scene(self.window)
        self.gui = GUI(self.window)

        # core
        self.threads_pool = ThreadPool()

        # service
        self.event_mgr = EventMgr(self)
        self.console_mgr = Console(self.event_mgr)

        # state
        self.mainloop = True

        self.services = {
            'user_console': self.threads_pool.register_continuous(self.user_console),
            'event_process': self.threads_pool.register_continuous(self.event_process)
        }

        self.start_core_service()

    def start_core_service(self):
        self.start_service('user_console')
        self.start_service('event_process')

    def run(self):
        self.mainloop = True
        while self.window.running and self.mainloop:
            self.scene.draw()
            self.gui.draw()
            self.window.show()

        _exit(0)

    def start_service(self, service):
        self.threads_pool.start(self.services[service])

    def stop_service(self, service):
        self.threads_pool.kill(self.services[service])

    def user_console(self):
        self.console_mgr.active()
        return self.window.running

    def add_event(self, event, *args):
        self.event_mgr.add_event(event, *args)

    def event_process(self):
        self.event_mgr.active()
        return self.window.running
import queue

from engine.component.event.event_group.event_engine_group import EventEngineGroup
from engine.component.event.event_group.event_scene_group import EventSceneGroup


class EventMgr:
    def __init__(self, engine):
        self.queue = queue.Queue()
        self.engine = engine

        self.event_group = {
            'engine' : EventEngineGroup(self.engine),
            'scene' : EventSceneGroup(self.engine.scene),
        }

        self.event_map = {
            'exit': self.event_group['engine'].exit,
            'setbackground': self.event_group['scene'].set_background_color,
        }

    def add_event(self, event, *args):
        self.queue.put({"event": event, "args": args})

    def active(self):
        active_event = self.queue.get()
        self.engine.threads_pool.start(
            self.engine.threads_pool.register_single(
                self.event_map[active_event["event"]],
                *active_event["args"]
            )
        )

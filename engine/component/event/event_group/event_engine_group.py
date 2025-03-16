from engine.component.event.event_group.event_group_base import EventGroupBase

class EventEngineGroup(EventGroupBase):
    def exit(self):
        self.component.mainloop = False
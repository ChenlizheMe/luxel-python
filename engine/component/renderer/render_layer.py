import uuid

class RenderLayer:
    def __init__(self):
        self.draw_list = {}  # 使用字典存储函数，键为唯一ID
        self.results = {}
        self.state = {}

    def draw(self):
        for uid, (func, args, kwargs) in list(self.draw_list.items()):
            new_value = func(*args, **kwargs)

            if self.results[uid] != 'this is a start':
                self.state[uid] = 1 if (new_value != self.results[uid] and self.state[uid] != 1) else 0
            self.results[uid] = new_value

    def catch(self, uid, func, *args):
        return self.register(self._catch, uid, func, *args)

    def _catch(self, uid, func, *args):
        if uid in self.state and self.state[uid] == 1:
            func(*args)

    def register(self, func, *args, **kwargs):
        """注册函数，使用 UUID 生成唯一标识，并返回 UID"""
        uid = str(uuid.uuid4())  # 生成 UUID
        self.results[uid] = 'this is a start'
        self.state[uid] = 0
        self.draw_list[uid] = (func, args, kwargs)
        return uid  # 返回 UID 以便后续移除

    def get(self, uid):
        return self.results[uid]

    def unregister(self, uid):
        """根据唯一ID移除函数"""
        if uid in self.draw_list:
            del self.draw_list[uid]
            del self.state[uid]


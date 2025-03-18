import uuid

class RenderLayer:
    def __init__(self):
        self.draw_list = {}  # 使用字典存储函数，键为唯一ID
        self.results = {}

    def draw(self):
        for uid, (func, args, kwargs) in list(self.draw_list.items()):
            self.results[uid] = func(*args, **kwargs)

    def register(self, func, *args, **kwargs):
        """注册函数，使用 UUID 生成唯一标识，并返回 UID"""
        uid = str(uuid.uuid4())  # 生成 UUID
        self.results[uid] = None
        self.draw_list[uid] = (func, args, kwargs)
        return uid  # 返回 UID 以便后续移除

    def get(self, uid):
        return self.results[uid]

    def unregister(self, uid):
        """根据唯一ID移除函数"""
        if uid in self.draw_list:
            del self.draw_list[uid]


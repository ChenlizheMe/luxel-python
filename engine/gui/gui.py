import uuid

from engine.component.renderer.render_layer import RenderLayer


class GUI(RenderLayer):
    def __init__(self, window):
        super().__init__()
        self.sub_windows = {}
        self.instance = window.get_gui()

    def __getitem__(self, item):
        return self.sub_windows[item]

    def create_sub_window(self, title, x=0, y=0, width=300, height=200):
        """
        只能在外层创建子窗口，返回一个 SubWindow 对象
        然后通过该对象的 add_xxx 接口向其中注册控件
        """
        sub_window_uid = str(uuid.uuid4())  # 生成 UUID
        s_window = SubWindow(self, title, x, y, width, height)
        sub_window_draw_id = self.register(s_window.draw_window)
        self.sub_windows[sub_window_uid] = s_window

        return sub_window_uid, sub_window_draw_id


class SubWindow(RenderLayer):
    def __init__(self, gui: GUI, title, x, y, width, height):
        super().__init__()
        self.gui = gui
        self.title = title
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw_window(self):
        with self.gui.instance.sub_window(self.title, self.x, self.y, self.width, self.height):
            self.draw()

    def add_text(self, text):
        return self.register(self.gui.instance.text, text)

    def add_button(self, label):
        return self.register(self.gui.instance.button, label)

    def add_slider_float(self, label, value, minimum=0.0, maximum=100.0):
        return self.register(self.gui.instance.slider_float, label, value, minimum=minimum, maximum=maximum)

    def add_color_edit(self, label, color):
        return self.register(self.gui.instance.color_edit_3, label, color)

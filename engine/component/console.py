class Console:
    def __init__(self, event_mgr):
        self.event_mgr = event_mgr

    def active(self):
        user_input = input("Command: ")
        parts = user_input.split()  # 按空格分割输入
        if not parts:
            return

        command = parts[0]  # 提取命令部分
        if command == "setbackground":
            if len(parts) == 4:
                self.event_mgr.add_event(command, parts[0], parts[1], parts[2])
        if command == "exit":
            self.event_mgr.add_event(command)
class Console:
    def __init__(self, event_mgr):
        self.event_mgr = event_mgr

    def active(self):
        user_input = input("Command: ")
        parts = user_input.split()  # 按空格分割输入
        if not parts:
            return

        command = parts[0].lower()  # 提取命令部分
        if command in {"setbackground", "setcamerapos", "setcameralookat"}:
            if len(parts) == 4:
                self.event_mgr.add_event(command, float(parts[1]), float(parts[2]), float(parts[3]))
        if command in {"addcube"}:
            if len(parts) == 8:
                self.event_mgr.add_event(command, (int(parts[1]), int(parts[2]), int(parts[3])), (int(parts[4]), int(parts[5]), int(parts[6])), parts[7])
        if command == "exit":
            self.event_mgr.add_event(command)

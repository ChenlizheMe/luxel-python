import logging


class Logger:
    # 定义日志级别的颜色
    COLORS = {
        'DEBUG': '\033[94m',  # Blue
        'INFO': '\033[92m',  # Green
        'LOG': '\033[0m',  # Default
        'WARNING': '\033[93m',  # Yellow
        'ERROR': '\033[91m',  # Red
    }

    RESET = '\033[0m'

    LEVELS = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'LOG': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
    }

    def __init__(self, level='INFO'):
        """
        初始化日志系统，设置显示的最低日志级别。
        :param level: 设置日志级别，默认 'INFO'，可选 'DEBUG', 'INFO', 'LOG', 'WARNING', 'ERROR'
        """
        self.level = self.LEVELS.get(level.upper(), logging.INFO)

        # 创建控制台处理器
        ch = logging.StreamHandler()

        # 设置日志输出格式
        formatter = logging.Formatter('%(levelname)s - %(message)s')
        ch.setFormatter(formatter)

    def set_level(self, level):
        self.level = self.LEVELS.get(level.upper(), logging.INFO)

    def _log(self, level, msg):
        """
        内部方法：根据不同的日志级别来打印日志
        :param level: 日志级别
        :param msg: 日志内容
        """
        color = self.COLORS.get(level.upper(), self.COLORS['LOG'])
        reset = self.RESET

        print(f"{color}{level}: {msg}{reset}")

    def log(self, msg):
        if self.level <= logging.INFO:
            self._log('LOG', msg)

    def info(self, msg):
        if self.level <= logging.INFO:
            self._log('INFO', msg)

    def debug(self, msg):
        if self.level <= logging.DEBUG:
            self._log('DEBUG', msg)

    def warning(self, msg):
        if self.level <= logging.WARNING:
            self._log('WARNING', msg)

    def error(self, msg):
        if self.level <= logging.ERROR:
            self._log('ERROR', msg)

Instance = Logger()
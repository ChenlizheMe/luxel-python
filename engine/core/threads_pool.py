import engine
from threading import Thread
import uuid


class ThreadPool:
    def __init__(self):
        self.threads = {}
        self.stop_flags = []

    def register_single(self, task_func, *args):
        """
        注册一个单次执行的线程任务，并返回一个唯一的线程uid。
        :param task_func: 线程执行的函数
        :param args: 线程函数的参数
        :return: 线程的uid
        """
        id = str(uuid.uuid4())
        thread = Thread(target=self._run_single, args=(task_func, id) + args)
        self.threads[id] = thread

        engine.log.debug(f"add a new thread :{task_func.__name__} with uuid:{id}")

        return id

    def register_continuous(self, task_func, *args):
        """
        注册一个重复执行的线程任务，并返回一个唯一的线程uid
        :param task_func: 线程执行函数。task_func的返回值(T/F)会决定是否终止线程
        :param args: 线程函数的参数
        :return: 线程的uid
        """
        id = str(uuid.uuid4())
        # 同样处理 args
        thread = Thread(target=self._run_continuous, args=(task_func, id) + args)
        self.threads[id] = thread

        engine.log.debug(f"add a new thread :{task_func.__name__} with uuid:{id}")

        return id

    def _run_single(self, task_func, id, *args):
        """
        运行单次任务，执行完毕后注销线程。
        :param task_func: 线程执行的函数
        :param id: 线程的唯一id
        :param args: 线程函数的参数
        """
        task_func(*args)  # 使用 *args 来解包参数
        self.deregister(id)

    def _run_continuous(self, task_func, id, *args):
        """
        执行持续运行任务，直到满足终止条件才退出。
        :param task_func: 线程执行的函数
        :param id: 线程的唯一id
        :param args: 线程函数的参数
        """
        result = True
        while result:
            if id in self.stop_flags:
                break
            result = task_func(*args)  # 使用 *args 来解包参数
        self.deregister(id)

    def start(self, uid):
        """
        :param uid: 线程的唯一id
        """
        if uid in self.threads:
            thread = self.threads[uid]
            thread.start()
        else:
            engine.log.error(f"thread {uid} not registered")

    def paused(self, uid):
        """
        :param uid: 线程的唯一id
        """
        if uid in self.threads:
            self.threads[uid].pause()
        else:
            engine.log.warning(f"thread {uid} not registered")

    def kill(self, uid):
        self.stop_flags.append(uid)

    def deregister(self, uid):
        """
        注销一个线程。
        :param uid: 线程的唯一id
        """
        if uid in self.stop_flags:
            self.stop_flags.remove(uid)

        if uid in self.threads:
            del self.threads[uid]
            engine.log.debug(f"remove thread :{uid}")
        else:
            engine.log.warning(f"thread {uid} not registered")

# This is a file which run background check every 10 secs and inform if something happens

import threading, time

# Notification to make a notify call (probably depends on System used
class NotificationHandler:
    def notify(self, message):
        raise Exception("Notification not implemented - probably generic class")

class PrintLine(NotificationHandler):
    def notify(self, message):
        print message + '\n'

class LinuxNotify(NotificationHandler):
    def notify(self, message):
        import subprocess as sub
        sub.Popen(['notify-send', '-t', '2', message])

class Background:

    def __init__(self, predicate, sleep=10, notification_handler = PrintLine()):
        self._stop_event = threading.Event()
        self._background_thread = threading.Thread(target=self._loop, args=(self._stop_event,))
        self._predicate = predicate
        self._sleep = sleep
        self._notification_handler = notification_handler

    def start(self):
        self._background_thread.start()

    def join(self):
        self._background_thread.join()

    def stop(self):
        self._stop_event.set()

    def _notify(self, msg):
        self._notification_handler.notify(msg)

    def _loop(self, stop):
        while not stop.is_set():
            msg = self._predicate()
            if msg is not None:
                self._notify(msg)
            time.sleep(self._sleep)

# Testing
def true():
    return 'HYHYHY'

notifier = Background(predicate=true, notification_handler=LinuxNotify())
notifier.start()
input('Whatever')
notifier.stop()


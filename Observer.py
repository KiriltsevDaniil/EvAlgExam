# Additional classes to achieve more object-oriented way of Model-Presenter relationship


# Observer class for eponymous pattern
class Observer:
    def __init__(self):
        pass

    def update(self, message):
        pass


# Publisher class, needed for Observer pattern between SSWM and Presenter
class Publisher:
    def __init__(self, sub: Observer):
        self.subscriber = sub

    def notify(self, msg):
        self.subscriber.update(msg)

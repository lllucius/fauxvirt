from abc import ABC, abstractmethod

class Base(ABC):
    def __init__(self, kind):
        super(Base, self).__init__()

        self.kind = kind
        self.guid = None
        self.name = None
        self.description = ""
        self.comment = ""
        self.state = None



class Obj(object):
    def __init__(self, init = None):
        super(Obj, self).__init__()

        if init is not None:
            self.__dict__.update(init.items())


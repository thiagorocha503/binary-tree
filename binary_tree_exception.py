from builtins import Exception


class NodeTypeError(Exception):

    def __init__(self, value):
        self.value = value

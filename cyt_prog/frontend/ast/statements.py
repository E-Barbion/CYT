from .base import ASTNode

class Assign(ASTNode):
    def __init__(self, target, value):
        self.target = target
        self.value = value
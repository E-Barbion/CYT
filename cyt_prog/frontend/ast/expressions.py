from .base import ASTNode

class Name(ASTNode):
    def __init__(self, name: str):
        self.name = name


class IntLiteral(ASTNode):
    def __init__(self, ident: str):
        self.ident = ident
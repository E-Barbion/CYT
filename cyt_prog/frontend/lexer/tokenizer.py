from .tokens import Token
from .cursor import Cursor as c
from .cursor import TCursor as tc

def tokenizer(source: str):
    TOKEN_STREAM = []
    while not c.at_end():
        pass
    TOKEN_STREAM.append(Token.kind.EOF)
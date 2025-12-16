from dataclasses import dataclass
from enum import Enum, auto

class TokenKind(Enum):
    NAME = auto()
    EQUAL = auto()
    INT = auto()
    NEWLINE = auto()
    EOF = auto()

@dataclass
class Token:
    kind: TokenKind
    lexeme: str
    line: int
    col: int
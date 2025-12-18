from .tokens import Token
from .cursor import Cursor as c
from .cursor import TCursor as tc
import cyt_prog.frontend.lexer.predicates as pr
import cyt_prog.frontend.lexer.handlers as h

rules = [
    (pr.is_strLiteral_start(), h.StrLiteral()),
    (pr.is_numLiteral_start(), h.IntLiteral()),
    (pr.is_compare_start(), h.Compare()),
    (pr.is_assign_start(), h.Assign()),
]

# def tc_loop(source:str, pos: int):
#     pass

def tokenizer(source: str):
    TOKEN_STREAM = []
    while not c.at_end():
        ch = c.current()
        for (predicate, handler) in rules:
            if predicate(ch):
                handler()
                is_ok = True
                break
        if not is_ok:
            raise IllegalCharError

    TOKEN_STREAM.append(Token.kind.EOF)
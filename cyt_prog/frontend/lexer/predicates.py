from .permitted_char_sets import *

def is_strLiteral_start(ch: str):
    if ch in START.STR_LITERAL:
        return True
    return False

def is_strLiteral_continue(ch: str):
    if ch in CONTINUE.STR_LITERAL:
        return True
    return False

def is_numLiteral_start(ch: str):
    if ch in START.NUM_LITERAL:
        return True
    return False

def is_numLiteral_continue(ch: str):
    if ch in CONTINUE.NUM_LITERAL:
        return True
    return False

def is_compare_start(ch: str):
    if ch in START.COMPARISON:
        return True
    return False

def is_compare_continue(ch: str):
    if ch in CONTINUE.COMPARISON:
        return True
    return False

def is_assign_start(ch: str):
    if ch in START.ASSIGNMENT:
        return True
    return False

def is_assign_continue(ch: str):
    if ch in CONTINUE.ASSIGNMENT:
        return True
    return False
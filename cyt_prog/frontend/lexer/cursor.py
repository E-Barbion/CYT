class Cursor:
    def __init__(self, source: str):  # --> None
        self.source = source
        self.pos = 0
    
    def at_end(self):  # --> bool
        if self.pos >= len(self.source):
            return True
        return False

    def current(self):  # --> char
        if self.at_end():
            return None
        return self.source[self.pos]
    
    def advance(self):  # --> None
        if self.at_end():
            raise EOFError
        self.pos += 1

class TCursor(Cursor):
    def __init__(self, source: str, pos: int):  # --> None
        self.source = source
        self.pos = pos

    def scan(self, allowed_chars: set):  # --> str
        data = []
        while self.current() in allowed_chars and not self.at_end():
            data.append(self.current())
            self.advance()
        return "".join(data)


import sys
import string


initial_chars = string.ascii_letters + '!$%&*/:<=>?~_^'
subsequent_chars = initial_chars + string.digits + '.+-'


def cons(x, y ):
    pair = Lexeme("",Lexeme.GLUE)
    pair.car = x
    pair.cdr = y
    return pair


class Lexeme:

    ID = 0
    INT = 1
    FLOAT = 2
    STRING = 3
    CHAR = 4
    OPEN_PAREN = 5
    CLOSE_PAREN = 6
    PERIOD = 7
    BOOL = 8
    QUOTE = 9
    BACKTIC = 10
    GLUE = 11

    def __init__(self,value,lex_type):
        if lex_type == Lexeme.INT:
            self.value = int(value)
        elif lex_type == Lexeme.FLOAT:
            self.value = float(value)
        else:
            self.value = value
        self.lex_type = lex_type
        self.car = None
        self.cdr = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class Lexer:

    def __init__(self,infile):
        self.infile = infile
        self.curr_char = infile.read(1)
        self.line = 1
        self.col = 1

    def next(self):
        self.skip_whitespace()
        
        c = self.peek()
        if c == "":
            return None

        if c in initial_chars:
            return self.read_id()
        elif c in string.digits:
            return self.read_number()
        elif c == '"':
            return self.read_string()
        elif c == '(':
            self.get()
            return Lexeme(c,Lexeme.OPEN_PAREN)
        elif c == ')':
            self.get()
            return Lexeme(c,Lexeme.CLOSE_PAREN)
        elif c == '.':
            self.get()
            return Lexeme(c,Lexeme.PERIOD)
        elif c == '+':
            self.get()
            return Lexeme(c,Lexeme.ID)
        elif c == '-':
            self.get()
            return Lexeme(c,Lexeme.ID)
        elif c == '#':
            self.get()
            c = self.get()
            if c == 't':
                return Lexeme(True,Lexeme.BOOL)
            else:
                return Lexeme(False,Lexeme.BOOL)
        elif c == "'":
            self.get()
            return Lexeme("'",Lexeme.QUOTE)
        else:
            return None

    def read_id(self):
        value = self.get()
        
        while self.peek() in subsequent_chars and self.peek() != "":
            value += self.get()

        return Lexeme(value,Lexeme.ID)

    def read_number(self):
        lex_type = Lexeme.INT
        value = ''

        while self.peek() in string.digits:
            c = self.get()
            value += c
            if self.peek() == '.':
                lex_type = Lexeme.FLOAT
                value += self.get()
                
        return Lexeme(value,lex_type)

    def read_string(self):
        value = ''

        self.get()

        c = self.get()
        while c != '"':
            if c == '\\':
                if self.peek() == 'n':
                    self.get()
                    value += '\n'
            else:
                value += c
            c = self.get()

        return Lexeme(value,Lexeme.STRING)

   
    def skip_whitespace(self):
        while self.peek() in string.whitespace:
            c = self.get()
            if (c == ""):
                return ""

        if (self.skip_comment()):
            self.skip_whitespace()

    def skip_comment(self):
        if self.peek() == ';':
            self.get()
            while self.get() != '\n':
                i = 0 # do nothing
            return True
        else:
            return False
            

    def get(self):
        return_char = self.curr_char
        if return_char == '\n':
            self.line += 1
            self.col = 0
        else:
            self.col += 1

        self.curr_char = self.infile.read(1)
        return return_char

    def peek(self):
        return self.curr_char


if __name__ == '__main__':

    lex = Lexer(open(sys.argv[1]))

    curr_lexeme = lex.next()
    while curr_lexeme != None:
        print(str(curr_lexeme))
        curr_lexeme = lex.next()



    


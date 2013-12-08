
import sys
from lexer import *


class Recognizer:

    def __init__(self, filename):
        self.lex = Lexer(open(filename))
        self.curr_lexeme = self.lex.next()

    def program(self):
        while self.curr_lexeme != None:
            self.application()

    def applicationList(self):
        if self.applicationPending():
            self.application()
            self.applicationList()

    def application(self):
        self.match(Lexeme.OPEN_PAREN)
        self.expr()
        if self.exprListPending():
            self.exprList()
        self.match(Lexeme.CLOSE_PAREN)

    def exprList(self):
        if self.exprPending():
            self.expr()
            self.exprList()


    def expr(self):
        if self.check(Lexeme.ID):
            self.match(Lexeme.ID)
        elif self.check(Lexeme.BOOL):
            self.match(Lexeme.BOOL)
        elif self.check(Lexeme.INT):
            self.match(Lexeme.INT)
        elif self.check(Lexeme.FLOAT):
            self.match(Lexeme.FLOAT)
        elif self.check(Lexeme.STRING):
            self.match(Lexeme.STRING)
        elif self.check(Lexeme.CHAR):
            self.match(Lexeme.CHAR)
        elif self.check(Lexeme.QUOTE):
            self.match(Lexeme.QUOTE)
            self.datum()
        elif self.applicationPending():
            self.application()
        else:
            print("Parse Error!")
            exit()


    def list(self):
        if self.check(Lexeme.OPEN_PAREN):
            self.match(Lexeme.OPEN_PAREN)
            if self.datumListPending():
                self.datumList()
                if self.check(Lexeme.PERIOD):
                    self.match(Lexeme.PERIOD)
                    self.datum()
            self.match(Lexeme.CLOSE_PAREN)
        elif self.check(Lexeme.QUOTE):
            self.match(Lexeme.QUOTE)
            self.datum()
        elif self.check(Lexeme.BACKTIC):
            self.match(Lexeme.BACKTIC)
            self.datum()
        else:
            print("Parse Error!")
            exit()



    def datumList(self):
        if self.datumPending():
            self.datum()
            self.datumList()
    
    def datum(self):
        if self.check(Lexeme.BOOL):
            self.match(Lexeme.BOOL)
        elif self.check(Lexeme.INT):
            self.match(Lexeme.INT)
        elif self.check(Lexeme.FLOAT):
            self.match(Lexeme.FLOAT)
        elif self.check(Lexeme.CHAR):
            self.match(Lexeme.CHAR)
        elif self.check(Lexeme.STRING):
            self.match(Lexeme.STRING)
        elif self.check(Lexeme.ID):
            self.match(Lexeme.ID)
        elif self.listPending():
            self.list()
        else:
            print("Parse Error!")
            exit()

    def exprListPending(self):
        return self.exprPending()

    def exprPending(self):
        return self.datumPending() or \
               self.applicationPending()

    def applicationPending(self):
        return self.check(Lexeme.OPEN_PAREN)

    def listPending(self):
        return self.check(Lexeme.OPEN_PAREN) or \
               self.check(Lexeme.QUOTE) or \
               self.check(Lexeme.BACKTIC)

    
    def datumListPending(self):
        return self.datumPending()

    def datumPending(self):
        return self.check(Lexeme.BOOL) or \
               self.check(Lexeme.INT) or \
               self.check(Lexeme.CHAR) or \
               self.check(Lexeme.STRING) or \
               self.check(Lexeme.ID) or \
               self.listPending()

    def match(self,lex_type):
        if self.curr_lexeme == None:
            print("Parser Error!")
            exit()
        elif self.curr_lexeme.lex_type == lex_type:
            return_lexeme = self.curr_lexeme
            self.curr_lexeme = self.lex.next()
            print(str(return_lexeme))
            return return_lexeme
        else:
            print("Parser Error!")
            exit()

    def check(self,lex_type):
        if self.curr_lexeme == None:
            return False
        else:
            return lex_type == self.curr_lexeme.lex_type



if __name__ == "__main__":
    r = Recognizer(sys.argv[1])
    r.program()


import sys
from lexer import *


class Parser:

    def __init__(self,filename):
        self.lex = Lexer(open(filename))
        self.curr_lexeme = self.lex.next()

    def program(self):
        tree = []
        while self.curr_lexeme != None:
            tree += [self.application()]
        return tree


    def application(self):
        self.match(Lexeme.OPEN_PAREN)
        tree = [self.expr()]
        if self.exprListPending():
            tree = tree + self.exprList()
        self.match(Lexeme.CLOSE_PAREN)
        return tree

    def exprList(self):
        tree = []
        if self.exprPending():
            tree = [self.expr()] + self.exprList()
        return tree

    def expr(self):
        if self.check(Lexeme.ID):
            return self.match(Lexeme.ID)
        elif self.check(Lexeme.INT):
            return self.match(Lexeme.INT)
        elif self.check(Lexeme.FLOAT):
            return self.match(Lexeme.FLOAT)
        elif self.check(Lexeme.STRING):
            return self.match(Lexeme.STRING)
        elif self.check(Lexeme.CHAR):
            return self.match(Lexeme.CHAR)
        elif self.check(Lexeme.BOOL):
            return self.match(Lexeme.BOOL)
        elif self.check(Lexeme.QUOTE):
            q = self.match(Lexeme.QUOTE)
            d = self.datum()
            if isinstance(d,list):
                return [q] + d
            else:
                return [q,d]
        elif self.applicationPending():
            return self.application()
        else:
            print(self.curr_lexeme)
            print("Parse Error!")
            exit()

    def list(self):
        if self.check(Lexeme.OPEN_PAREN):
            self.match(Lexeme.OPEN_PAREN)
            tree = []
            if self.datumListPending():
                tree = self.datumList()
                if self.check(Lexeme.PERIOD):
                    self.match(Lexeme.PERIOD)
                    tree = [tree,self.datum()]
            self.match(Lexeme.CLOSE_PAREN)
            return tree
        elif self.check(Lexeme.QUOTE):
            q = self.match(Lexeme.QUOTE)
            d = self.datum()
            if isinstance(d,list):
                return [q] + d
            else:
                return [q,d]
        elif self.check(Lexeme.BACKTIC):
            return [self.match(Lexeme.BACKTIC),self.datum()]
        else:
            print(self.curr_lexeme)
            print("Parse Error!")
            exit()


    def datumList(self):
        tree = []
        if self.datumPending():
            tree = [self.datum()] + self.datumList()
        return tree

    def datum(self):
        if self.check(Lexeme.INT):
            return self.match(Lexeme.INT)
        elif self.check(Lexeme.FLOAT):
            return self.match(Lexeme.FLOAT)
        elif self.check(Lexeme.BOOL):
            return self.match(Lexeme.BOOL)
        elif self.check(Lexeme.STRING):
            return self.match(Lexeme.STRING)
        elif self.check(Lexeme.CHAR):
            return self.match(Lexeme.CHAR)
        elif self.check(Lexeme.ID):
            return self.match(Lexeme.ID)
        elif self.listPending():
            return self.list()
        else:
            print(self.curr_lexeme)
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
            print("None")
            print("Parser Error!")
            exit()
        elif self.curr_lexeme.lex_type == lex_type:
            return_lexeme = self.curr_lexeme
            self.curr_lexeme = self.lex.next()
            return return_lexeme
        else:
            print(self.curr_lexeme)
            print("Parser Error!")
            exit()

    def check(self,lex_type):
        if self.curr_lexeme == None:
            return False
        else:
            return lex_type == self.curr_lexeme.lex_type



if __name__ == '__main__':
    p = Parser(sys.argv[1])
    tree = p.program()
    print(tree)

    
 
    



class Environment:

    def __init__(self, enclosing_env=None):
        self.enclosing_env = enclosing_env
        self.table = dict()

    def insert(self, symbol, value):
        self.table[symbol] = value

    def update(self, symbol, value):
        if symbol in self.table:
            self.table[symbol] = value
        else:
            if self.enclosing_env == None:
                print("Error: " + symbol + " not defined!")
                exit()
            else:
                self.enclosing_env.update(symbol,value)

    def lookup(self, symbol):
        if symbol in self.table:
            return self.table[symbol]
        else:
            if self.enclosing_env == None:
                print(self.table)
                print("Error: " + symbol + " not defined!")
                exit()
            else:
                return self.enclosing_env.lookup(symbol)

    def extend(self):
        return Environment(self)

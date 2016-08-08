class _Connection:

    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db

class Connections:
    STOCK = _Connection("127.0.0.1", 'stock', 'stockaholic', 'stock')
    STOCK_TEST = _Connection("localhost", 'stocktest', 'tester', 'stocktest')

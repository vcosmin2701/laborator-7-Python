class Database:
    _INSTANCE = None

    @staticmethod
    def getInstance():
        if Database._INSTANCE is None:
            Database._INSTANCE = Database()
        return Database._INSTANCE

    def query(self, output):
        print(output)


Database.getInstance = staticmethod(Database.getInstance)
foo = Database.getInstance()
foo.query("SELECT...")

boo = Database.getInstance()
boo.query("SELECT...")

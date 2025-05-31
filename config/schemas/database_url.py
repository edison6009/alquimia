
class ConnectionData:
    def __init__(self, USER, PASSWORD, HOST, PORT, DATABASE, DIALECT, DRIVER):
        self.user = USER
        self.password = PASSWORD
        self.host = HOST
        self.port = PORT
        self.database = DATABASE
        self.dialect = DIALECT
        self.driver = DRIVER
        
    @property
    def url(self):
        return (
            f"{self.dialect}+{self.driver}://"
            f"{self.user}:{self.password}@"
            f"{self.host}:{self.port}/"
            f"{self.database}"
        )
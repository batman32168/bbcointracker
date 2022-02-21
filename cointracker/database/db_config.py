import os

class DB_CONFIG:
    HOST = 'localhost'
    PORT = 5432
    USER = 'potgres'
    PASSWORD = 'meins'
    DATABASE ='fifo'

    def __init__(self):
        if os.getenv('DB_HOST') is not None:
            self.HOST = os.getenv('DB_HOST')
        if os.getenv('DB_PORT') is not None:
            self.PORT = os.getenv('DB_PORT')
        if os.getenv('DB_USER') is not None:
            self.HOST = os.getenv('DB_USER')
        if os.getenv('DB_PASSWORD') is not None:
            self.HOST = os.getenv('DB_PASSWORD')
        if os.getenv('DATABASE') is not None:
            self.HOST = os.getenv('DATABASE')
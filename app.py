import redis
class Database:
    def __init__(self) -> None:
        self.__r__ = redis.Redis(host='localhost', port=6379)
    def set(self, key, data):
        self.__r__.set(key, data)
        print("Guardado exitosamente.")
        return key
    def get(self, key):
        self.__r__.get(key)
        print("Recuperado exitosamente.")

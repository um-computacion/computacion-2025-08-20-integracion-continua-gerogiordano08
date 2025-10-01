import redis
import json
class Database:
    def __init__(self) -> None:
        self.__r__ = redis.Redis(host='localhost', port=6379, decode_responses=True)
    def set_str(self, key, str):
        self.__r__.set(key, str)
        print("Guardado exitosamente.")
        return key
    def set_list(self, list_name, *items):
        self.__r__.delete(list_name)
        if items:
            self.__r__.rpush(list_name, *items)
    def list_append(self, list_name, *items):
        if items:
            self.__r__.rpush(list_name, *items)
    def get(self, key):
        g = self.__r__.get(key)
        print("Recuperado exitosamente.")
        return g
    def get_list(self, key):
        g = self.__r__.lrange(key, 0, -1, )
        print("Recuperado exitosamente.")
        return g
    def list_to_json(self, list_name, lista):
        self.__r__.set(list_name, json.dumps(lista))
    def json_to_list(self, list_name):
        raw = self.__r__.get(list_name)
        if raw is None:
            return []
        return json.loads(raw)
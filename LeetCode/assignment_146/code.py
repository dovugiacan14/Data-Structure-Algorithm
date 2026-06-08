from collections import OrderedDict, defaultdict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache: 
            return  -1 
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache: 
            self.cache.move_to_end(key)
        self.cache[key] = value 
        if len(self.cache) > self.capacity: 
            self.cache.popitem(last= False)

commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

res= []
obj = None 
for cmd, arg in zip(commands, args): 
    if cmd == "LRUCache": 
        obj = LRUCache(*arg)
        res.append(None)
    elif cmd == "put":
        obj.put(*arg)
        res.append(None)
    elif cmd == "get": 
        res.append(obj.get(*arg))
print(res)

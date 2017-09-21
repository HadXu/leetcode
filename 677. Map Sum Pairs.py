class MapSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = dict()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.map[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        sum = 0
        for k, v in self.map.items():
            if k.startswith(prefix):
                sum += v
        return sum




        # Your MapSum object will be instantiated and called as such:
        # obj = MapSum()
        # obj.insert(key,val)
        # param_2 = obj.sum(prefix)

if __name__ == '__main__':
    obj = MapSum()
    obj.insert('apple',3)
    obj.insert('app',2)
    res = obj.sum('ap')
    print(res)
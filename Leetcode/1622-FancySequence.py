class Fancy:

    def __init__(self):
        self.mod = 10**9 + 7
        self.arr = []
        self.mul = 1
        self.add = 0

    def append(self, val: int) -> None:
        # store normalized value
        val = (val - self.add) % self.mod
        val = val * pow(self.mul, -1, self.mod) % self.mod
        self.arr.append(val)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.mod
        self.add = (self.add * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        return (self.arr[idx] * self.mul + self.add) % self.mod

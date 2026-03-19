class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.front = 0
        self.rear = 0
        self.count = 0
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.count == self.size:
            return False
        
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.q[(self.rear - 1 + self.size) % self.size]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size

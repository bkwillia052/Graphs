class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return (len(self.queue))

    def values(self):
        print(self.queue)


q = Queue()

q.enqueue(1)
q.enqueue(3)
q.enqueue(2)
q.enqueue(10)

q.values()

q.dequeue()

q.values()


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return (len(self.stack))

    def values(self):
        print(self.stack)


s = Stack()

s.push(1)
s.push(3)
s.push(2)
s.push(10)

s.values()

s.pop()

s.values()

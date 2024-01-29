class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)        

    def pop(self) -> int:
        if self.queue:
            first_element = self.peek()
            self.queue = self.queue[1:]
            return first_element
        else:
            return []

    def peek(self) -> int:
        return self.queue[0] if self.queue else []

    def empty(self) -> bool:
        return True if not self.queue else False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
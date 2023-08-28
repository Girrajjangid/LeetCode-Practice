class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.queue:
            last_element = self.top()
            self.queue = self.queue[:-1]
            return last_element
        else:
            return []

    def top(self) -> int:
        return self.queue[-1] if self.queue else []

    def empty(self) -> bool:
        return True if not self.queue else False
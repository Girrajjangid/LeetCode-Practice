class CustomStack:
    def __init__(self, maxSize: int):
        # Initialize the stack as a deque for efficient add/remove operations
        self.stack = deque()
        self.max_size = maxSize

    def push(self, x: int) -> None:
        # Add the element to the top of the stack if it hasn't reached max_size
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        # Return -1 if the stack is empty, otherwise remove and return the top element
        return self.stack.pop() if self.stack else -1

    def increment(self, k: int, val: int) -> None:
        # Increment the bottom k elements (or all elements if k > stack size)
        for i, _ in zip(range(k), self.stack):
            self.stack[i] += val
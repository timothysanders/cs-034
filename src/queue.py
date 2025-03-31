
class Queue:
    def __init__(self, max_length: int = -1) -> None:
        self.items = []
        self.max_length = max_length

    def enqueue(self, value):
        if self.
class Stack:
    def __init__(self):
        self.items = []

    def get_stack(self):
        return self.items

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Index out of bounds")

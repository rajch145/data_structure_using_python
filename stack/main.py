class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def top(self):
        if self.items:
            return self.items[0]

    def is_empty(self):
        if self.items:
            return False
        else:
            return True

    def print_stack(self):
        print(self.items)


if __name__ == "__main__":
    stack = Stack()
    def switch(num):
        switcher = {
        1 : stack.push,
        2 : stack.pop,
        3 : stack.top,
        4 : stack.is_empty,
        5 : stack.print_stack,
        }
        return switcher.get(num)
    while(True):
        print('Please select the operation')
        print('1: add to stack')
        print('2: remove from stack')
        print('3: check top')
        print('4: check if empty')
        print('5: print stack')
        num = int(input('Enter your choice'))
        if num==1:
            data = input('Enter your data')
            print(switch(num)(data))
        else:
            print(switch(num)())

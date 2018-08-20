class Queue:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop(0)

    def top(self):
        if self.items:
            return self.items[len(self.items)-1]

    def is_empty(self):
        if self.items:
            return False
        else:
            return True

    def print_queue(self):
        print(self.items)


if __name__ == "__main__":
    queue = Queue()
    def switch(num):
        switcher = {
        1 : queue.push,
        2 : queue.pop,
        3 : queue.top,
        4 : queue.is_empty,
        5 : queue.print_queue,
        }
        return switcher.get(num)
    while(True):
        print('Please select the operation')
        print('1: add to queue')
        print('2: remove from queue')
        print('3: check top')
        print('4: check if empty')
        print('5: print queue')
        num = int(input('Enter your choice'))
        if num==1:
            data = input('Enter your data')
            print(switch(num)(data))
        else:
            print(switch(num)())

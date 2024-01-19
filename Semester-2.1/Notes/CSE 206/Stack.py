class Stack:
    __maxSize = 0
    __a = []
    __top = -1

    def __init__(self, size: int):
        self.__maxSize = size

    def size(self) -> int:
        return self.__top + 1

    def isFull(self) -> bool:
        return self.__top == self.__maxSize - 1

    def isEmpty(self) -> bool:
        return self.__top == - 1

    def top(self) -> int:
        if self.__top != -1:
            return self.__a[self.__top]
        else:
            return -1

    def isPeek(self, n: int) -> int:
        return n == self.top()

    def push(self, n: int) -> int:
        if not self.isFull():
            self.__a.append(n)
            self.__top += 1
        else:
            print("Stack overflow!\n")

    def pop(self) -> int:
        if not self.isEmpty():
            item = self.__a[self.__top]
            self.__top -= 1
            self.__a.pop()
            return item
        else:
            print("Stack underflow!\n")
            return -1

    def printAll(self):
        for n in self.__a:
            print(n, end=" ")
        print()


size = int(input("Enter Stack capcity: "))
s = Stack(size)
print()

while (True):
    print("Stack Operation:\n1. Push item\n2. Pop item\n3. View Top\n4. Check if the stack is full?\n5. Check if the stack is empty?\n6. Print all elements.\n0. Exit")
    option = int(input("Select: "))
    print()

    match option:
        case 1:
            n = int(input("Enter a number: "))
            s.push(n)

        case 2:
            item = s.pop()
            if item != -1:
                print(f"{item} has been poped.\n")

        case 3:
            if s.top() != -1:
                print(f"Top item: {s.top()}.\n")
            else:
                print("No element in Stack.\n")

        case 4:
            if s.isFull():
                print("Stack is full.\n")
            else:
                print("Stack is not full.\n")

        case 5:
            if s.isEmpty():
                print("Stack is empty.\n")
            else:
                print("Stack is not empty.\n")

        case 6:
            print("Stack items: ")
            s.printAll()

        case 0:
            break

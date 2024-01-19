def BubbleSort(a: list[int]):
    for i in range(len(a)):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


def PrintArray(a: list[int]):
    for n in a:
        print(n, end=" ")
    print()


a = [3, 4, 2, 1, 9, 8, 7, 6, 5]
BubbleSort(a)
PrintArray(a)

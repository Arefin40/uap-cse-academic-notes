def Selection(a: list[int]):
    for i in range(len(a)):
        min = i
        for j in range(i + 1, len(a)):
            print(a[j], end=" ")
            if a[j] < a[min]:
                min = i
        print(f"Min: {a[min]}")

        # a[i], a[min] = a[min], a[i]


def PrintArray(a: list[int]):
    for n in a:
        print(n, end=" ")
    print()


a = [3, 4, 2, 1, 9, 8, 7, 6, 5]
Selection(a)
# PrintArray(a)
# print()

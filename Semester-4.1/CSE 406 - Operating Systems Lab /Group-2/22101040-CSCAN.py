head, disc_size = 53, 200
req = sorted([98, 183, 37, 122, 14, 124, 65, 67])

left = [r for r in req if r < head]
right = [r for r in req if r >= head]
paths = [head] + right + [disc_size - 1, 0] + left

total = sum(abs(paths[i] - paths[i - 1]) for i in range(1, len(paths)))

print(" -> ".join(map(str, paths)))
print(f"Total movements: {total}")

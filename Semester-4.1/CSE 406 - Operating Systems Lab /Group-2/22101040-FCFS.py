head_position = int(input("Enter head position: "))
requests = [98, 183, 37, 122, 14, 124, 65, 67]

total_movement = 0
current_position = head_position
movement_path = [head_position]

for request in requests:
    total_movement += abs(request - current_position)
    current_position = request
    movement_path.append(request)

print(f"Total movement: {total_movement}")
print("Path of movement:", " -> ".join(map(str, movement_path)))

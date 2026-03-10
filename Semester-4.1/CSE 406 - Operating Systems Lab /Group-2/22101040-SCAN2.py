requests = [98, 183, 37, 122, 14, 124, 65, 67]
initial_head = int(input("Enter head position: "))
max_cylinder = 200
scan_direction = "down"

sorted_requests = sorted(requests)
total_head_movement = 0
head_position = initial_head
movement_sequence = [initial_head]

requests_left = [req for req in sorted_requests if req < initial_head]
requests_right = [req for req in sorted_requests if req >= initial_head]

if scan_direction == "up":
    for req in requests_right:
        total_head_movement += abs(head_position - req)
        head_position = req
        movement_sequence.append(req)

    if head_position != max_cylinder - 1:
        total_head_movement += abs(head_position - (max_cylinder - 1))
        head_position = max_cylinder - 1
        movement_sequence.append(head_position)

    for req in reversed(requests_left):
        total_head_movement += abs(head_position - req)
        head_position = req
        movement_sequence.append(req)
else:
    for req in reversed(requests_left):
        total_head_movement += abs(head_position - req)
        head_position = req
        movement_sequence.append(req)

    if head_position != 0:
        total_head_movement += abs(head_position - 0)
        head_position = 0
        movement_sequence.append(head_position)

    for req in requests_right:
        total_head_movement += abs(head_position - req)
        head_position = req
        movement_sequence.append(req)

print("Total movement:", total_head_movement)
print("Path of movement:", " -> ".join(map(str, movement_sequence)))

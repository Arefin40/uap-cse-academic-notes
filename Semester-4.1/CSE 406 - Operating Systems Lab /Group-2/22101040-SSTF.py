head_position = int(input("Enter head position: "))
requests = [98, 183, 37, 122, 14, 124, 65, 67]

pending_requests = requests.copy()
total_movement = 0
current_position = head_position
movement_path = [head_position]

while pending_requests:
    closest_request = min(pending_requests, key=lambda r: abs(r - current_position))
    total_movement += abs(closest_request - current_position)
    current_position = closest_request
    movement_path.append(closest_request)
    pending_requests.remove(closest_request)

print(f"Total movement: {total_movement}")
print("Path of movement:", " -> ".join(map(str, movement_path)))

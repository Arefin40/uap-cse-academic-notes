n = int(input("Enter the number of processes: "))
q = int(input("Enter quantum: "))

time = 0
processes = []
remaining = []

print("Enter burst time for the following processes:")
for i in range(n):
    t = int(input(f"p{i + 1}: "))
    processes.append(t)
    remaining.append(t)

waiting_times = [0] * n
turnarounds = [0] * n

sequence = []
time_points = []

done = False
while not done:
    done = True
    for i in range(n):
        if remaining[i] > 0:
            done = False
            sequence.append(f"p{i + 1}")
            time_points.append(time)
            if remaining[i] > q:
                time += q
                remaining[i] -= q
            else:
                time += remaining[i]
                waiting_times[i] = time - processes[i]
                remaining[i] = 0

print("Sequence:", end=" ")
for idx in range(len(sequence)):
    print(f"{time_points[idx]} {sequence[idx]}", end=" ")
print(time)

for i in range(n):
    turnarounds[i] = processes[i] + waiting_times[i]

avg_wt = sum(waiting_times) / n

print(f"Average waiting time: {avg_wt}")

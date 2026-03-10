n = int(input("Enter the number of processes: "))

time = 0
processes = []
waiting_times = []

print("Enter burst time and priority for the following processes:")
for i in range(n):
    bt, pr = input(f"p{i + 1}: ").split(" ")
    processes.append((f"p{i + 1}", int(bt), int(pr)))

processes.sort(key=lambda x: x[2])

print("Sequence:", end=" ")
for process in processes:
    waiting_times.append(time)
    pid, burst, priority = process
    print(f"{time} {pid}", end=" ")
    time += burst
print(time)


print(f"Average waiting time: {(sum(waiting_times)) / n} ms")

"""
4
21 2
3 1
6 4
2 3
"""

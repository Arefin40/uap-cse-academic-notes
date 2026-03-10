def cpu_scheduling_algorithm():
    wait_time = 0
    total_time = 0
    processes_input = input("Enter the processes (p1-21 p2-3): ").split(" ")
    print()

    processes = []
    for process in processes_input:
        name, time = process.split("-")
        processes.append((name, int(time)))

    processes.sort(key=lambda x: x[1])

    print("Sequence of processes:", end="")
    for name, time in processes:
        print(f" {wait_time} {name}", end="")
        wait_time += time
        total_time += wait_time
    print(f" {wait_time}")

    avg_waiting_time = (total_time - wait_time) / len(processes)

    print(f"Average waiting time: {avg_waiting_time:.2f}")


cpu_scheduling_algorithm()

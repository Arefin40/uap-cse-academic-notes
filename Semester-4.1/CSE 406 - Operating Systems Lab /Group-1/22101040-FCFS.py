def cpu_scheduling_algorithm():
    wait_time = 0
    total_time = 0
    processes = input("Enter the processes (p1-21 p2-3): ").split(" ")
    print()

    print("Sequence of processes:", end="")
    for process in processes:
        name, time = process.split("-")
        print(f" {wait_time} {name}", end="")
        wait_time += int(time)
        total_time += wait_time
    print(f" {wait_time}")

    avg_waiting_time = (total_time - wait_time) / len(processes)

    print(f"Average waiting time: {avg_waiting_time:.2f}")


cpu_scheduling_algorithm()

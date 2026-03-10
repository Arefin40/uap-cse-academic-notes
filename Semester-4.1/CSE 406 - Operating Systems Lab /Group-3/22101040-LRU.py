def LRU(reference_string, queue_size):
    faults = 0
    queue = []
    last_accessed = []

    def least_recently_used():
        min_time = min(last_accessed)
        return last_accessed.index(min_time)

    for t, page in enumerate(reference_string):
        # print("Time:", t, "Page:", page)
        # print("Queue:", queue)
        # print("Last Accessed:", last_accessed, end="\n\n")

        if page in queue:
            idx = queue.index(page)
            last_accessed[idx] = t
            print("HIT")
        elif len(queue) < queue_size:
            faults += 1
            queue.append(page)
            last_accessed.append(t)
            print(f"MISS: {queue}")
        else:
            faults += 1
            idx = least_recently_used()
            queue[idx] = page
            last_accessed[idx] = t
            print(f"MISS: {queue}")

        print(f"\n{'-' * 20}")
    print(f"Faults: {faults}")


if __name__ == "__main__":
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    queue_size = 3
    LRU(reference_string, queue_size)

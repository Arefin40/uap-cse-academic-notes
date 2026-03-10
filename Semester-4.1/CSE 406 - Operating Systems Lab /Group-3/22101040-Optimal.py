def optimal_page_replacement(reference_string, queue_size):
    from collections import defaultdict, deque

    faults = 0
    queue = []
    access_times = defaultdict(deque)

    for t, page in enumerate(reference_string):
        access_times[page].append(t)

    def get_farthest_index():
        farthest_time = -1
        farthest_idx = 0
        for idx, page in enumerate(queue):
            if not access_times[page]:
                return idx
            next_time = access_times[page][0]
            if next_time > farthest_time:
                farthest_time = next_time
                farthest_idx = idx
        return farthest_idx

    for t, page in enumerate(reference_string):
        print("Time:", t, "Page:", page)
        print("Queue:", queue)
        print("Last Accessed:", dict(access_times), end="\n\n")

        if page in queue:
            print("HIT")
        elif len(queue) < queue_size:
            faults += 1
            queue.append(page)
            print(f"MISS: {queue}")
        else:
            faults += 1
            idx = get_farthest_index()
            queue[idx] = page
            print(f"MISS: {queue}")
        access_times[page].popleft()

    print(f"Faults: {faults}")


if __name__ == "__main__":
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    queue_size = 3
    optimal_page_replacement(reference_string, queue_size)

def FIFO(reference_string, queue_size):
    queue = [None] * queue_size
    pointer = 0
    faults = 0

    for page in reference_string:
        if page not in queue:
            queue[pointer] = page
            pointer = (pointer + 1) % queue_size
            print(f"MISS: {queue}")
            faults += 1
        else:
            print("HIT")
    print(f"Faults: {faults}")


if __name__ == "__main__":
    # reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    reference_string = [8, 1, 2, 3, 1, 4, 1, 5, 3, 4, 1, 4, 3, 2, 3, 1, 2, 8, 2]
    queue_size = 3
    FIFO(reference_string, queue_size)

mutex = 1
x = 0
empty = 0
full = 0

def producer():
    global mutex, x, empty, full
    mutex = wait(mutex)
    empty = wait(empty)
    full = signal(full)
    x += 1
    print("Producer produced item", x)
    mutex = signal(mutex)

def consumer():
    global mutex, x, empty, full
    mutex = wait(mutex)
    empty = signal(empty)
    full = wait(full)
    print("Consumer consumed item", x)
    x -= 1
    mutex = signal(mutex)

def signal(s):
    return s + 1

def wait(s):
    return s - 1

def main():
    global mutex, empty, full
    ans = int(input("Enter the type of semaphore to use: (1) Binary Semaphore (2) Counting Semaphore: "))
    if ans == 1:
        empty = 1
    elif ans == 2:
        n = int(input("Enter the number of resources for counting semaphore: "))
        empty = n
        mutex = 1
    while True:
        ch = int(input("Enter choice: (1) Produce (2) Consume (3) Exit: "))
        if ch == 1:
            if mutex == 1 and empty != 0:
                producer()
            else:
                print("Buffer is full")
        elif ch == 2:
            if mutex == 1 and full != 0:
                consumer()
            else:
                print("Buffer is empty")
        elif ch == 3:
            break

if __name__ == "__main__":
    main()

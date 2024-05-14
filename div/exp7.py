import threading
import time
import math

shared_resource = 0

lock = threading.Lock()

def increment_shared_resource():
    global shared_resource
    for _ in range(5):
        lock.acquire(blocking=False)
        # print('Shared resource value',shared_resource)
        shared_resource += 1
        # time.sleep(1)
        lock.release()
        
# Create multiple threads
threads = []
for _ in range(6):
    thread = threading.Thread(target=increment_shared_resource)
    threads.append(thread)
    print("Shared resource value:",shared_resource)
    print("Thread",thread)
    thread.start()
    # time.sleep(0.1)
    # thread.join()

# time.sleep(1)
# Wait for all threads to complete
for thread in threads:
    thread.join()
# while threading.active_count() > 1:  # Main thread is also running
#     pass
# Print the final value of the shared resource
print("Final value of shared resource:", shared_resource)

import time
class Semaphore:
    def __init__(self,value):
        self.value = value
        self.waitingqueue = []
        self.in_CS = []
    def current_value(self):
        print("Number of process that can enter the critical section:",self.value)
processno = 1
def P(s):
    global processno
    if s.value == 0:
        print(f"Process {processno} Blocked")
        s.waitingqueue.append(processno)
    else:
        print(f"Process {processno} entered the critical section")
        s.in_CS.append(processno)
        s.value -= 1
    processno+=1
def V(s):
    global processno
    if len(s.in_CS) == 0:
        print("Critical Section Free")
        return
    print(f"Process {s.in_CS.pop(0)} waked up and is completed.")
    if len(s.waitingqueue) != 0:
        tmp = s.waitingqueue.pop(0)
        s.in_CS.append(tmp)
        print(f"Process {tmp} is entering critical section")
    else:
        s.value += 1

val = int(input("Enter the value of semaphore(The number of processes that can enter the critical section at once):"))
s = Semaphore(val)
s.current_value()
n = int(input("Enter the number of process: "))
for i in range(n):
    P(s)
    s.current_value()
    time.sleep(2)
for i in range(n):
    V(s)
    s.current_value()
    time.sleep(2)
print("WORKING COMPLETE")
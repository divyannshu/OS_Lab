import threading
import pprint

def is_safe_state(available, max_claim, allocated):
    num_processes=len(allocated)
    num_resources=len(available)

    # Initialize work and finish arrays
    work=available[:]
    finish =[False] * num_processes

    safe_sequence=[]

    #loop through processes until all are finished or no safe sequence exists
    while True:
        #finding an index i such that process i is not finished and needs <= available
        found= False
        for i in range(num_processes):
            if not finish[i] and all(need + work[j] >= max_claim[i][j] for j, need in enumerate(allocated[i])):
                for j in range(num_resources):
                    work[j]+= allocated[i][j]
                finish[i]=True
                safe_sequence.append(i)
                print(safe_sequence)
                print("Available",work)
                print('found')
                found=True
        if not found:
            print('Not found')
            break

    #check if all processes are finished, return safe sequence
    if all(finish):
        return safe_sequence
    else:
        print("No safe sequence found.")
        return None
    
available_resources = [3,4,2]
max_needed_resources = [
    [7, 5, 3],
    [3, 2, 2],
    [3, 1, 4],
    [4, 2, 2]
]
allocated_resources = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1]
]

# Deadlock resources
# max_needed_resources = [
#     [7, 5, 3],
#     [3, 2, 2],
#     [9 ,0 ,2],
#     [4, 2, 2]
# ]

safe_sequence = is_safe_state(available_resources, max_needed_resources, allocated_resources)

# print(len(safe_sequence)," ",len(max_needed_resources))
# if len(safe_sequence)==len(max_needed_resources):
print("Safe sequence:", safe_sequence)
# else:



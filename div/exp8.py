from collections import deque
from collections import defaultdict
from prettytable import PrettyTable
table = PrettyTable()
table.field_names=["Frames"]


def fifo(page_reference_string, num_frames):
    page_faults = 0
    frames = []
    hitmiss=[]
    for page in page_reference_string:
        table.clear_rows()
        if page not in frames:
            page_faults += 1
            if len(frames) < num_frames:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            hitmiss.append('Miss')
        else:
          hitmiss.append('Hit')
        print('[',frames,']')
        for i in frames:
            table.add_row([str(i)])
        if len(frames)<num_frames:
              for i in range(num_frames-len(frames)):
                  table.add_row([" "])
        print(table)
    print(hitmiss)
    return page_faults

def lru(page_reference_string, num_frames):
    
    page_faults = 0
    # frames = deque(maxlen=num_frames)
    frames=[]
    hitmiss=[]

    for page in page_reference_string:
        table.clear_rows()
        if page not in frames:
            page_faults += 1
            if len(frames) == num_frames:
                frames.pop(0)
            frames.append(page)
            hitmiss.append('Miss')
        else:
            frames.remove(page)
            frames.append(page)
            hitmiss.append('Hit')
        frame1=list(frames)
        print('[',frame1,']')
        for i in frame1:
            table.add_row([str(i)])
        if len(frame1)<num_frames:
              for i in range(num_frames-len(frame1)):
                  table.add_row([" "])
        print(table)

    print(hitmiss)
    return page_faults

def lfu(page_reference_string, num_frames):
    page_faults = 0
    frames = []
    hitmiss=[]
    page_access_count = defaultdict(int)

    for page in page_reference_string:
        table.clear_rows()
        if page not in frames:
            page_faults += 1
            if len(frames) == num_frames:
                # Remove the least frequently used page
                least_used_page = min(frames, key=lambda x: page_access_count[x])
                frames.remove(least_used_page)
            frames.append(page)
            hitmiss.append('Miss')
        else:
            hitmiss.append('Hit')
        page_access_count[page]+=1
        print('[',frames,']')
        for i in frames:
            table.add_row([str(i)])
        if len(frames)<num_frames:
              for i in range(num_frames-len(frames)):
                  table.add_row([" "])
        print(table)
    print(hitmiss)
    return page_faults

def main():
    with open('input.txt', 'r') as file:
        page_reference_string = list(map(int, file.readline().strip().split()))
        num_frames = int(file.readline().strip())

    page_faults = fifo(page_reference_string, num_frames)
    print("Page faults using FIFO algorithm:", page_faults)

    page_faults = lru(page_reference_string, num_frames)
    print("Page faults using LRU algorithm:", page_faults)

    page_faults = lfu(page_reference_string, num_frames)
    print("Page faults using LFU algorithm:", page_faults)

if __name__ == "__main__":
    main()

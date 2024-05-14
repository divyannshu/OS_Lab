frames=[]
page_faults = 0
page_table={}
def paging(page_num,num_frames):
    if page_num not in frames:
            # page_faults += 1
            if len(frames) < num_frames:
                frames.append(page_num)
                page_table[page_num]=len(frames)-1
            else:
                print("Replacing using FIFO algorithm")
                first=frames[0]
                frames.pop(0)
                frames.append(page_num)
                page_table.pop(first)
                page_table[page_num]=0
            print('Miss')
            
    else:
         print('Page already in Main Memory')
         print('Hit') 
    return page_table
logical_address=int(input('Enter size of logical address'))
physical_address=int(input('Enter size of primary adress'))
lst=[]
for i in range(1,physical_address):
    if physical_address%i==0 and logical_address%i==0:
        lst.append(i)

print(lst)
page_size=int(input('Enter any one page size  '))
if page_size in lst:
    num_pages=int(logical_address/page_size)
    num_frames=int(physical_address/page_size)
    # page_string=[]
    # for i in range(0,num_pages):
    #     print(i)
    #     page_string.append(i)
    
    while True:
        print('Enter page number in range 0 to ',num_pages-1)
        page_num=int(input())
        if page_num<0 or page_num>=num_pages:
            print('Invalid page number')
        else:
           page_table=paging(page_num,num_frames)
        print("Page Table",page_table)
else:
    print('Not a valid page size')


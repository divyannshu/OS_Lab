import matplotlib.pyplot as plt

def fcfs(processes):
    start_time = 0
    gantt_chart = []

    for pid, arrival_time, burst_time in processes:
        # Wait until the arrival time
        if start_time < arrival_time:
            start_time = arrival_time
        gantt_chart.append((start_time, start_time + burst_time, pid))
        start_time += burst_time

    return gantt_chart

def draw_gantt_chart(gantt_chart):
    plt.figure(figsize=(10, 2))
    plt.title('Gantt Chart - FCFS')
    plt.xlabel('Time')
    plt.ylabel('Process')
    plt.grid(True)

    yticks = [f'P{pid}' for _, _, pid in gantt_chart]
    start_times = [start for start, _, _ in gantt_chart]
    end_times = [end for _, end, _ in gantt_chart]

    plt.barh(y=yticks, width=[end - start for start, end, _ in gantt_chart], left=start_times, color='skyblue')
    plt.xlim(0, max(end_times) + 2)
    plt.ylim(-1, len(gantt_chart))
    plt.yticks(range(len(gantt_chart)), yticks)

    for i in range(len(gantt_chart)):
        plt.text((gantt_chart[i][0] + gantt_chart[i][1]) / 2 - 0.5, i, f'{gantt_chart[i][1] - gantt_chart[i][0]}', color='black', fontsize=10)

    plt.show()

if __name__ == '__main__':
    # Accept process information from the user
    num_processes = int(input("Enter the number of processes: "))
    processes = []
    for i in range(num_processes):
        pid = int(input(f"Enter Process ID for Process {i + 1}: "))
        arrival_time = int(input(f"Enter Arrival Time for Process {i + 1}: "))
        burst_time = int(input(f"Enter Burst Time for Process {i + 1}: "))
        processes.append((pid, arrival_time, burst_time))

    # Sort processes by arrival time
    processes.sort(key=lambda x: x[1])

    # FCFS scheduling
    gantt_chart = fcfs(processes)

    # Display Gantt chart
    draw_gantt_chart(gantt_chart)

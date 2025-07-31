import matplotlib.pyplot as plt

#TASK1
# Processes: [PID, ArrivalTime, BurstTime]
processes = [
    ["P1", 0, 3],
    ["P2", 5, 4],
    ["P3", 6, 2],
    ["P4", 7, 6]
]

processes.sort(key=lambda x: x[1])

current_time = 0
for p in processes:
    pid, at, bt = p
    st = max(current_time, at)
    ct = st + bt
    tat = ct - at
    wt = tat - bt
    rt = st - at
    
    p.extend([st, ct, tat, wt, rt])
    current_time = ct

print("PID\tAT\tBT\tST\tCT\tTAT\tWT\tRT")
for p in processes:
    print("\t".join(str(x) for x in p))


#TASK 2: Performance Metrics
n = len(processes)
avg_wt = sum(p[6] for p in processes) / n 
avg_tat = sum(p[5] for p in processes) / n 
avg_rt = sum(p[7] for p in processes) / n 

print("\nAverage Waiting Time:", round(avg_wt, 2))
print("Average Turnaround Time:", round(avg_tat, 2))
print("Average Response Time:", round(avg_rt, 2))

# Task 3:Gantt Chart
#extracting data for plotting
pids = [p[0] for p in processes]         
completion_times = [p[4] for p in processes]
waiting_times = [p[6] for p in processes]
response_times = [p[7] for p in processes]


plt.figure(figsize=(8, 5), facecolor='lightblue')

plt.plot(pids, response_times, marker='o', label='Response Time')
plt.plot(pids, completion_times, marker='o', label='Completion Time')
plt.plot(pids, waiting_times, marker='o', label='Waiting Time')

plt.legend()
plt.show()

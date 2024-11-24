import threading

def sumtotal(ID, startvalue, endvalue, results):
    rangesum = sum(range(startvalue,endvalue)) + endvalue
    results[ID] = rangesum

ranges = [
    [10, 20],
    [1, 5],
    [70, 80],
    [27, 92],
    [0, 16]
]

results = [0] * len(ranges)
threads = []
count = 0

for i in ranges:
    thread = threading.Thread(target=sumtotal, args=(count, i[0], i[1], results))
    thread.start()
    threads.append(thread)
    count += 1

for thread in threads:
    thread.join()

print(results)
print(sum(results))
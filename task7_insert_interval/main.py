intervals = [[3, 5], [8, 10], [1, 2], [6, 7], [12, 16]]
newInterval = [4, 8]
intervals = [[6, 9], [1, 3]]
newInterval = [2, 5]
intervals.append(newInterval)
intervals.sort()

result = []
i = 0
step = 1
while i < len(intervals):
    current = intervals[i]
    right = current[1]
    while i + step < len(intervals) and right >= intervals[i + step][0]:
        right = max(right, intervals[i + step][1])
        step += 1
    result.append([current[0], right])
    i += step
    step = 1

print(intervals)
print(result)
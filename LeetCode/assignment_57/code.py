def insert(intervals, newInterval):
    intervals.append(newInterval)
    def merge(intervals):
        idx = 1
        intervals= sorted(intervals, key=lambda x: x[0])
        while True:
            n_interval = len(intervals)
            if idx >= n_interval:
                break 
            if intervals[idx][0] >= intervals[idx-1][0] and intervals[idx][0] <= intervals[idx-1][1]:
                if intervals[idx][1] >= intervals[idx-1][1]:
                    intervals[idx-1][1] = intervals[idx][1]
                del intervals[idx]
            else: 
                idx += 1  
        return intervals
    result = merge(intervals)
    return result 

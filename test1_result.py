

def getMinRooms(meetingTimings):
    n = len(meetingTimings)
    ans = 0
    count = 0
    times = []

    for st, en in meetingTimings:
        times.append([st, 1])
        times.append([en, -1])
        times.sort()

    for _, val in times:
        count += val
        print(count)
        print(val)
        print("---")
        ans = max(ans, count)
    return ans


meetingTimings = [[2, 8], [3, 7], [4, 6], [1, 9], [2, 5]]
print(getMinRooms(meetingTimings)) 
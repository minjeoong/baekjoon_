def min_meeting_rooms(meeting_timings):
    if not meeting_timings:
        return 0

    start_times = [timing[0] for timing in meeting_timings]
    print(start_times)

    end_times = [timing[1] for timing in meeting_timings]
    print(end_times)

    # 시작 시간과 종료 시간을 정렬
    start_times.sort()
    end_times.sort()

    min_rooms = 0
    available_rooms = 0
    start_ptr = 0
    end_ptr = 0

    while start_ptr < len(start_times):
        # 현재 회의의 시작 시간이 이전 회의의 종료 시간보다 크거나 같으면
        # 같은 회의실을 사용할 수 있으므로 종료 시간을 늘리고 포인터를 이동
        if start_times[start_ptr] >= end_times[end_ptr]:
            available_rooms -= 1
            end_ptr += 1

        # 새로운 회의실이 필요한 경우
        available_rooms += 1
        min_rooms = max(min_rooms, available_rooms)
        start_ptr += 1
        print(available_rooms)
        print(min_rooms)
        print(start_ptr)
        print(end_ptr)
        print( "------")
    return min_rooms


n = 5
meeting_timings = [[2, 8], [3, 4], [3, 9], [5, 11], [11, 15], [8,20]]
print(min_meeting_rooms(meeting_timings)) 

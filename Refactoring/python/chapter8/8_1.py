def track_summary(points):
    # 두 지점의 거리 계산
    def distance(p1, p2):
        pass

    # 라디안 값으로 변환
    def radians(degrees):
        pass

    # 총 시간 계산
    def calculate_time():
        pass

    # 총 거리 계산
    def calculate_distance():
        result = 0
        for i in range(len(points)):
            result += distance(points[i-1], points[i])
        return result

    total_time = calculate_time()
    total_distance = calculate_distance()
    pace = total_time / 60 / total_distance

    return {
        "time": total_time,
        "distance": total_distance,
        "pace": pace,
    }

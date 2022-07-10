import math


def track_summary(points):
    # 총 시간 계산
    def calculate_time():
        pass

    total_time = calculate_time()
    pace = total_time / 60 / top_calculate_distance(points)

    return {
        "time": total_time,
        "distance": top_calculate_distance(points),
        "pace": pace,
    }


# 총 거리 계산
def top_calculate_distance(points):
    result = 0
    for i in range(len(points)):
        result += distance(points[i - 1], points[i])
    return result


# 두 지점의 거리 계산
def distance(p1, p2):
    radians(1234)
    return p1 - p2  # 책 따라하면 너무 김. 간단하게.


# 라디안 값으로 변환
def radians(degrees):
    return degrees * math.pi / 180

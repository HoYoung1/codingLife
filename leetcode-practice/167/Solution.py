from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while numbers[start] + numbers[end] != target:
            temp = numbers[start] + numbers[end]
            if temp > target:
                end -= 1
            else:  # == elif temp < target:
                start += 1

        return [start + 1, end + 1]  # +1 -> index starts from 1


if __name__ == '__main__':
    s = Solution()

    numbers = [2, 7, 11, 15]
    target = 9
    assert s.twoSum(numbers, target) == [1,2]

    numbers = [2,3,4]
    target = 6
    assert s.twoSum(numbers, target) == [1, 3]

    numbers = [-1, 0]
    target = -1
    assert s.twoSum(numbers, target) == [1, 2]


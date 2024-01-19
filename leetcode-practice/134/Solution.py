from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_minus_cost = [gas - cost for gas, cost in zip(gas, cost)]
        for i in range(len(gas_minus_cost)):
            if gas_minus_cost[i] <= 0:
                continue

            result = 0
            # result += gas[i] # fill_up with start station
            for j in range(0, len(gas)):
                if (i + j + 1) % len(gas) == i:
                    # 출발지 도착
                    return result
                result += gas[(i+j) % len(gas)]
                result -= cost[(i+j) % len(gas)]
                if result < 0:
                    return -1



gas , cost = [1,2,3,4,5], [3,4,5,1,2]
assert Solution().canCompleteCircuit(gas, cost) == 3

gas , cost = [2,3,4], [3,4,3]
assert Solution().canCompleteCircuit(gas, cost) == -1

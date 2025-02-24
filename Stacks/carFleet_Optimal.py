class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort car by decending pos
        # if time to reach destination is > last num in stack, its new fleet, add to stack

        sortedCars = [(pos, spd) for pos, spd in zip(position, speed)]
        sortedCars.sort(reverse=True)
        stack = []

        for pos, spd in sortedCars:
            time_reach_des = (target-pos)/spd
            if len(stack) == 0 or time_reach_des > stack[-1]:
                stack.append(time_reach_des)
        return len(stack)

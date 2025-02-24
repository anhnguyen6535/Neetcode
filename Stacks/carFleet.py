import heapq
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort car by its starting position from the closest to 0 to closest to target: O(logn)
        # loop thru this sorted array
        # check each pair to see if fleet increases or not

        # question: how to sort speed array too?
        # store in a heap min
        if len(position) == 1: return 1
        minHeap = []
        stack = []

        for idx in range(len(position)):
            heapq.heappush(minHeap, [-position[idx], speed[idx]])

        while minHeap:
            stack.append(heapq.heappop(minHeap))
        print(stack)

        fleets = [-1] * len(position)
        num_fleets = 0
       
        for idx in range(len(position) - 1):
            pos1, spd1 = stack[idx]
            pos2, spd2 = stack[idx + 1]
            print(pos1, pos2, num_fleets)
            print(fleets)
            if self.willCarsMeet(target, -pos1, -pos2, spd1, spd2):
                print("MEET")
                # car1 is in a fleet
                stack[idx + 1] = stack[idx]
                if fleets[idx] != -1:
                    fleets[idx + 1] = fleets[idx]
                else:
                    fleets[idx] = num_fleets
                    fleets[idx+1] = num_fleets
                    num_fleets += 1
            else:
                print("DONT MEET")
                # car1 is in a fleet
                if fleets[idx] != -1:
                    fleets[idx+1] = fleets[idx] + 1
                    num_fleets += 1
                else:
                    fleets[idx] = num_fleets
                    fleets[idx+1] = num_fleets + 1
                    num_fleets += 2
            print(pos1, pos2, num_fleets)
            print(fleets)
            print()

        return num_fleets

    def willCarsMeet(self, target: int, pos1: int, pos2: int, spd1: int, spd2: int) -> bool:
        if pos1 == pos2: return True
        
        # same speed cars never reach unless start at the same pos
        if spd1 == spd2: return False

        n = (pos1 - pos2) / (spd2 - spd1)
        return n > 0 and (pos1 + n*spd1) <= target
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # create a min heap: key is temperature and value is its index
        stack = []
        res = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, stackIdx =  stack.pop()
                res[stackIdx] = index - stackIdx
               
            stack.append([temp, index])

        return res
## One stack only
## Runtime O(1)
## Space O(n)
class MinStack:

    def __init__(self):
        self.aStack = []
        self.minVal = float('inf')

    def push(self, val: int) -> None:
        if not self.aStack:
            self.aStack.append(0)
            self.minVal = val
        else:
            self.aStack.append(val - self.minVal)
            if val < self.minVal:
                self.minVal = val

    def pop(self) -> None:
        pop = self.aStack.pop()

        if pop < 0:
            self.minVal = self.minVal - pop

    def top(self) -> int:
        top = self.aStack[-1]

        if top > 0:
            return top + self.minVal
        else:
            return self.minVal

    def getMin(self) -> int:
        return self.minVal
    
    def printStat(self) -> None:
        print("stack", self.aStack)
        print()

minStack = MinStack()
minStack.push(-1)
minStack.push(3)
minStack.push(-4)
minStack.printStat()
print(minStack.getMin())
minStack.printStat()

print(minStack.pop())
minStack.printStat()

print(minStack.getMin())
minStack.printStat()

print(minStack.top())
minStack.printStat()

# import heapq
# class MinStack:

#     def __init__(self):
#         self.aStack = []
#         self.minHeap = []

#     def push(self, val: int) -> None:
#         self.aStack.append(val)
#         heapq.heappush(self.minHeap, val)

#     def pop(self) -> None:
#         self.minHeap.remove(self.aStack.pop())

#     def top(self) -> int:
#         return self.aStack[-1]

#     def getMin(self) -> int:
#         print(self.minHeap)
#         return heapq.nsmallest(1, self.minHeap)[0]
    
#     def printStat(self) -> None:
#         print("stack", self.aStack)
#         print("minHeap", self.minHeap)
#         print()

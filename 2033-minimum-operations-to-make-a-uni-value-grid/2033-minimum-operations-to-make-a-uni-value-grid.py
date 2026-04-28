class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        res = 0 
        for row in grid:
            for num in row:
                arr.append(num)

        arr.sort()
        length = len(arr)
        final = arr[length//2]
        for number in arr:
            if number %x != final %x :
                return -1 
            res += abs(final-number) //x 
        return res        
class Solution:
    def trailingZeroes(self, n: int) -> int:
        num1, num2 = 0, 0
        count1, count2 = 0, 0
        # for i in range(1, n+1):
        #     num1 = i
        #     while(num1 % 2 is 0):
        #         num1 = num1 // 2
        #         count1 += 1
        for i in range(1, n+1):
            num2 = i
            while(num2 % 5 is 0):
                num2 = num2 // 5
                count2 += 1
        return count2 # 5의 개수가 2의 개수보다 항상 적다. 
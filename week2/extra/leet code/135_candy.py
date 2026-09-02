# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         n = len(ratings)
#         compare = [[0 for _ in range(n)] for _ in range(n)]
#         for i in range(n):
#             for j in range(n):
#                 if ratings[i] > ratings[j] :
#                     compare[i][j] = 1
#                 else : compare[i][j] = 0

#         result = []
#         for i in range(n):
#             result[i] = sum(compare[i])
            


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1: return 1

        result = []
        cursor = 0
        starting_point = 0
        end_point = 0
        while(cursor < n - 1):
            if cursor > n - 1 : break
        # case 1 : 시작부터 증가
            starting_point = cursor
            while(ratings[cursor] < ratings[cursor+1]):
                cursor += 1
            # end_point = cursor
                if cursor > n-1 : break # 배열 끝에 도달하면 cursor값 가지고 반복 종료
            value = 1
            # starting_point = cursor
            for i in range(starting_point, cursor+1):
                result[i] = value
                value += 1
                # cursor = end_point
            while(ratings[cursor] > ratings[cursor+1]):
                cursor += 1
                if cursor >= n-1 : break
            # end_point = cursor
            value = 1
            for i in range(cursor, starting_point + 1, -1):
                if i == starting_point:
                    if ratings[i] > value:
                        pass
                else: 
                    result[i] = value
                    value += 1
                # cursor = end_point
        return result

                    

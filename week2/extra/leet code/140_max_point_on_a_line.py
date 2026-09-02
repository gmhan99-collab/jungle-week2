class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
# 브루트 포스?
# 한 점에서 다른 모든 점의 기울기를 계산하는 방식
# 일차방정식 만들어서 점을 대입해가지고 만들기 or y증가량/x증가량0
        n = len(points)
        results = []
        if n == 1: return 1
        check = {}
        for i in range(n-1):
            start = points[i]
            for j in range(i+1 ,n):
                target = points[j]
                dy = target[1] - start[1]
                dx = target[0] - start[0]
                if dx == 0: slope = "vertical"
                else : slope = dy / dx

                if check.get(slope) == None:
                    check[slope] = 2
                else : check[slope] = check[slope] + 1
            results.append(max(check.values()))
            check = {}
        return max(results)

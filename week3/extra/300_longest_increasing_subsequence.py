class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # min보다는 큰데, MAX보다는 작은걸 세면 될거같은데?
        # min = 처음 상승이 시작되는 구간의 값
        # max = min의 바로 다음 값으로 놓고 계산 시작

        # 새로운 값이 min보다 작으면, 지금까지의 개수를 list에 넣고 새로 계산 시작 + 하던거 이어서
        # DP와는 거리가 멀다 + 위 방법은 내림차순된 배열을 입력하면 O(n) 시간복잡도
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1 , dp[i])
        return max(dp)

        pass

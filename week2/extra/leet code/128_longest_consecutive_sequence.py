class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 파이썬의 dict는 내부적으로 해시 테이블로 구현되어 있다.
        s = set(nums)
        n = len(s)
        # dict_list = dict(zip(s,s))
        if not nums:
            return 0
        answers = []
        for x in s:
            if x - 1 in s : continue
            else:
                count = 1
                while(True) :
                    if x + count not in s: 
                        answers.append(count)
                        break
                    else :
                        count += 1
        return max(answers)

        
        # cursor = min(s)
        # s.remove(cursor)
        # count = 1

        # answers = []
        # for _ in range(n):
        #     if len(s) == 0: 
        #         answers.append(count)
        #         break
        #     if cursor + 1 in s:
        #         s.remove(cursor+1)
        #         count += 1
        #         cursor += 1
        #     else:
        #         answers.append(count)
        #         count = 1
        #         cursor = min(s)
        #         s.remove(cursor)
        # return max(answers)

        
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

  
        dummy = ListNode()
        dummy.next = head # dummy를 만들어서 head 왼편에 붙임 dummy -> 1 -> 2 -> ... -> tail 이런 식

        before = dummy # 회전 후에 링크를 복구해 주기 위한 변수


        # 처음엔 head에서 시작

        while(True):
            check = before
            for _ in range(k): # k개 만큼 확인해서
                if check.next is None: # 확인하다가 끝을 만나면 k개보다 적으므로
                    return dummy.next # 결과 return 하고 종료
                check = check.next 

            # 노드 뒤집는 과정
            start = before.next
            prev = None
            curr = start

            for _ in range(k):
                next_node = curr.next # 다음 노드 좌표 임시 저장
                curr.next = prev # 현재 노드의 화살표를 이전 노드로 연결
                prev = curr # prev와 curr을 우측으로 한 칸씩 이동
                curr = next_node
                
            # 앞뒤 연결    
            before.next = prev
            start.next = curr

            # 다음 그룹으로 이동
            before = start

        return dummy.next

    
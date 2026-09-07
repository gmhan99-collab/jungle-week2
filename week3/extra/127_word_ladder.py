class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:


        """
        1. 그래프를 그린다
        1 - 1. 근데 인접한 노드를 어떻게 구별하지?
        1 - 2. 한"글자"만 차이난다는 점을 이용해야 한다.
            집합 이용? 왜 집합? 중복제거에는 용이하다. discard도 용이하다.
        """
        wordset = set(wordList)
        if endWord not in wordset: return 0
        wordset.discard(beginWord)

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        def neighbor(word):
            for i in range(len(word)):
                for letter in alphabet:
                    newWords = word[:i] + letter + word[i+1:]
                    if newWords in wordset:
                        yield newWords

        queue = []
        queue.append(beginWord)
        distance = 1

        while queue:

            for _ in range(len(queue)):
                curr = queue.pop(0)
                for word in neighbor(curr):
                    if word == endWord:
                        return distance + 1
                    
                    wordset.discard(word)
                    queue.append(word)
                    
            distance += 1  

        else: return 0
        
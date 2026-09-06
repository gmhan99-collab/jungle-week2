class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cursor = self.root
        for i in range(len(word)):
            if word[i] not in cursor.children : # 문자가 없을 때
                cursor.children[word[i]] = Node()

            cursor = cursor.children[word[i]]
        cursor.isend = True
    def search(self, word: str) -> bool:
        cursor = self.root
        for i in range(len(word)):
            # if i == len(word) - 1 and cursor.isend is True: 
            #    return True
            if word[i] not in cursor.children:
               return False
            cursor = cursor.children[word[i]]
        return cursor.isend

    def startsWith(self, prefix: str) -> bool:
        cursor = self.root
        for i in range(len(prefix)):
            if prefix[i] not in cursor.children: return False

            cursor = cursor.children[prefix[i]]
        return True

class Node:
    def __init__(self):
        self.children = {}
        self.isend = False

    def __iter__(self):
        return self

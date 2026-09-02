class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        strlen = len(word)

        directions = [
            (1, 0), # 아래
            (-1, 0),#위
            (0, 1), #오른쪽
            (0, -1) #왼쪽
        ]


        def find_word(n, i, j): # arr 매개변수까지는 필요 없을것 같음
            # 0 <= i, j <= row, col 지켜져야 함
            # arr[i][j]와 인접한 문자 찾기
            # if n >= len(word)-1: return True
            # if (i + 1) >= row : pass
            # elif(board[i+1][j] == word[n+1]):
            #     if((i+1, j) not in seen):
            #         seen.append((i+1, j))
            #         find_word(n+1, i+1, j)
            # if (i - 1) < 0 : pass
            # elif(board[i-1][j] == word[n+1]):
            #     if((i-1, j) not in seen):
            #         seen.append((i-1, j))
            #         find_word(n+1, i-1, j)
            # if (j + 1) >= col : pass
            # elif(board[i][j+1] == word[n+1]):
            #     if((i, j+1) not in seen):
            #         seen.append((i, j+1))
            #         find_word(n+1, i, j+1)
            # if (j - 1) < 0 : pass
            # elif(board[i][j-1] == word[n+1]):
            #     if((i , j-1) not in seen):
            #         seen.append((i, j-1))
            #         find_word(n+1, i, j-1)

            if n == len(word)-1 : return True
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if(0 <= ni < row and 0 <= nj < col):
                    if(board[ni][nj] == word[n+1]):
                        if (ni, nj) not in seen :
                            seen.add((ni,nj))
                            if find_word(n+1, ni, nj): return True
                            seen.remove((ni,nj))
            return False


        seen = set()
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    seen = set()
                # if(len(seen) == len(word)): return True
                    seen.add((i,j))
                    if(find_word(0, i, j)): return True
            # 탈출조건 어떻게 넣어야하지?
            print(len(seen), len(word))
        return False
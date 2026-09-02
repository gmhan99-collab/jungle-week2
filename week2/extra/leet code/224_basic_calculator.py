class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        queue = "" # 숫자 만들기용
        postfix = [] # 후위표기식 #사실 큐임
 
        calc = [] #스택
        s = s.replace(" ", "")

        for i in range(len(s)):
            if s[i].isdecimal() :
                queue += s[i]
            else:
                if len(queue) != 0 :
                    postfix.append(int(queue))
                    queue = ""
                if s[i] == '-' and (i == 0 or s[i-1]== '('): #부호 체크
                    if s[i+1] == '(':
                        queue += '0'
                        stack.append('-')
                    else:
                        queue += s[i]
                    continue
                if s[i] == ')' :
                    # print(stack)
                    while(stack[-1] != '('): #여기 고쳐야될듯
                        # if stack[-1] == '+' or stack[-1] == '-':
                        postfix.append(stack.pop())
                    stack.pop()
                    continue
                # if len(stack) > 0 and (stack[-1] == '+' or stack[-1] == '-'):
                #     postfix.append(stack.pop())
                # stack.append(s[i])
                if s[i] == '+' or s[i] == '-' :
                    while stack and stack[-1] != '(':
                        postfix.append(stack.pop())
                    stack.append(s[i])
                if s[i] == '(':
                    stack.append(s[i])
                    continue


        if(len(queue) != 0): postfix.append(int(queue))
        while(len(stack)) : 
            postfix.append(stack.pop())
        # print(postfix)
        for i in range(len(postfix)):
            if isinstance(postfix[i], int) :
                calc.append(postfix[i])
            else:
                n1, n2 = calc.pop(), calc.pop()
                if postfix[i] == '+':
                    calc.append(n2 + n1)
                else :
                    calc.append(n2 - n1)
        return calc[0]
class Postfix():
    def __init__(self):
        self.list = []
        self.count = 0
    
    def push(self, data):
        self.list.append(data)
        self.count += 1
    
    def pop(self):
        self.count -=1
        return self.list.pop()
  
     
    def printall(self):
        for i in range(self.count):
            print(self.list[i])
        print('count : ', self.count)

    def evaluate(self, p):
        digitPreviously = False
        for i in range(len(p)):
            ch = p[i]
            if ch.isdigit():
                if digitPreviously:
                    tmp = self.pop()
                    tmp = 10 * tmp + (ord(ch) - ord('0'))
                    self.push(tmp)
                else:
                    self.push(ord(ch)-ord('0'))
                    digitPreviously = True
            elif self.isOperator(ch):
                self.push(self.operation(self.pop(), self.pop(), ch))
                digitPreviously = False
            else:
                digitPreviously = False
        return self.pop()

    def  isOperator(self, ch):
        return(ch == '+' or ch == '-' or ch == '*' or ch == '/')


    def operation(self, opr2:int, opr1:int, ch) -> int: # 연산하기
        return {'+': opr1 + opr2, '-': opr1 - opr2, '*': opr1 * opr2, '/': opr1 // opr2}[ch]



p1 = Postfix()
str = '700 3 47 + 6 * - 4 /'
ans = p1.evaluate(str)

print(str)
print(ans)
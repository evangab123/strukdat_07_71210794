class PrefixConverter:
    def __init__(self):
        self.stackList = []
# method untuk menambahkan data baru 
    def push(self,data):
        self.stackList.append(data)
# method untuk melihat data paling atas
    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return "Isi Stack Kosong"
# method untuk menghapus data palin atas
    def pop(self):
        if self.stackList:
            data = self.stackList.pop(-1)
            return data
        else:
            return "Isi Stack Kosong"
    def is_empty(self):
        return len(self.stackList) == 0

    def printAll(self):
        if self.is_empty():
            print("Empty!")
        else:
            return self.stackList

    def cekValidExpression(self,expression):
        for char in expression:
            if char == '(' or char == ')':
                return False
            else:
                return True
            

    def infixToPrefix(self,expression):
        Operators = set(['+', '-', '*', '/', '^'])
        Priority = {'+':1, '-':1, '*':2, '/':2, '^':3}
        if self.cekValidExpression(expression) == True:
            for i in range(len(expression)):
                if i not in Operators:
                    self.push(i)
                else:
                    while Priority(expression[i]) <= Priority(self.peek()):
                        op1 = self.peek()
                        self.pop()
                        op2 = self.peek()
                        self.pop()
                        temp = op2+op1
                        self.push(temp)
            return self.printAll()
        else:
            x = 'Expresi Infix yang anda masukan tidak valid!!'
            return x
            

# Test Case
if __name__ == '__main__':
    expresi1 = PrefixConverter()
    print(expresi1.infixToPrefix("1+2+3*4/2-1"))
    print(expresi1.infixToPrefix("("))
    print(expresi1.infixToPrefix("(1+2)*3"))
    print(expresi1.infixToPrefix("20 * 3 - 10 + 289"))
    print(expresi1.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))
from sys import stdin
        
class Editor() :
    def __init__(self, sentence) :
        self.cursor = 0
        self.place = 0
        self.left = sentence
        self.right = []
        
    def L(self) :
        if self.left :
            self.right.append(self.left.pop())
        
    def D(self) :
        if self.right :
            self.left.append(self.right.pop())
            
    def B(self) :
        if self.left :
            self.left.pop()
                
    def P(self, plus) :
        self.left.append(plus)


#--실행--
input = stdin.readline
editor = Editor(list(input().replace("\n", "")))
num = int(input())

for idx in range(num) :
    a =  input().split()
    
    if len(a) == 1 :
        val1 = a[0]
        getattr(editor, val1)()
        
    else :
        val1, val2 = a
        getattr(editor, val1)(val2)

print("".join(editor.left + editor.right[::-1]))

"""
From book: Data Structures and Algorithms with Python
Developed by: Kent D. Lee and Steve Hubbard
Chapter: 4.5. - The Stack Datatype
Where to buy the book: https://www.amazon.com.br/dp/3319130714
Source code: https://kentdlee.github.io/CS2Plus/build/html/chap4/chap4.html#the-stack-datatype
"""

class Stack:
    def __init__(self):
        self.items = []
        
    def pop(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to pop an empty stack")
        
        topIdx = len(self.items)-1
        item = self.items[topIdx]
        del self.items[topIdx]
        return item
    
    def push(self,item):
        self.items.append(item)
        
    def top(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to get top of empty stack")
        
        topIdx = len(self.items)-1
        return self.items[topIdx]
    
    def isEmpty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []
    
def main():
    s = Stack()
    items = list(range(10))
    items2 = []
    
    for k in items:
        s.push(k)
        
    if s.top() == 9:
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")
        
    while not s.isEmpty():
        items2.append(s.pop())

    items2.reverse()
    
    if items2 != items:
        print("Test 2 Failed")
    else:
        print("Test 2 Passed")
        
    try:
        s.pop()
        print("Test 3 Failed")
        
    except RuntimeError:
        print("Test 3 Passed")
    except:
        print("Test 3 Failed")

    try:
        s.top()
        print("Test 4 Failed")
        
    except RuntimeError:
        print("Test 4 Passed")
    except:
        print("Test 4 Failed")   
        
if __name__=="__main__":
    main()
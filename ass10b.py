# create a class B and define a constructor with one argument (integer type) which will show object created define a method show() which will show class B  Object having val1

class B :
    def __init__(self, n):
        self.n = n
        print("Object Created")
    
    def Show(self) :
        print("Value of object B: " , self.n)
        
B = B(5) 
B.Show()
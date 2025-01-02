# class C inheriting the class B. Take two arguments which initializes class B object with 1st argument, show class c object created and all the values 

class B :
    def __init__(self, var1):
        print("Parent Class created")
        self.var1 = var1

    def show(self) :
        print(self.var1)

class C (B):
    def __init__(self, var1, var2):
        print("Child Class created")
        self.var2 = var2
        super().__init__(var1)

    def show(self) :
        super().show()
        print(self.var1, self.var2)

c = C(1, 2)

c.show()
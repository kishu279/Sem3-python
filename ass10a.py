# define the constructor , destructor and a method and print suitable statement of thier creation and deletion 

class A :
    def __init__(self):
        print("Object Created")
        self.run
    
    def run(self) :
        print("Program method is called")
    
    def __del__(self):
        print("object destroyed")


obj = A()
obj.run()
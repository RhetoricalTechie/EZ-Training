class sample:
    
    def __init__(self):
        self.a = input("Enter the string: ")
        self.b = int(input("Enter the 1st integer:"))
        self.c = int(input("Enter the 2nd integer:"))
       
    def method(self):
        self.a = self.a[::-1]
        print("The reverse of the string is: ", self.a)
        self.b = self.b*self.b
        print("The square of the 1st integer is: ", self.b)
        
    def display_results(self):
        print("The length of the string is:", len(self.a))       
        print("The modular division of two integers is: ", self.b%self.c)
        
obj = sample()
obj.method()
obj.display_results()



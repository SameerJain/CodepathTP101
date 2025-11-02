class problem_1:

    def print_function(self,input):
        print(input)   
    
    def solve(self):
        print(f"Expected: Hello World")
        print(f"Actual: ",end= "")
        self.print_function('Hello World')
        

problem_1().solve()

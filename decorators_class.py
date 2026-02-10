class CountCalls:
    def __init__(self,func):
        self.func=func
        self.num=0

    def __call__(self,*args,**kwargs):
        self.num+=1
        print(f"Function is being called:{self.num} times")
        return self.func(*args,**kwargs)

@CountCalls
def print_name(name):
    print(name)

print_name("Sanchit")
print_name("Sharvari")
print_name("Yash")
print_name("Gawde")

## Class decorator with argument DOING SAME STUFF AS FUNCTION!

class RepeatExec:
    def __init__(self,x):
        self.x=x
        self.result_list = []

    def __call__(self,func):
        def wrapper(*args,**kwargs):
            for _ in range(self.x):
                self.result_list.append(func(*args,**kwargs))
            return self.result_list
        return wrapper

@RepeatExec(x=10)
def print_name(name):
    print(name)

print_name("SUMAN")
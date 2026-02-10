# DECORATORS give extra functionality
# to normal functions without having to add any code to existing function

# Q: Prior to running of the function we need to log that the function is being executed and after execution
# we should log that function execution is complete

import functools
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        logger.debug("FUNCTION IS BEING EXECUTED!")
        result = func(*args,**kwargs)
        logger.debug("FUNCTION EXECUTION IS COMPLETED")
        return result
    return wrapper

@my_decorator
def audit_input_calculator(x):
    return x*5

result=audit_input_calculator(8)
print(result)

## FUNCTION DECORATOR WITH ARGUMENT

# Q: we need to write a function decorator which can repeat execution of function as per the user input times
# When we have requirement to get input for decorator always do function inside function like this
def repeat(num_times):
    def decorator_repeat(func): #Function inside Function
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = []
            for _ in range(num_times):
                logger.debug("FUNCTION IS BEING EXECUTED!")
                result.append(func(*args, **kwargs))
            return result #all the results are appended to result list and then sent to the user

        return wrapper

    return decorator_repeat


@repeat(num_times=4)
def greet(name):
    return f"Hello:{name}"


# calling function
# Thus now even if greet is returning just string due to the decorator
# its returning list of string
# thats the usage of decorator w/o updating any existing code of the function we are able
# to change the functionality of the function

result=greet("sanchit")
for r in result:
    print(r)

# CONTEXT MANAGER: Tools for resource management they allow to allocate
# and release resource precisely when we want to

# WRITING TO A FILE:
# FULL BLOW CODE
file = open('file.txt','w')
try:
    file.write("sometODO")
finally:
    file.close()

# USING CONTEXT MANAGER: (DONT HAVE TO DO MUCH IN THIS CASE)
with open('file.txt','w') as f:
    f.write("HELLO WORLD")

# WRITING CONTEXT MANAGER USING CLASS
# __enter__ and __exit__ magic method are responsible for context manager!
class ManagedFile:
    def __init__(self,file_name):
        print('init')
        self.file_name=file_name

    def __enter__(self):
        print('enter')
        self.file = open(self.file_name,'w')
        return self.file # Returns file object

    def __exit__(self,exc_type,exc_value,exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None: # if theres some excpetion # exc_type will have some value
            print('Exception has been handled!')
        return True # __exit__ always returns true if evveything is good

with ManagedFile('file.txt') as f:
    f.write('Hello')




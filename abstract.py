from abc import ABC, abstractmethod

class Stack(ABC):
    # Abstract method of an abstract class.
    @abstractmethod
    def tech():
        print("I am a techie")
    
    # Non abstract method of an abstract class.
    def stack():
       print("I am a fullstack developer")  

    def get_stack():
        Stack.get_stack()   


# Subclass of an abstract class
class Frontend(Stack):
    def tech(self):
        # Attempting to create an object for abstract class(Stack)
        # to access non abstract methods throws an error because 
        # an abstract class cannot be instantiated.
        stk = Stack()
        stk.get_stack()

# Subclass of an abstract class
class Backend(Stack):
    def Technology(self):
        # Attempting to create an object for abstract child class(Backend)
        # to access non abstract methods throws an error because
        # an abstract class cannot be instantiated.
        back = Backend()
        # Calling the abstract method.
        back.tech() 
        # Calling the non abstract method.
        back.get_stack()

front = Frontend().tech()
back = Backend().get_stack()

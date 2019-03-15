####Abstract method
##from abc import ABC,abstractmethod
##class vehicle(ABC):
##    def __init__(self):
##        pass
##    @abstractmethod
##    def drive(self):
##        pass
##class car(vehicle):
##    def color(self):
##        print('red')
##    def drive(self):
##        pass
##c=car()
##c.color()

##Var=20/0
##print(Var)  

##try:
##    var=10/0
##    print(var)
##except:
##    print("sorry")

##try:
##    print(9+'a')
##except ZeroDivisionError:
##    print("sorry")
##except TypeError as a:
##    print(a)
##except:
##    Print("Oops")

##try:
##    print(9+'a')
##except ZeroDivisionError as a:
##    print(a)
##except TypeError as a:
##    print(a)
##except:
##    Print("Oops")

##try:
##    print('a'+b)
##except (ZeroDivisionError,TypeError )as a:
##    print(a)
##except:
##    print("Oops")
##else:
##    print("my python")
##finally:
##    print("Program Executed")

##try:
##    var=10
##    if var>5:
##        raise TypeError("my raise error")
##except TypeError as a:
##    print(a)

##class OwnError(Exception):
##    pass
##try:
##    var=20
##    if var>5:
##        raise OwnError()
##except OwnError:
##    print("user defined error")

class OwnError(Exception):
    var="user error"
  
try:
    c=OwnError
    print(c.var)
        raise OwnError()
except OwnError:
    print("user defined error")

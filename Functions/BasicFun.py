#creating a function
def myfun():
    print("Hello World")

myfun()  #function call


#Arguments
def my_func(fname):
    print(fname,"Sayyad")

my_func("Hameed")   #passing arguments
my_func("Akmal")


#No.of arguments
def Arguments(fname, lname):
    print(fname + " " + lname)

Arguments("Rebelstar", "Prabhas")


#Default parameter value    
def my_fun(country = "India"):
    print("I am from",country)

my_fun()
my_fun("Brazil")    #updated arguments
my_fun("Sweden")    
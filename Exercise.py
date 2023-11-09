#(i) Using Create a user class, write properties i.e. name, age, location. 
#(ii) create a new instance of the user class (a new object). 
# (iii) Access the user's name and age (iv). Create a function for the function for the user class that prints the user's location.
# (v) print the user's location using the function.

#Solution
#(i)
class User:
    def __init__(user, name, age, location):
        user.name = name
        user.age = age
        user.location = location

#(ii)
user1 = User("Bridget", 25, "New York")

#(iii)
user_name = user1.name
user_age = user1.age
print(f"User's Name: {user_name}")
print(f"User's Age: {user_age}")

#(iv)
class User:
    def __init__(user, name, age, location):
        user.name = name
        user.age = age
        user.location = location

    def print_location(user):
        print(f"User's Location: {user.location}")

#(v)

user2 = User("Brandy", 25, "Los Angeles")
user2.print_location()

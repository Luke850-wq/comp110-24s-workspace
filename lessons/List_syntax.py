"""Demonstrate Basic List Syntax"""

# Initialize an empty list
#<list name>: list[<item type>] = list()
grocery_list: list[str] = list() #<- list constructor
grocery_list: list[str] = [] # <- literal
#<list name>.appen(<item>)
grocery_list.append("bananas") #added to end of list
grocery_list.append("bread")
grocery_list.append("milk")

print("after appending: ")
print(grocery_list)

#create an already populated list
grocery_list2: list[str] = ["bananas", "milk", "bread"]
print("Populated list")
print(grocery_list2)

#Indexing
print("print first element of string")
print(grocery_list[0])
#grocery_list: list[str] = 

#Modifying by Index
print("before change:")
print(grocery_list)
grocery_list[1] = "almond milk"
print("after change")
print(grocery_list)

#You can have duplicates

#Measuring length
print(len(grocery_list))

#Remove an item from a list
grocery_list.pop(1)
print(grocery_list)

#Function name :display
#Parameter: list[str]
#Return: nothing
#Print out the list!
def display(word:list[str]):
    print(word)

display(grocery_list)

#Create a list:
#Name: create
# Parameters: str and str
#RV: list[str]
# Put both parameters into list and return that list

def create(a: str, b: str) -> list[str]:
    my_list: list[str] = [a, b]
    return my_list

 
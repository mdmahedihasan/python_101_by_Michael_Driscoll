empty_list = []
empty_tuple = ()
empty_string = "something"
nothing = None

if empty_list == []:
    print("It's an empty list")
if empty_tuple:
    print("It's not an empty tuple")
if not empty_string:
    print("This is an empty string")
if not nothing:
    print("Then it's nothing")
if empty_string == "":
    print("This is an empty string")

print(empty_list == empty_string)
print(empty_string == nothing)
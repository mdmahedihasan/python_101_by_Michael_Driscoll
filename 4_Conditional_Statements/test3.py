# Python 3 code
value = input("How much is that doggy in the window?")
value = int(value)

if value < 10:
    print("That was a great deal!")
elif 10 <= value <= 20:
    print("I'll still pay that...")
else:
    print("Wow! that's too much")
# ask the for their name
username = input("what is your name? ")
# ask the user for their favourite number ( integer )
fav_num = int(input("what is you favourite number? "))
# Double , halve and a square the user favourite number
double = fav_num * 2
halve = fav_num / 2
square = fav_num * fav_num

# greet the user

print (f"\nhi {username}, your favourite number is{fav_num} ")

# output the results of  doubling, halving and
print (f"double {fav_num} is {double}.")
print (f"half{fav_num} is {halve}")
print (f"{fav_num} squared is {square}")
print()
print("have a nice day")
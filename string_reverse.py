from audioop import reverse


print("======++++++ String Reverse Code ++++++======")
print("\n")

#This code uses Recursion function to operate

expected_string = input("Type the string you want to reverse: \n").lower()

def reverse_value(value):
    if len(value) == 0:
        return value
    else:
        reversal = reverse_value(value[1:]) + value[0]
        return f"{reversal}"

related = reverse_value(expected_string)
print(related)
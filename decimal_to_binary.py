print("======++++++ Binary Conversion Code ++++++======")
print("\n")

number_to_convert = int (input("Enter your number:  "))


def convert_decimal(num):
    """This will take in a number to convert
        And will return back the numbers in its binary format
    """
    binary = []
    while num !=0:
        if num % 2 == 0:
            num = num /2
            binary.insert(0,0)
        else:
            num = (num -1) / 2
            binary.insert(0,1)
    return binary

bin_check = convert_decimal(number_to_convert)
print(bin_check)

print("\n")
print("======++++++ Binary Conversion Process(Using Recursion) ++++++======")
print("\n")


def decimal_convert_process(num):
    bin_holder = []
    if num >= 1:
        decimal_convert_process(num//2)
        print(num//2, num%2, sep="|")
        # bin_holder.append(str(num%2))
        # print(bin_holder[::-1])

decimal_convert_process(number_to_convert)


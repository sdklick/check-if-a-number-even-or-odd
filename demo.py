# check if a number even or odd

userinput = int(input('please enter one number : '))

if userinput > 0:
    if userinput % 2 == 0:
        print(userinput, "is a Even Number")
    else:
        print(userinput, 'is a Odd Number')
elif userinput == 0:
    print('you enter zero number')
else:
    print('please enter positive number')

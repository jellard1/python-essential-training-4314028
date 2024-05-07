def factorial(num):
    if type(num) == int and num>0:
        if num == 1:
            return 1
        return num * factorial(num - 1)
    else:
        return('not a positive integer')

factorial(input)
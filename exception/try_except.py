try:
    
    value = int(input('enter a numper : '))
    print(value)
    result = 10/0
    
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid error")

print('success')

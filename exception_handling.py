def convert_to_integer(value):
    try:
        result = int(value)
        print(f'Conversion of value is {result}')
    except ValueError:
        print ('conversion failed. Please enter a valid integer')
    finally:
        print ('closing any open resorces.')

# User input
user_input = input("enter a number ot convert to integer: ")

# convert number
convert_to_integer(user_input)
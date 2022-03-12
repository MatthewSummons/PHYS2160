# Radix_Implementation.py
#Find decimal equivalent of radix base-r numbers
#Shaheer Ziya


from ctypes.wintypes import PINT
from unicodedata import digit

from numpy import negative


def get_num_input(enquiry, error_text):
    ''' Obatin non-zero float from user, continue asking until a valid input is obtained
        Takes in enquiy which is displayed to user with a new line added to it (by default)
        Outputs error_text if a non-zero float is not input '''
    while True:
        try:
            num = float(input(enquiry + "\n"))
            if num == 0: raise Exception ##
            break
        except:
            print(error_text)
            print() # new line for formatting
    return num


def convert_to_decimal(num, base):
    '''Converts base-r numbers to decimal
        Takes in the radix_num its base and split the num into parts to 
            the left and to the right of the decimal point
        Loops through each and returns a decimal (float) value'''
    num_str = str(num).split('.')
    positive_digits = num_str[0][::-1]
    negative_digits = num_str[1][::-1]
    
    num_sum = 0
    radix = 1

    for pos_digit in positive_digits:
        num_sum += (int(pos_digit) * radix)
        radix  *= base
    
    radix = 1 / base
    for neg_digit in negative_digits:
        num_sum += (int(neg_digit) * radix)
        radix /= base
    
    return num_sum



def main():
    # getInput(radix_number, base)
    base = get_num_input('What base is your number?',
                         'Please enter a valid integer base')
    radix_num = get_num_input('What is your number', 
                        "Please enter a valid number with no spaces")

    #convert to decimal
    num = convert_to_decimal(radix_num, base)
    print(f"The decimal equivalent of {radix_num} base {base} is {num}")


main()
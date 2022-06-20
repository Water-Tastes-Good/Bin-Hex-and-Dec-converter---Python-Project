# Binary Converter

# This program inputs decimal or hexadecimal digits and returns binary, or the other way around. 

global type_dict; 

type_dict = {0: 'decimal' , 1: 'hexadecimal', 2: 'binary'}


# all working functions (for now lol)


class user_input():
    def __init__(self):
        
        print('value created!')

    def get_result_type(self):
        while True:
            
            try:
                val_type = int(input("What do you want back? (0 for decimal, 1 for hexadecimal, or 2 for binary: "))
            except:
                print('Error invalid value type. Please enter valid value type: ')
                continue
            return type_dict[val_type]

    def test_for_errors(self,user_in, val_type):
        
        if val_type == 'decimal': 
            try:
                convert = float(user_in)
            except:
                return True

        # does not work for hexadecimals yet
        elif val_type == 'hexadecimal': 
            # how tf lol (research hexdecimals)    
            return False

        elif val_type == 'binary': 
            for char in user_in: 
                if char not in ['1', '0']:
                    return True

    def get_value(self,val_type, requested_value_type):

        while True:
            
            val = input('Enter your {} value: '.format(val_type))
            
            # test for error, doesn't work for hexdecimals
            if self.test_for_errors(val, val_type):
                print('Please enter a valid {}. If you want to change the value type you entered, type in CHANGE TO, and then 0,1, or 2 (0 for decimal, 1 for hexadecimal, or 2 for binary.'.format(val_type))
                continue
            return val

    def all_to_decimal(self,x, x_type):

        if x_type == 'decimal':
            return float(x)
        elif x_type == 'binary':
            # Problem: floats cannot be directly converted to binary, and converting it as an int leads to data loss
            # losing data can change the message. 
            # Solution: treat the binary as string rather than a numeric type
                # Steps: 
                # 1. Create a list of integers and manifest a list from it
                # 2. Iterate through the dictionary and assign a consequent bit to each element
                # 4. Finally, iterate through it again, but turning the indexs into exponents for 2
                # 5. Add them together
                # Thereis your binary value 

                # Reverse the process to decode to decimal values again
            base2PVs = [y for y in range(0, 64)]
            dictBinaryPVs = {}
            total_amount = 0
            # creation of dictionary of binary place values
            for iterator in base2PVs:
                basePV = 2**iterator
                try:
                    dictBinaryPVs[2**iterator] = int(x[::-1][iterator])
                    total_amount += int(x[::-1][iterator]) * basePV 
                except:
                    dictBinaryPVs[2**iterator] = 0
                        
            # print(dictBinaryPVs)
            return total_amount
        elif x_type == 'hexadecimal':
            print(x_type)
            # convert hexadecimal to decimal
            deciHexa =  0

            base16PVs = [y for y in range(0, 64)]
            potentialValues = [y for y in range(0, 10)] + ['A', 'B', 'C', 'D', 'E', 'F']

            dictBinaryPVs = {}
            total_amount = 0
            # creation of dictionary of binary place values

            # iterates through PLACE VALUES (note it is just 0 - 63 right now)
            for basePV in base16PVs:
                # Problem: that's not the x-place value, its the potentialValues
                # Its useless because the potV and placeV aren't supposed to be 
                # paired up like this. 

                # Plan: Assign the input into PV's 1-64
                # iterate through the created dictionary, 
                # make each value an exponent of 16, create variable forming
                # total amount
                
                # Updating dictionary to include numeric digits to 
                # corresponding values of x, basically creating a digital
                # place value table and getting the total amount from there

                # the x[::-1] is there because the computer "writes" the PVs from 
                # left to right (computers are left handed?!?! lol)
                try: 
                    if x[::-1][basePV] in potentialValues[10:]:
                        letter_x_value = potentialValues.index(x[::-1][basePV])
                        total_amount += letter_x_value * 16**basePV
                except IndexError:
                    dictBinaryPVs[basePV] = 0
                try: 
                    dictBinaryPVs[basePV] = int(x[::-1][basePV])
                    total_amount += dictBinaryPVs[basePV] * 16**basePV
                except:
                    dictBinaryPVs[basePV] = 0
                deciHexa = total_amount

            return deciHexa
        else: 
            print("Error occured. Please restart program.")

    def get_value_type(self):
        while True:
            try:
                val_type = int(input("What is the value type of the digit you want to convert? (0 for decimal, 1 for hexadecimal, or 2 for binary: "))
            except:
                print('Error invalid value type. Please enter valid value type: ')
                continue
            return type_dict[val_type]

    def all_to_bin(self, x, x_type):

        if x_type == 'decimal':
            return bin(x)
        elif x_type == 'hexadecimal':
            return self.hex_to_bin(x)
        elif x_type == 'binary':
            return x

    def all_to_hex(self, x, x_type):
        decimal = self.all_to_decimal(x, x_type)
        return self.dec_to_hex(decimal)

    def hex_to_bin(self,x):
        #each hex digit has 0-G values, starting after 10 values turn to letters A-G
        # each base is 16^n

        decimal = self.all_to_decimal(x, 'hexadecimal')
        binary_version = bin(decimal)
        return binary_version

    def dec_to_hex(self,x):
        return hex(int(x))
         
        
# val type (decimal, hexdecimal, or binary) & result type (same options)

        
# returns a string value
user_in = user_input()
print(user_in)


value_type = user_in.get_value_type()

requested_value_type = user_in.get_result_type()

value = user_in.get_value(value_type, requested_value_type)

if requested_value_type == 'decimal':
    answer = user_in.all_to_decimal(value, value_type)
elif requested_value_type == 'hexadecimal':
    answer = user_in.all_to_hex(value, value_type)
elif requested_value_type == 'binary':
    answer = user_in.all_to_bin(value, value_type)

print(answer)
# print('The number you entered is {} and of type {}. You want to change the value type to {}.'.format(initial_number, val_type, result_value_type))




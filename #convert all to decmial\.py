# convert all to decmial, starting with decimal and ending with binary

def all_to_decimal(x, x_type):

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

def hex_to_bin(x):
    #each hex digit has 0-G values, starting after 10 values turn to letters A-G
    # each base is 16^n
    decimal = all_to_decimal(x, 'hexadecimal')
    binary_version = bin(decimal)

    return binary_version

def dec_to_hex(x):
    return hex(int(x))

# def bin_to_hex(x)
     

test_case = dec_to_hex(input('Enter a decimal: '))
# testCase = all_to_decimal(input('Enter a decimal, hexadecimal, or binary value: '), input('What is it? (decimal, hexadecimal, or binary): '))
print(test_case)
# convert to decimal
# then convert to desired results
# rn we're just making the functions, don't complicate it
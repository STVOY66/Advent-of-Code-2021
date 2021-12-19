import sys

input_file = open('input.txt', 'r')
input_lines = input_file.readlines()
for index in range(0, len(input_lines)):
    input_lines[index] = input_lines[index].strip()
bitLength = len(input_lines[0])

def part_one():
    most_common = 0
    num_one = 0
    num_zero = 0
    gamma = ''
    epsilon = ''
    for index in range(bitLength):
        for val in input_lines:
            if val[index] == '0': num_zero += 1
            elif val[index] == '1': num_one += 1
        if num_zero > num_one:
            gamma += '0'
            epsilon += '1'
        elif num_one > num_zero:
            gamma += '1'
            epsilon += '0'
        num_one, num_zero = 0, 0
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print("gamma:{}, epsilon:{}, power con:{}".format(gamma,epsilon,gamma*epsilon))

def genRecur(inputList, type, index = 0):
    if(len(inputList) == 1):
        return inputList[0]
    else:
        #print(inputList)
        out = []
        num0 = 0
        num1 = 0
        commonVal = 0
        #find common value
        for bitStr in inputList:
            if(bitStr[index] == '0'): num0 += 1
            elif(bitStr[index] == '1'): num1 += 1
        #print('num0: {}, num1:{}'.format(num0, num1))
        if(max(num0, num1) == num0): commonVal = '0'
        elif(max(num0, num1) == num1): commonVal = '1'
        if(num0 == num1): commonVal = '-1'
        #print(commonVal)
        #build output list
        match type.lower():
            case 'oxy':
                for bitStr in inputList:
                    #keep bitStrings with most common value (0 or 1)
                    if(bitStr[index] == commonVal):
                        out.append(bitStr)
                    #if both values are equal in frequency, keep stings with a 1 in this pos
                    elif(commonVal == '-1' and bitStr[index] == '1'):
                        out.append(bitStr)
            case 'co2':
                for bitStr in inputList:
                    #keep bitStrings with least common value (0 or 1)
                    if(bitStr[index] != commonVal and commonVal != '-1'):
                        out.append(bitStr)
                    #if both values are equal in frequency, keep stings with a 0 in this pos
                    elif(commonVal == '-1' and bitStr[index] == '0'):
                        out.append(bitStr)
        #print(out)
        return genRecur(out, type, index + 1)

def part_two():
    print("Life Support Rating: {}".format(int(genRecur(input_lines, 'oxy', 0), 2)*int(genRecur(input_lines, 'co2', 0), 2)))

if len(sys.argv) == 1:
    print("Please enter \'1\' for part one or \'2\' for part two")
elif len(sys.argv) == 2:
    if int(sys.argv[1]) == 1:
        part_one()
    elif int(sys.argv[1]) == 2:
        part_two()
    else:
        print("Invalid input, please enter \'1\' for part one or \'2\' for part two")
else:
    print("Too many arguments passed, please enter \'1\' for part one or \'2\' for part two")
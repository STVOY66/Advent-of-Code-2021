import sys

input_file = open('input.txt', 'r')
input_lines = input_file.readlines()
for index in range(0, len(input_lines)):
    input_lines[index] = input_lines[index].strip()

#processing inputs by converting each line into [x1,y1,x2,y2]
for i in range(len(input_lines)):
    input_lines[i] = input_lines[i].split(' ')
    input_lines[i][0] = input_lines[i][0].split(',')
    input_lines[i][2] = input_lines[i][2].split(',')
    input_lines[i] = [int(input_lines[i][0][0]), int(input_lines[i][0][1]), int(input_lines[i][2][0]), int(input_lines[i][2][1])]

#finds the intersection of two line segments given the coordinates of
#their endpoints in [x1, y1, x2, y2] format
def findIntersectPoint(line1, line2):
    x1, y1, x2, y2 = line1[0], line1[1], line1[2], line1[3]
    x3, y3, x4, y4 = line2[0], line2[1], line2[2], line2[3]
    denominator = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
    if denominator != 0:
        t = ((x1 - x3)*(y3 - y4) - (y1 - y3)*(x3 - x4))/denominator
        u = ((x1 - x3)*(y1 - y2) - (y1 - y3)*(x1 - x2))/denominator
        if 0 <= u <= 1 and 0 <= t <= 1:
            return (x1 + t*(x2 - x1), y1 + t*(y2 - y1))
    return -1

#function returns a list of points that intersect with the input line and every line in the input list
def findInterPointsinList(inLine, inList):
    workList = [] + inList
    output = []
    while inLine in workList:
        workList.remove(inLine)
    for line in workList:
        newPoint = findIntersectPoint(inLine, line)
        if newPoint != -1:
            output.append(newPoint)
    return output

def part1():
    #get vertical and horizontal lines
    workList = []
    output = []
    #creates a list of every horizontal and vertical line
    for line in input_lines:
        if line[0] == line[2] or line[1] == line[3]:
            workList.append(line)
    for line in workList:
        line_intersec = findInterPointsinList(line, workList)
        output = list(set().union(output, line_intersec))
    print('input: {}\nvertical and horizontal lines: {}\noutput: {}'.format(len(input_lines), len(workList), len(output)))


def part2():
    pass

if len(sys.argv) == 1:
    print("Please enter \'1\' for part one or \'2\' for part two")
elif len(sys.argv) == 2:
    if int(sys.argv[1]) == 1:
        part1()
    elif int(sys.argv[1]) == 2:
        part2()
    else:
        print("Invalid input, please enter \'1\' for part one or \'2\' for part two")
else:
    print("Too many arguments passed, please enter \'1\' for part one or \'2\' for part two")
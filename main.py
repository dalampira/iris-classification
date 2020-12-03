
#opening the file and storing the data
with open('iris.data') as fp:
    dataset = [line.split(",") for line in fp.readlines() if line]

#omitting the last empty line
dataset.pop()

#omitting the new-line character
for row in dataset:
    category = row[4]
    category = category[:-1]
    row[4] = category


#normalizing the data
def normalize():
    xMax = [float(dataset[0][0]), float(dataset[0][1]), float(dataset[0][2]), float(dataset[0][3])]
    xMin = [float(dataset[0][0]), float(dataset[0][1]), float(dataset[0][2]), float(dataset[0][3])]
    for row in dataset:
        for value in range(0,4):
            if xMax[value]< float(row[value]):
                xMax[value] = float(row[value])
            if xMin[value] > float(row[value]):
                xMin[value] = float(row[value])
    for row in dataset:
        for i in range(0, 4):
           x = float(row[i])
           y = (x - xMin[i]) / (xMax[i] - xMin[i])
           row[i] = y

normalize()

#defining the membership of each x
def membership(x):
    if x == 0.0:
        list_row = [1, 0, 0]
        return list_row
    if 0.0 < x < 0.6:
        ys = (-1/0.6)*x + 1
        ym = (1/0.6)*x
        list_row = [ys, ym, 0]
        return list_row
    if x == 0.6:
        list_row = [0, 1, 0]
        return list_row
    if 0.6 < x < 1.0:
        ym = (-1/0.4)*x + (1/0.4)
        yl = (1/0.4)*x - (0.6/0.4)
        list_row = [0,ym,yl]
        return list_row
    if x == 1.0:
        list_row = [0,0,1]
        return list_row


dataset2 = list()

#creating a new dataset with the membership of each x and the flower category
for row in dataset:
    row_list = list()
    for index in range(0,4):
        z = membership(row[index])
        row_list.append(z)
    row_list.append(row[4])
    dataset2.append(row_list)


#defining the FIRST rule
def rule1(line):
    rule = list()
    x1=max(line[0][0],line[0][2])
    rule.append(x1)
    x2 = max(line[1][1],line[1][2])
    rule.append(x2)
    x3 = max(line[2][1],line[2][2])
    rule.append(x3)
    x4 = line[3][1]
    rule.append(x4)
    return min(rule)

#defining the SECOND rule
def rule2(line):
    rule = list()
    x3 = max(line[2][0],line[2][1])
    rule.append(x3)
    x4 = line[3][0]
    rule.append(x4)
    return min(rule)

#defining the THIRD rule
def rule3(line):
    rule = list()
    x2 = max(line[1][0],line[1][1])
    rule.append(x2)
    x3 = line[2][2]
    rule.append(x3)
    x4 = line[3][2]
    rule.append(x4)
    return min(rule)

#defining the FOURTH rule
def rule4(line):
    rule = list()
    x1 = line[0][1]
    rule.append(x1)
    x2 = max(line[1][0],line[1][1])
    rule.append(x2)
    x3 = line[2][0]
    rule.append(x3)
    x4 = line[3][2]
    rule.append(x4)
    return min(rule)

#classifying the data based on the 4 rules
def classify(line):
    rule_list = list()
    r1 = rule1(line)
    r2 = rule2(line)
    r3 = rule3(line)
    r4 = rule4(line)
    rule_list.append(r1)
    rule_list.append(r2)
    rule_list.append(r3)
    rule_list.append(r4)
    maxRule = max(rule_list)
    if maxRule == r1:
        return "Iris-versicolor"
    if maxRule == r2:
        return "Iris-setosa"
    if maxRule == r3:
        return "Iris-virginica"
    else:
        return "Iris-versicolor"


score = 0

for row in dataset2:
    point = classify(row)
    if point == row[4]:
        score = score +1



print("The score is: " + str(score) + " out of 150")

print("The accuracy is: "+ str((score/150)*100))
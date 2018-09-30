file = open("practice_outliers_net_worths.pkl", 'r')

line = file.readline()
l = []

while line:
    line = file.readline()
    l.append(line)

li = []
se = []
li.append(float(l[0][1:len(l[0])-2]))
for line in l[1:len(l)-2]:
    se.append(line)
    print(line[2:len(line)-2])
    print(float(line[2:len(line)-2]))
    li.append(float(line[2:len(line)-2]))

print se

import cPickle

new_file = open("new_file.pkl","w")
cPickle.dump(li,new_file)
new_file.close()


new_file = open("new_file.pkl","r")
lis = cPickle.load(new_file)
new_file.close()
print lis
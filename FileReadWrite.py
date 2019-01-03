# FileReadWrite
# This is a test for reading and writing to a file

file = open("testfile.txt", "r")
p1 = file.readline()
data1 = p1.split("#")
p2 = file.readline(1)
data2 = p2.split("#")
p3 = file.readline(1)
data3 = p2.split("#")

print(data1[0])
amount = int(data1[1]) + 12
print(amount) 

file.close()

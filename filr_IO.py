f = open("F:\python-practice\learn_python\demo.txt", "r")
data = f.read()

print(data)

# readline() is used for print line by line data
# line1 = f.readline()
# print(line1)

f.close()

file = open("sample.txt", "a")
file.write("\nI want to learn Django")
file.close

with open("sample.txt", "a") as f:
    f.write("\nabc")
    f.close
    
# delete /remove file
import os
os.remove("F:\python-practice\sample.txt")
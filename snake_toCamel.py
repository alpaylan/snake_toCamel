import sys

if(len(sys.argv) > 1):
    input_file_name = sys.argv[1]
else:
    input_file_name = input("Please Provide File Name to Convert")


f = open(input_file_name, "r")

file_content = f.read()

converted_file_content = ""

i = 0

while(i < len(file_content)):
    if file_content[i] == "_":
        i+=1
        converted_file_content += (file_content[i].upper())
    else:
        converted_file_content += (file_content[i])

    i += 1

f.close()

f = open(input_file_name, "w")

f.write(converted_file_content)

from pathlib import Path

result = list(Path(".\..\BUILD").rglob("*.[o]"))
f = open("..\..\object_list.txt", "w")

for file in result :
    print(file)
    f.write(str(file))
    f.write('\n')

f.close()
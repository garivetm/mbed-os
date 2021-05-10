from pathlib import Path

result = list(Path("mbed-os/BUILD").rglob("*.[o]"))
f = open("object_list.txt", "w")

for file in result :
    print(file)
    f.write("\"${workspace_loc:/${ProjName}/" + str(file) + "}\"\n")

f.close()
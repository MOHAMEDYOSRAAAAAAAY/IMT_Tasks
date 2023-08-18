import subprocess

com = "gcc 1.c -o a.exe  "
output = subprocess.getoutput(com)
print(output)
print(output)
print(output)
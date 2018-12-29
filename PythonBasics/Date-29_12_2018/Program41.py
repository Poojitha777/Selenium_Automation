#WAP for the I/O error

# filename=open("Python.txt",'r')
# filename.write("Hello Bengaluru")

try:
    f=open("Python.txt",'r')
    f.write("Hello Bengaluru")
except Exception as q:
    print(type(q))
# r - read
# w - write if file not exit its create and write 
# a- append create exit file if not exist and append data to file

# r+ = read and write
# w+ = write and read

# rb = read binary
# wb = write binary


# with syntax 

# with open("file.txt", "r") as f:
#     pass

# without sntax:

# f = open("file.txt", "r")
# pass
# f.close()

def write_file(content):
    with open("file.txt", "w") as f:
        f.write(content)

def read_file():
    with open("file.txt", "r") as f:
        return f.read()

def append_file(content):
    with open("file.txt", "a") as f:
        f.write(content)

def read_binary_file():
    with open("file.txt", "rb") as f:
        return f.read()





#parameters
def add(a, b):
    c=a + b
    print(c)
#arguments
add(2, 3)

def greeting():
    return "Hello, World!"
def name(name):
    wish = greeting()
    return f"{wish} {name}"
print(name("John"))
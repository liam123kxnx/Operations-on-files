Jesse = open("abc.txt","r")
print(Jesse.read())
Jesse.close()

Jesse = open("abc.txt","r")
print(Jesse.readline())
print(Jesse.readline())
print(Jesse.readline())
Jesse.close()

Jesse = open("abc.txt","r")
print(Jesse.readlines())
Jesse.close()
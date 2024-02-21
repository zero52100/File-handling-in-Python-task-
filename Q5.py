file_name=input("Enter the file to copy")
file_name1=input("Enter the file copied to ")
try:
    with open(file_name,'r')as file:
        output=file.read()
        with open(file_name1,'w')as copyfile:
            copyfile.write(output)
        with open(file_name1,'r')as copyfile:
            print(copyfile.read())
except FileNotFoundError:
    print(f"The file '{file_name}' not found.")
            
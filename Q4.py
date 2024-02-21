file_name=input("Enter the file ")
try:
    with open(file_name,'r')as file:
        output=""
        for i in file:
            output += i
        print(output)
except FileNotFoundError:
    print(f"The file '{file_name}' not found.")
            
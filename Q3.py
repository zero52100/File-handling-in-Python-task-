file_name = input("Enter  file name: ")  
try:
    text = (input("Enter enter the text to append "))
    with open(file_name, 'a+') as f:
        f.write(' ' + text)
    with open(file_name, 'r') as f:
        print(f.read())
except FileNotFoundError:
    print(f"The file '{file_name}' not found.") 



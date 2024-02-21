"""
Saved file with text is sample"""

file_name = input("Enter the file name: ")  
try:
    with open(file_name, "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print(f"The file '{file_name}' not found.") 



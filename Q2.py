file_name = input("Enter  file name: ")  
try:
    num = int(input("Enter the number of lines to print: "))
    with open(file_name, 'r') as f:
        current_line = 1
        for i in f:
            if current_line <= num:
                print(i.strip()) 
            current_line += 1
except FileNotFoundError:
    print(f"The file '{file_name}' not found.") 
except ValueError:
    print("Invalid input. Please enter a valid number.")


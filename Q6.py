file_name = input("Enter the file name: ")
num = int(input("Enter the line number to print from the file: "))

try:
    with open(file_name, 'r') as file:
        present = 1
        for line in file:
            if present == num:
                print(line)
                break
            present += 1
        else:
            print(f"The file '{file_name}' has fewer lines than {num}.")
except FileNotFoundError:
    print(f"The file '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

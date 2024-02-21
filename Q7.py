file_name = input("Enter the file name: ")

try:
    file = open(file_name, 'r')
    print(f"Is the file closed? {file.closed}")
    text=input(f"Do you want to close the {file_name} file  ? please type yes or no :")
    if text=='yes':
            file.close()
            print(f"The file {file_name}  is  closed")
    else:
         print(f"The file  is not closed")
         
    
except FileNotFoundError:
    print(f"The file '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

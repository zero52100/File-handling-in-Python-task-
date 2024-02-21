file_name = input("Enter the file name to create: ")
letters_per_line = int(input("Enter the number of letters per line: "))
with open(file_name, 'w') as file:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(0, len(alphabet), letters_per_line):
            line = alphabet[i:i + letters_per_line]
            file.write(line + '\n')
        print(f"The file '{file_name}' has been created successfully.")
with open(file_name,'r')as file:
       print(file.read())


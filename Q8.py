def list_to_file(file_name, data):
    try:
        with open(file_name, 'w') as f:
            for item in data:
                f.write(item + '\n')
        print(f"The list has been added to the file '{file_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

limit = int(input("Enter the number of elements in the list: "))
list1 = []
for i in range(limit):
    value = input(f"Enter element {i + 1}: ")
    list1.append(value)

file_name = input("Enter the file name: ")
list_to_file(file_name, list1)

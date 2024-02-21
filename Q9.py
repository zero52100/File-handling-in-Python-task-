
file_name = input("Enter the text file name: ")
def count_words(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            content = content.replace(',', ' ')
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return f"The file '{file_name}' not found."
    except Exception as e:
        return f"An error occurred: {e}"

result = count_words(file_name)

if isinstance(result, int):
    print(f"The file '{file_name}' contains {result} words.")
else:
    print(result)


file_name = input("Enter the file name: ")  
try:
    num=int(input("Enter the numer of line to print"))
    f=open(file_name,'r')
    current_line=1
    for i in f:
        if current_line<=num:
            print(i)
        current_line +=1
except FileNotFoundError:
    print(f"The file '{file_name}' not found.") 


File_Name='output.txt'
file_1=open(File_Name,'r+')

a=input("Enter text to write in file: ")
file_1.write(a+"\n")
print("Data successfully written to the",File_Name)
file_1.close()

file_1=open(File_Name,'a')
b=input("Enter additional text to append: ")
file_1.write(b)
print("\nData successfully appended")
file_1.close()

file_1=open(File_Name,'r+')
Read=file_1.read()
print("Final content of",File_Name,":")
print(Read)
file_1.close()

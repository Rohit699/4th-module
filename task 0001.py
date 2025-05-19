try:
    FileName='newfile.txt'

    file_1=open(FileName,'r')


    first_Line = file_1.readlines(1)
    second_Line = file_1.readlines(2)
    print("Reading content:")
    print("Line 1:", first_Line)
    print("Line 2:", second_Line)



    file_1.close()
except FileNotFoundError:
    print("The File",FileName,"does not exist")
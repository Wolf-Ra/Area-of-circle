fileName=str(input("Enter the File Name : "))
extension=str(input("Enter the extension format (.py , .xlx , .c) : "))
print("The input File Name is ",fileName+extension)
if (extension ==".py"):
    print("The extension of the file is Python")
elif (extension ==".c"):
    print("The extension of the file is C")
elif (extension ==".xlx"):
    print("The extension of the file is Excel")
newFile=input("new file: ")
new_File_Size=int(input("size in bytes desired: "))
new_File_Size=int((new_File_Size/5)+.5)
with open(newFile, 'a') as out:
  for i in range(1,new_File_Size,1):
    out.write("Word")
    if i%10==0:
      out.write("\n")

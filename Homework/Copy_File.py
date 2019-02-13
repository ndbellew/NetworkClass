#!/usr/bin/env python3

def main():
  CurrentFile = input("Please input the name of the file to copy\n")
  NumOfBytes = int(input("Please input the rate at which the file will be copied (bytes)\n"))
  NewFile = input("input the new file, dont forget to add /home/usr to the start\n")

  with open(CurrentFile, 'rb') as Read_File, open(NewFile, 'wb') as Target:
    maxdata = Read_File.read()
    data = Read_File.read(NumOfBytes)
    if data>maxdata:
      NumOfBytes = NumOfBytes/4
      data = Read_File.read(NumOfBytes)
    while data<maxdata:
      data+=Read_File.read(NumOfBytes)
      Target.write(data)
    ReadFile.close()
    Target.close()


if __name__ == "__main__":
  main()

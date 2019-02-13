
def main():
    filename = input("input file name\n")
    numOfBytes =int( input("Input number of bytes to pass through\n"))
    newFile=input("input new file name\n")
    quality = int(input("input the quality, the higher the number the better\n"))
    quality*=100
    with open(filename, "rb") as f:
      b = f.read(numOfBytes)
      for i in range(1,quality,1):
        if i>1:
          b += f.read(numOfBytes)
        if b == b'':break
        with open(newFile, 'wb') as nf:
          nf.write(b)
          nf.close()
    f.close()

main()

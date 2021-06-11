
def avacado():
    fileName=input("Enter the name of your file: ");
    file= open(fileName,'r');

    numberOfWords =0;

    for line in file:
        words = line.split()
        numberOfWords = numberOfWords+len(words)

    print(numberOfWords);


avacado();



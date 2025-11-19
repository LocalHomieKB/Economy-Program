file = open("/resources/books.txt", "r")

#your code goes here

cont = file.read()
for line in file:
    line = line.strip
    #this took me an hour to find FML^
    print(line[0] + str(len(line)))



file.close
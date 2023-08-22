# Print 1st 2 charatcters from each word in a String 


lineList = input('Enter a line: ').split(' ')


for i in lineList:
    print(str(i)[0:2])
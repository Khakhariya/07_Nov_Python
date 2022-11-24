for i in range (3):
    spelling = input ("enter the spelling : ")
    add = "ing"

    if spelling [-3:] == 'ing' :
        x = spelling.replace ('ing','ly')
        print (x)

    elif len(spelling) >= 3:
        spelling = spelling  + add
        print (spelling)

    else :
        print(spelling)
def encrypt(plaintext,shift, whichOneToAdd):  
  
    ordarray = []
    new = ""
    #shift word using alphabet
    for char in plaintext:
        n = ord(char) + shift
        if n > 122:
            n = n - 26
        new += chr(n)

    #get the ASCII values for each letter
    for i in new:
        ordarray.append(ord(i))
        
    #mess up frequency precidtion
    for z in range(0, len(ordarray)):
        if z%whichOneToAdd:
            ordarray[z] = ordarray[z] + 1
            
    #input the messed up prediction into an equation to produce big numbers
    #this will make it harder to brute force since the hacker needs the inverse equation to brute force
    for r in range(0, len(ordarray)):
        ordarray[r] = 2*(ordarray[r])**3 + 2.5*(ordarray[r])**2 + 9*(ordarray[r])-5

    return ordarray


def encrypt(plaintext,shift, whichOneToAdd):  
  
    ordarray = []
    new = ""
    for char in plaintext:
        n = ord(char) + shift
        if n > 122:
            n = n - 26
        new += chr(n)

    for i in new:
        ordarray.append(ord(i))

    for z in range(1, len(ordarray)):
        if z%whichOneToAdd:
            ordarray[z] = ordarray[z] + 1

    for r in range(1, len(ordarray)):
        ordarray[r] = 



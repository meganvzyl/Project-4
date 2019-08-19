# Introduction to Programming, Task 25: Capstone Project IV 
# Megan van Zyl, 12/05/2019
# Python code to identify and return the amino acid sequence of DNA

import math  #importing math function
#x = input("Please enter a DNA sequence: ").upper()

def translate(x): #function to translate DNA sequence to amino acid sequence
    #x = input("Please enter a DNA sequence: ").upper()
    code = [] #create new list
    if len(x) % 3 == 0: #create new string for every third character
        x = x
    else:
        x = x[0:(math.floor(len(x)/3)*3)] #if string is not divisable by three, do not take into account the left over string

    for i in range(0,len(x),3):
            code.append(x[i:i +3]) #add the new strings of characters to the list
    #print (code)
    y = [] #create a new list for the amino acids
    #z = [] 
    dicna = {"ATT":"I","ATC":"I","ATA":"I","CTT":"L","CTC":"L","CTA":"L","CTG":"L", "TTA":"L", "TTG":"L", "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V", "TTT":"F", "TTC":"F", "ATG":"M"} #dictionary for the DNA sequences
    #dicnal = {"ATT":"Isoleucine","ATC":"Isoleucine","ATA":"Isoleucine","CTT":"Leucine","CTC":"Leucine","CTA":"Leucine","CTG":"Leucine", "TTA":"Leucine", "TTG":"Leucine", "GTT":"Valine", "GTC":"Valine", "GTA":"Valine", "GTG":"Valine", "TTT":"Phenylalanine", "TTC":"Phenylalanine", "ATG":"Methionine"}
    for i in code:
        if i in dicna: #if the DNA sequence is in the dictionary add the amino acid to the new list y
            y.append(dicna[i])
            #z.append(dicnal[i])
        else:
            y.append("X") #if the DNA sequence is not in the dictionary, add "X" to the list
            #z.append("Other")
            
    for i in y: #take out spaces to make one long string to print the amino acid sequence
        print(i, end="")
    #print(y)


#translate(x)

def mutate(): #function to change an item in a text file
    with open("DNA.txt","r") as f: #open the text file to read
        newline=[] #new list for replaced string
        for word in f.readlines():        
            newline.append(word.replace("a","A"))  #Replace a with A.

    n = open("normalDNA.txt","w") #open a new text file to write the replaced version
    for line in newline:
        n.writelines(line) 

    with open("DNA.txt","r") as f: #open the text file to read
        newline=[] #new list for replaced string
        for word in f.readlines():        
            newline.append(word.replace("a","T")) #Replace a with T.
           
    m = open("mutatedDNA.txt","w") #open a new text file to write the replaced version
    for line in newline:
        m.writelines(line)
        
    f.close() #close the text files
    n.close()
    m.close()
mutate()

def txtTranslate(): #function to translate the text to the amino acid sequence
    n = open("normalDNA.txt","r") #open text file to read
    textn = n.read() 
    print ("normalDNA: ")
    translate(textn) #use function to translate text to amino acid sequence
    
    m = open("mutatedDNA.txt","r") #open text file to read
    textm = m.read()
    print ("\nmutatedDNA: ")
    translate(textm) #use function to translate text to amino acid sequence

    n.close() #close the programs
    m.close()
txtTranslate()

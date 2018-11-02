# Naam:
# Datum:
# Versie:

# Voel je vrij om de variabelen/functies andere namen te geven als je die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.

def main():
    list1, list2= getsequence()
    sequence =is_DNA()
    cut(list1, list2, sequence)
#bestand = "alpaca.fa" # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
#"""
#Hier onder vind je de aanroep van de lees_inhoud functie, die gebruikt maakt van de bestand variabele als argument.
#De resultaten van de functie, de lijst met headers en de lijst met sequenties, sla je op deze manier op in twee losse resultaten.
#"""
#headers, seqs = lees_inhoud(bestand) 
        
#zoekwoord = input("Geef een zoekwoord op: ")

# schrijf hier de rest van de code nodig om de aanroepen te doen
    
    
#def lees_inhoud(bestands_naam):
    #bestand = open(bestands_naam)
    #headers = []
    #seqs = []

def getsequence():
    list1=[]
    list2=[]
    for line in open ("enzymen.txt"):
        line.replace("^","")
        line.split()
        list1.append(line[0])
        list2.append(line[1])
    return list1, list2
    
#"""
#Schrijf hier je eigen code die het bestand inleest en deze splitst in headers en sequenties.
#Lever twee lijsten op:
#    - headers = [] met daarin alle headers
#    - seqs = [] met daarin alle sequenties behorend bij de headers
#Hieronder vind je de return nodig om deze twee lijsten op te leveren
#"""
     
#return headers, seqs

    
def is_DNA():
    sequence=""
    file="sequence.txt"
    for i in open (file):
        if i.startswith(">")==False:
            sequence+=i.rstrip()
    validDNA="ATCG"
    is_DNA=all(c in validDNA for c in sequence.upper())
    print(is_dna)
    return sequence

#"""
#Deze functie bepaald of de sequentie (een element uit seqs) DNA is.
#Indien ja, return True
#Zo niet, return False
#"""
    

def cut(list1, list2, sequence):
    for k in range(len(list2)):
        if list2[k] in sequence:
            print ("cuts with",list1[k], "in the position", sequence.index(list2[k]), sequence)
        if seq in normaal_seq and sikkel_seq:
            if seq not in sikkel_seq:
                print(enzyme, seq, "is the restriction endonucleases (enzyme) that cuts in only one of the two sequences.")
# """
# Bij deze functie kan je een deel van de code die je de afgelopen 2 afvinkopdrachten geschreven hebt herbruiken

#Deze functie bepaald of een restrictie enzym in de sequentie (een element uit seqs) knipt.
#Hiervoor mag je kiezen wat je returnt, of wellicht wil je alleen maar printjes maken.
#    """
       
    
main()

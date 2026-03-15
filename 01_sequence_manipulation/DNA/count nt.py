# taking input
file= input("Enter DNA Sequence:")
with open(file,"r") as f:
    data= f.read().strip()
    
# counting the nucleotides in a sequence
a= data.count('A')
c= data.count('C')
g= data.count('G')
t= data.count('T')

# printing nucleotide count
print(a, c, g, t)
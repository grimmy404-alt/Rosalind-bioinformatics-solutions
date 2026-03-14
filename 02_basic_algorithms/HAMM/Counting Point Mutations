#Reading data
file= input('Enter file name:')
with open(file,"r") as f:
    data= f.read().splitlines()

#separating dna sequence strings
s= data[0]
t= data[1]

#initialising hamming distance counter
dH= 0

#comparing nucleotides and calculating hamming distances
compared_data= zip(s,t)

for (character_s, character_t) in compared_data:
    if character_s!= character_t:
        dH+= 1

print(dH)




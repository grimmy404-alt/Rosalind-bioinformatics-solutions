#Taking user input

s=str(input())

#Reversing the sequence

s_reverse= s[::-1]
s_c=""                      #Storing sata in S_C

#Complementary nucleotide assignment

for nt in s_reverse:
    if nt == 'A':
        s_c+='T'
    elif nt == 'T':
        s_c+='A'
    elif nt == 'G':
        s_c+='C'
    elif nt == 'C':
        s_c+='G'
        
#Printing result

print(s_c)

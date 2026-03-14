# parsing RNA codon table 
file= input("Enter RNA codon table containing file name:")
with open(file,"r") as f:
    rna_data= f.read().split()

# parsing RNA string
file= input("Enter dataset file name:")
with open(file,"r") as f:
    s= f.read().strip()

RNA_codon_table={}

# making RNA codon table dictionary
for i in range(0,len(rna_data),2):
    codon_dict= rna_data[i]
    amino_acid_dict= rna_data[i+1]
    RNA_codon_table[codon_dict]= amino_acid_dict

Amino_acid_sequence= ""

# encoding RNA into amino acid
for i in range(0,len(s),3):
    codon= s[i:i+3]

    amino_acid= RNA_codon_table[codon]

    if amino_acid== "Stop":
        break
    
    Amino_acid_sequence+= amino_acid

print(Amino_acid_sequence)



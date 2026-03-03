# Read FASTA file and split data
file= input('Enter File Name:')
with open(file,"r") as f:
    data= f.read().split(">")

# Build dictionary mapping sequence ID to sequence string
ID= {}

for chunk in data:
    if chunk=="":               
        continue
    lines= chunk.splitlines()   
    id_name= lines[0]
    sequence= "".join(lines[1:])
    ID[id_name]= sequence

# Compute GC content for each sequence
GC_dict= {}

for id_key, dna_seq in ID.items():
    G= dna_seq.count("G")           
    C= dna_seq.count("C")           
    nt= len(dna_seq)                

    GC_content= ((G+C)*100)/nt
    GC_dict[id_key]= GC_content

# Identify sequence with highest GC content
max_GC_content_id= max(GC_dict, key=GC_dict.get)       
max_GC_content= GC_dict[max_GC_content_id]

# Output result
print(max_GC_content_id)
print(f"{max_GC_content:.6f}")      
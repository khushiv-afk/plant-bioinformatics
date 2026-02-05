def read_fasta(filename):
    sequences = {}
    current_gene = ""

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                current_gene = line[1:]
                sequences[current_gene] = ""
            else:
                sequences[current_gene] += line

    return sequences


def gc_content(sequence):
    g = sequence.count('G')
    c = sequence.count('C')
    return ((g + c) / len(sequence)) * 100


fasta_file = "plant_genes.fasta"
genes = read_fasta(fasta_file)

print("GC Content of Plant Genes:\n")

for gene, seq in genes.items():
    gc = gc_content(seq)
    print(gene, ":", round(gc, 2), "%")

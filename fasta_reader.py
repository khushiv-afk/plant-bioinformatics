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


# Example usage
fasta_file = "plant_genes.fasta"
genes = read_fasta(fasta_file)

for gene, seq in genes.items():
    print(gene, ":", seq)

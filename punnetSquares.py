# Punnet Square Solver


def validGeno(prompt):

    while True:
        variable = input(prompt)

        if len(variable) != 2 and len(variable) != 4:
            print("This number of alleles is not supported.")

        elif variable[1].isupper() and not variable[0].isupper():
            print("Please put dominant alleles first (XxYy).")

        elif len(variable) == 4 and (variable[3].isupper() and not variable[2].isupper()):
            print("Please put dominant alleles first (XxYy).")

        else:
            variable = list(variable)
            return variable


def printer(length, row, column, genes):

    print("       ", end="")
    for gene in column:
        print(gene + "     ", end="")
    print()
    print("     ", end="")
    for _ in range(length * 7):
        print("-", end="")
    print()

    start = 0
    end = length
    for _ in range(length):
        print(row[_] + "  |  ", end="")
        for gene in genes[start:end]:
            print(gene + "   ", end="")
        start += length
        end += length
        print()


def rows(genes):
    row = []
    for gene_1 in genes[0:2]:
        for gene_2 in genes[2:4]:
            row.append(gene_1 + gene_2)

    return row


geno_1 = validGeno("First genotype: ")
geno_2 = validGeno("Second genotype: ")


if len(geno_1) == 4:

    # Top row
    top = rows(geno_1)

    # Bottom row
    bottom = rows(geno_2)

    # Crossing top and bottom
    new_genes = []
    for allele in top:
        for trait in bottom:
            new_genes.append(allele[0] + trait[0] + trait[1] + allele[1])

    # Printing
    printer(4, top, bottom, new_genes)

elif len(geno_2) == 2:

    new_genes = []

    # Crossing
    for allele in geno_1:
        for trait in geno_2:
            new_genes.append(allele + trait)

    # Printing
    printer(2, geno_1, geno_2, new_genes)

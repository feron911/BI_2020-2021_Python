def nucleotide_generator(length_of_sequence:int):
    import itertools as itr
    nucleotides = "ATCG"
    for j in range(1, length_of_sequence + 1):
        for i in itr.combinations_with_replacement(nucleotides, j):
            yield "".join(i)

print(list(nucleotide_generator(0)))

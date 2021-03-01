def translation(sequences:str, code_table = "Standard"):
    from Bio.Seq import Seq
    from Bio import SeqIO
    for record in SeqIO.parse(sequences, "fasta"):
        yield Seq.translate(record.seq, code_table)





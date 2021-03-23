class Dna(object):

    '''This class for dna'''

    def __init__(self, sequence, name="dna"):
        if not isinstance(sequence, str):
            raise TypeError ("Object of the class \"Dna\" must be a string")
        if len(sequence) == 0:
            raise TypeError ("Object of the class \"Dna\" must have length more than 1")
        for i in sequence:
            dna_letters = ("A", "a", "G", "g", "C", "c", "T", "t")
            if i not in dna_letters:
                raise TypeError(f"Object of the class \"Dna\" cannot include \"{i}\" symbol")
        self.sequence = sequence
        self.name = name

    def reverse_complement(self):
        rc = ''
        for i in self.sequence:
            rev_comp = {"A": "T", "a": "t", "G": "C", "g": "c", "T": "A", "t":"a", "C":"G", "c":"g"}
            rc += rev_comp[i]
        return Dna(rc)

    def gc_content(self):
        gc = (self.sequence.upper().count('G') + self.sequence.upper().count('C')) / len(self.sequence)
        return f"GC content is {gc}"

    def __iter__(self):
        return self.sequence.__iter__()

    def transcribe(self):
        rev_trans = self.reverse_complement()
        rev_trans_rna = ''
        for i in rev_trans:
            if i == "T":
                rev_trans_rna += 'U'
            elif i == "t":
                rev_trans_rna += 'u'
            else:
                rev_trans_rna += i
        return Rna(rev_trans_rna)

    def __eq__(self, other):
        return self.sequence == other.sequence

class Rna(object):

    '''This class for Rna'''

    def __init__(self, sequence, name="rna"):
        if not isinstance(sequence, str):
            raise TypeError("Object of the class \"Rna\" must be a string")
        if len(sequence) == 0:
            raise TypeError("Object of the class \"Rna\" must have length more than 1")
        for i in sequence:
            rna_letters =  ("A", "a", "G", "g", "C", "c", "U", "u")
            if i not in rna_letters:
                raise TypeError(f"Object of the class \"Rna\" cannot include \"{i}\" symbol")
        self.sequence = sequence
        self.name = name

    def reverse_complement(self):
        rc = ''
        for i in self.sequence:
            rev_comp = {"A": "U", "a": "u", "G": "C", "g": "c", "U": "A", "u": "a", "C": "G", "c": "g"}
            rc += rev_comp[i]
        return Rna(rc)

    def gc_content(self):
        gc = (self.sequence.upper().count('G') + self.sequence.upper().count('C')) / len(self.sequence)
        return f"GC content is {gc}"

    def __iter__(self):
        return self.sequence.__iter__()

    def __eq__(self, other):
        return self.sequence == other.sequence

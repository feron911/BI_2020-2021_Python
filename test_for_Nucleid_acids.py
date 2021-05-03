import unittest
from Nucleic_acids_class import Dna, Rna

class Dna_classTests(unittest.TestCase):

    def test_representation(self):
        rep_test = Dna("ATGC")
        named_rep_test = Dna("ATGC", "named_Dna")
        self.assertEqual((rep_test.name, rep_test.sequence), ("dna", "ATGC"))
        self.assertEqual((named_rep_test.name, named_rep_test.sequence), ("named_Dna", "ATGC"))
        self.assertRaises(TypeError, Dna, "")
        self.assertRaises(TypeError, Dna, 3)
        self.assertRaises(TypeError, Dna, "ATXCG")
        self.assertRaises(TypeError, Dna, "ATUCG")

    def test_gc_content(self):
        zero_test = Dna("AaTt")
        fifty_percent_test = Dna("GcaT")
        one_hundred_test = Dna("GCcg")
        self.assertEqual(zero_test.gc_content(), 0.0)
        self.assertEqual(fifty_percent_test.gc_content(), 0.5)
        self.assertEqual(one_hundred_test.gc_content(), 1.0)

    def test_transcribe(self):
        trans_test = Dna("ATGC")
        self.assertEqual(trans_test.transcribe(), Rna("UACG"))
        self.assertEqual((trans_test.transcribe().sequence, trans_test.transcribe().name), ("UACG", "rna"))


    def test_reverse_complement(self):
        rev_complement_test = Dna("ATGC")
        self.assertEqual(rev_complement_test.reverse_complement(), Dna("TACG"))

    def test_eq(self):
        st_for_eq = "AAAAAA"
        seq_for_eq = Dna("AAAAAA")
        test_named_Dna = Dna("AAAAA", "polyADna")
        self.assertEqual(seq_for_eq == st_for_eq, False)
        self.assertEqual(seq_for_eq == test_named_Dna, False)

class Rna_classTests(unittest.TestCase):

    def test_representation(self):
        rep_test = Rna("AUGC")
        self.assertEqual((rep_test.name, rep_test.sequence), ("rna", "AUGC"))
        self.assertRaises(TypeError, Rna, "")
        self.assertRaises(TypeError, Rna, 3)
        self.assertRaises(TypeError, Dna, "AUXCG")
        self.assertRaises(TypeError, Dna, "AUTCG")

    def test_gc_content(self):
        zero_test = Rna("AAUU")
        fifty_percent_test = Rna("GCAU")
        one_hundred_test = Rna("GCCG")
        self.assertEqual(zero_test.gc_content(), 0.0)
        self.assertEqual(fifty_percent_test.gc_content(), 0.5)
        self.assertEqual(one_hundred_test.gc_content(), 1.0)

    def test_reverse_complement(self):
        rev_complement_test = Rna("AUGC")
        self.assertEqual(rev_complement_test.reverse_complement(), Rna("UACG"))

    def test_eq(self):
        test_str = "AAAAA"
        test_Rna = Rna("AAAAA")
        test_named_Rna = Rna("AAAAA", "polyArna")
        self.assertEqual(test_str == test_Rna, False)
        self.assertEqual(test_Rna == test_named_Rna, False)

if __name__ == '__main__':
    unittest.main()
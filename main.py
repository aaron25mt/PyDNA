translation, rna = {'UUU':'Phe', 'UUC':'Phe', 'UUA':'Leu', 'UUG':'Leu', 'UCU':'Ser', 'UCC':'Ser', 'UCA':'Ser', 'UCG':'Ser', 'UAU':'Tyr', 'UAC':'Tyr', 'AUU':'Ter', 'AUC':'Ter', 'UGU':'Cys', 'UGC':'Cys', 'ACU':'Ter', 'UGG':'Trp', 'CUU':'Leu', 'CUC':'Leu', 'CUA':'Leu', 'CUG':'Leu', 'CCU':'Pro', 'CCC':'Pro', 'CCA':'Pro', 'CCG':'Pro', 'CAU':'His', 'CAC':'His', 'GUU':'Gln', 'GUC':'Gln', 'CGU':'Arg', 'CGC':'Arg', 'CGA':'Arg', 'CGG':'Arg', 'AUU':'Ile', 'AUC':'Ile', 'AUA':'Ile', 'AUG':'Met', 'ACU':'Thr', 'ACC':'Thr', 'ACA':'Thr', 'ACG':'Thr', 'AAU':'Asn', 'AAC':'Asn', 'AAA':'Lys', 'AAG':'Lys', 'AGU':'Ser', 'AGC':'Ser', 'AGA':'Arg', 'AGG':'Arg', 'GUU':'Val', 'GUC':'Val', 'GUA':'Val', 'GUG':'Val', 'GCU':'Ala', 'GCC':'Ala', 'GCA':'Ala', 'GCG':'Ala', 'GAU':'Asp', 'GAC':'Asp', 'GAA':'Glu', 'GAG':'Glu', 'GGU':'Gly', 'GGC':'Gly', 'GGA':'Gly','GGG':'Gly'}, {'a':'u', 'g':'c', 'c':'g', 't':'a'}
def main(dnas):
    for x in dnas:
        print("DNA: %s" % x)
        print("RNA: %s" % dnaToRna(x))
        print("Protein Sequence: %s" % rnaToProtein(dnaToRna(x))[1])
        if(len(rnaToProtein(dnaToRna(x))[0]) > 0):
            print("Unknowns: %s" % rnaToProtein(dnaToRna(x))[0])
        print("")

def dnaToRna(dna):
    newString = ""
    for x in dna:
        newString += rna[x]
    return newString

def rnaToProtein(dna):
    counter, newString, unknowns = 0, "", []
    for x in [dna[i:i+3] for i in range(0, len(dna), 3)]:
        try:
            newString += translation[x.upper()] + "-"
            counter + 3
        except KeyError:
            newString += "(UNKNOWN: %s)-" % x
            unknowns.append(x)
            continue
    return [unknowns, newString[:-1]]

main(['gga', 'ggatcctcacatgagttcagtatataattgtaacagaataaaaaatcaattatgtattcaagttgctagtgtcttaagaggttcacatttttatctaactgattatcacaaaaatacttcgagttacttttcattataattcctgactacacatgaagagactgacacgtaggtgccttacttaggtaggttaagtaatttatccaaaaccacacaatgtagaacctaagctgattcggccatagaaacacaatatgtggtataaatgagacagagggatttctctccttcctatgctgtcagatgaatactgagatagaatatttagttcatctatcacacattaaacgggactttacatttctgtctgttgaagatttgggtgtggggataactcaaggtatcatatccaagggatggatgaaggcaggtgactctaacagaaagggaaaggatgttggcaaggctatgttcatgaaagtatatgtaaaatccacattaagcttctttctgcatgcattggcaatgtttatgaataatgtgtatgtaaaagtgtgctgtatattcaaaagtgtttcatgtgcctaggggtgtcaaatactttgagtttgtaagtatatacttctctgtaatgtgtctgaatatctctatttacttgattctcaataagtaggtatcatagtgaacatctgacaaatgtttgaggaacaatttagtgtttacctattcaccaaaatttattaaatgcctaatctgtatcagatatacaattatctggcgaaatctgtaattcctaatttaaacagctgtgtagcctaattagggataaaggcatgcaaacccataatttgtgtaggttgaaatgagctatagaaaaatgcagtatatttatcagaagtctttagggtcatgaaaaggaatggtcaactgacactgccagggactcatatgtaagagataactaatgtgaagtgactttaaaggagaaattagcagaagttttctttccatgtctcctcatcatgttacaataacggaagagattaaaacaacaaatacatttagacagcaatgtttatc', 'ggatcctc'])
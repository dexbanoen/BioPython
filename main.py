from DNAToolkit import *
import random

randDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(50)])
DNAStr = validateSeq(randDNAStr)

print(f'\nSequence: {DNAStr}\n')
print(f'[1] Sequence Length: {len(DNAStr)}\n')
print(f'[2] Nucleotide Frequency: {countNucFrequency(DNAStr)}\n')
print(f'[3] DNA/RNA Transcription: {transcription(DNAStr)}\n')
print(f'[4] DNA String + Complement + Reverse Complement:\n5\' {DNAStr} 3\'')
print(f'    {"".join(["|" for c in range(len(DNAStr))])}')
print(f'3\' {reverse_complement(DNAStr)[::-1]} 5\' [Complement]')
print(f"5' {reverse_complement(DNAStr)} 3' [Reverse Complement]\n")
print(f'[5] GC Content: {gc_content(DNAStr)}%\n')
print(f'[6] GC Content in Subsection k=5: {gc_content_subset(DNAStr, k=5)}\n')
print(f'[7] Aminoacids Sequence from DNA: {translate_seq(DNAStr, 0)}\n')
print(f'[8] Codon frequency (L): {codon_usage(DNAStr, "L")}\n')
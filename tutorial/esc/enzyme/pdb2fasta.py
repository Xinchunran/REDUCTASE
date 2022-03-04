import sys


if len(sys.argv) <= 1:
    print('usage: python3 pdb2fasta.py .pdb > .fasta')
    exit()


input_file = open(sys.argv[1])

letters ={'ALA':'A', 'VAL':'V', 'PHE':'F', 'PRO':'P', 'MET':'M','ILE':'I',
           'LEU':'L', 'ASP':'D', 'GLU':'E', 'LYS':'K','ARG':'R', 'SER':'S',
           'THR':'T', 'TYR':'Y', 'HIS':'H','CYS':'C', 'ASN':'N', 'GLN':'Q',
           'TRP':'W', 'GLY':'G','MSE':'M',}

name = (sys.argv[1].split('.',1)[0])
name = '>' + name
print(name)

prev = '-1'

for line in input_file:
    toks = line.split()
    if len(toks) < 1:continue
    if toks[0] != 'ATOM': continue
    if toks[5] != prev:
        sys.stdout.write('%c' % letters[toks[3]])
    prev = toks[5]

sys.stdout.write('\n')
input_file.close()




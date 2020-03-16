#!/usr/bin/env python

import sys

infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')

for line in infile:
    x = line.strip().split('/')
    print(x)
    outfile.write("wget"+" "+"-P"+" "+"/scratch/vineis.j/THIOHALO-PAN/"+" "+str("/".join(x[0:9]))+"/"+x[9]+"/"+x[9]+"_genomic.fna.gz"+'\n')
    

#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='''This script takes the output returned from swarmv2.2.2 -w flag, which is a list of lists '\n' containing the sequence ids for each swarm, and converts it into a '\n' ASV count matrix. It will also write a reduced fasta file for the representative nodes if you want to remove swarms below a particular count threshold''')
parser.add_argument('-f' , help = "A list of accession numbers for the genomes you want to recover")
parser.add_argument('-o' , help = "The path to the genome contained in the ncbi server. you can use this as input for the gen-ncbi-wget-commands.py script")
parser.add_argument('-n' , help = "The complete collection of ncbi genomes as a text file. You can find out how to get this file here https://github.com/jvineis/get-ncbi-genomes")
args = parser.parse_args()

outfile = open(args.o, 'w')

ncbi_dict = {}
for line in open(args.n,'r'):
    x = line.strip().split('\t')
    ncbi_dict[x[0]] = x[0:len(x)]


for id in open(args.f, 'r'):
    x = id.strip()
    if x in ncbi_dict.keys():
        outfile.write(ncbi_dict[x][19]+'\n')


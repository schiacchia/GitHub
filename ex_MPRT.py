#!/usr/bin/env python
# Given a list of uniprot id's, returns the amino acide positions of any N-glycosylation motif
from urllib import urlopen
import re

# Read in list of proteins
inFile = open("rosalind_mprt.txt", "rU")
proteins = []
for line in inFile:
    line = line.replace('\n', '')
    proteins.append(line)

# Calls uniprot webAPI, retrieves peptide sequence, matches overlapping
# N-glycosylation motifs, returns amino acid of positions of thes motifs
for protein in proteins:
    url = "http://www.uniprot.org/uniprot/" + protein + "_id.fasta"
    html = urlopen(url)
    html = html.read()
    html = html.split()
    proteinSeq = ""
    for line in html:
        if len(line) > 59:
            proteinSeq += line
    proteinSeq += html[len(html) - 1]

    matches = re.finditer(r'(?=(N[^P][ST][^P]))', proteinSeq)
    results = [int(match.span()[0]) + 1 for match in matches]

    if len(results) > 0:
        results = str(results).strip('[]')
        results = results.replace(',', '')
        print protein
        print results

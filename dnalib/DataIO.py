import numpy as np

from Bio import SeqIO

import re

from Utility import only_atcg




def read_fasta(path, singleton=False):
    '''
    
    '''
    
    label_list = []
    handle = open(path, "rU")
    for record in SeqIO.parse(handle, "fasta"):
        label_list.append(record.description.split('\t')[1].split(';')[-1])
    genus_count = {}
    for label in set(label_list):
        genus_count[label] = label_list.count(label)
    handle.close()
    
    # read in fasta and store each sequences in a list
    fasta_list = []
    label_list = []
    handle = open(path, "rU")
    for record in SeqIO.parse(handle, "fasta"):
        if not singleton:
            if genus_count[record.description.split('\t')[1].split(';')[-1]] > 1:
                fasta_list.append(str(record.seq))
                label_list.append(record.description.split('\t')[1].split(';')[-1])
        else:
            fasta_list.append(str(record.seq))
            label_list.append(record.description.split('\t')[1].split(';')[-1])
    handle.close()
    
    return fasta_list, label_list
    
    
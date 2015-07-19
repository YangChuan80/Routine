def read_fasta():
    f_fasta=open('D:\\Chuan\\Documents\\My Text\\Genbank\\Creatine Kinase.fas', 'rt')
    header=f_fasta.readline()
    sequence=f_fasta.read()
    return header, sequence
    f_fasta.close()
    
if __name__=='__main__':
    header, sequence=read_fasta()
    sequence=sequence.replace('\n','')
    
    print('Header:\n', header)
    print('Sequence:\n', sequence)
    
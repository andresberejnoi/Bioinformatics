'''
    Author: Carlos Andres BErejnoi Bejarano
    Date: 02/21/2016 
'''

DNA_bases_complement = {'A':'T',
                        'T':'A',
                        'C':'G',
                        'G':'C'}
RNA_bases_complement = {'A':'U',
                        'T':'A',
                        'C':'G',
                        'G':'C'}

class DNA(object):
    def __init__(self,seq=''):
        self.seq = [base.upper() for base in seq]               # assumes seq is a string. Everything is stoted in uppercase
        
    
    #
    # Overloaders
    #    
    def __str__(self):
        return ''.join(self.seq)
    
    __repr__ = __str__
    
    #
    # Getters
    #
    def get_complementary(self):
        '''
        Returns the complementary strand of DNA to the one stored in this object
        '''
        comp_strand = DNA([DNA_bases_complement[base] for base in self.seq])           #uses a dictionary to find the correspoding complementary base to each one
       
        return comp_strand
    
    def get_mRNA(self):
        '''
        Returns the mRNA strand of the current one. It may be incorrect.
        '''        
        mRNA = DNA([RNA_bases_complement[base] for base in self.seq])
        return mRNA
        
        
    def get_sequence(self):
        '''
        Returns self.seq as a Python list. This could be changed later.
        '''
        return self.seq
        
    
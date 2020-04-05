import numpy as np

with open('sequences.txt') as file: sequences = file.readlines()

for i in range(len(sequences)): sequences[i] = sequences[i].replace('\n', '')

GAP = -2
MISMATCH = -1
MATCH = +5

class COMPARISON:
    def __init__(self, _SEQ1, _SEQ2):
        self.SEQ1 = _SEQ1
        self.SEQ2 = _SEQ2
        self.SCORING_MATRIX = ""
        self.DIRECTION_MATRIX = ""
        self.SCORE = ""
        self.OUTPUT1 = ""
        self.OUTPUT2 = ""
        
        self.FILL_MATRICES()
        
    def FILL_MATRICES(self) :
        SEQA = self.SEQ1
        SEQB = self.SEQ2
        LENA = len(SEQA)
        LENB = len(SEQB)
        
        scoring_matrix = np.zeros((LENA+1, LENB+1))
        direction_matrix = np.zeros((LENA+1, LENB+1), str)
            
        for i in range(LENA):
            scoring_matrix[(i+1)][0] = scoring_matrix[i][0] + GAP
            direction_matrix[(i+1)][0] = '↑'
            
        for i in range(LENB):
            scoring_matrix[0][(i+1)] = scoring_matrix[0][i] + GAP
            direction_matrix[0][(i+1)] = '←'
        
        for i in range(1, LENA+1):
            for j in range(1, LENB+1):
                VALUE_H = scoring_matrix[i-1][j] + GAP
                VALUE_V = scoring_matrix[i][j-1] + GAP
                VALUE_D = scoring_matrix[i-1][j-1] + MATCH if SEQA[i-1] == SEQB[j-1] else scoring_matrix[i-1][j-1] + MISMATCH
                DIRECTION = ['←', '↑', '↖']
                LIST = [VALUE_H, VALUE_V, VALUE_D]
                INDEX = LIST.index(max(LIST))
                scoring_matrix[i][j] = max(LIST)
                direction_matrix[i][j] = DIRECTION[INDEX]
                
        self.SCORING_MATRIX = scoring_matrix
        self.DIRECTION_MATRIX = direction_matrix


a = COMPARISON(sequences[0], sequences[1])

print(a.DIRECTION_MATRIX) 
print(a.SCORING_MATRIX)
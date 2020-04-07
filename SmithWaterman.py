import numpy as np
np.set_printoptions(edgeitems=10, threshold=1000, linewidth=1000)
#np.set_printoptions(threshold=3000, linewidth=3000)
#If you need to observe matrices every item uncomment above line

GAP = -6

DIAGONAL = 'D'
HORIZONTAL = 'H'
VERTICAL = 'V'

class COST:
    def __init__(self, _FILEREAD):
        self.AA = _FILEREAD[0]
        self.TA = _FILEREAD[1]
        self.TT = _FILEREAD[2]
        self.CA = _FILEREAD[3]
        self.CT = _FILEREAD[4]
        self.CC = _FILEREAD[5]
        self.GA = _FILEREAD[6]
        self.GT = _FILEREAD[7]
        self.GC = _FILEREAD[8]
        self.GG = _FILEREAD[9]

class COMPARISON:
    def __init__(self, _SEQ1, _SEQ2, _COST):
        self.SEQ1 = _SEQ1
        self.SEQ2 = _SEQ2
        self.SCORING_MATRIX = ""
        self.DIRECTION_MATRIX = ""
        self.OUTPUT1 = []
        self.OUTPUT2 = []
        self.SCORE = 0
        self.COST = _COST
        self.SEARCH_I = 0
        self.SEARCH_J = 0
        
        self.FILL_MATRICES()
        self.BACKTRACKING()
        self.CALCULATE_SCORE()
    
    def RET_COST(self, PROT1, PROT2):
        if (PROT1 == PROT2 ):
            if (PROT1 == 'A'):
                return self.COST.AA
            elif (PROT1 == 'T'):
                return self.COST.TT
            elif (PROT1 == 'G'):
                return self.COST.GG
            else:
                return self.COST.CC
        else:
            if ((PROT1 == 'A' and PROT2 == 'T') or (PROT1 == 'T' and PROT2 == 'A')):
                return self.COST.TA
            elif ((PROT1 == 'C' and PROT2 == 'A') or (PROT1 == 'A' and PROT2 == 'C')):
                return self.COST.CA
            elif ((PROT1 == 'C' and PROT2 == 'T') or (PROT1 == 'T' and PROT2 == 'C')):
                return self.COST.CT
            elif ((PROT1 == 'G' and PROT2 == 'A') or (PROT1 == 'A' and PROT2 == 'G')):
                return self.COST.GA
            elif ((PROT1 == 'G' and PROT2 == 'T') or (PROT1 == 'T' and PROT2 == 'G')):
                return self.COST.GT
            elif ((PROT1 == 'G' and PROT2 == 'C') or (PROT1 == 'C' and PROT2 == 'G')):
                return self.COST.GC
    
    def FILL_MATRICES(self) :
        VALUE_MAX = 0
        
        LENA = len(self.SEQ1)
        LENB = len(self.SEQ2)
        
        scoring_matrix = np.zeros((LENA+1, LENB+1))
        direction_matrix = np.zeros((LENA+1, LENB+1), str)
        direction_matrix[0][0] = '0'
            
        for i in range(LENA):
            scoring_matrix[(i+1)][0] = 0
            direction_matrix[(i+1)][0] = VERTICAL
            
        for i in range(LENB):
            scoring_matrix[0][(i+1)] = 0
            direction_matrix[0][(i+1)] = HORIZONTAL
        
        for i in range(1, LENA+1):
            for j in range(1, LENB+1):
                VALUE_H = scoring_matrix[i][j-1] + GAP
                VALUE_V = scoring_matrix[i-1][j] + GAP
                VALUE_D = scoring_matrix[i-1][j-1] + int(self.RET_COST(self.SEQ1[i-1], self.SEQ2[j-1]))
                if (VALUE_H < 0): VALUE_H = 0
                if (VALUE_V < 0): VALUE_V = 0
                if (VALUE_D < 0): VALUE_D = 0
                DIRECTION = [DIAGONAL, HORIZONTAL, VERTICAL]
                LIST = [VALUE_D, VALUE_H, VALUE_V]
                INDEX = LIST.index(max(LIST))
                scoring_matrix[i][j] = LIST[INDEX]
                if(LIST[INDEX] > VALUE_MAX) :
                    VALUE_MAX = LIST[INDEX]
                    self.SEARCH_I = i
                    self.SEARCH_J = j
                direction_matrix[i][j] = DIRECTION[INDEX]
                
        self.SCORING_MATRIX = scoring_matrix
        self.DIRECTION_MATRIX = direction_matrix
        
    def BACKTRACKING(self):
        OUT1 = []
        OUT2 = []
                
        direction_matrix = self.DIRECTION_MATRIX
        
        i = self.SEARCH_I
        j = self.SEARCH_J
                
        exit=1
        
        while (exit != 0):
            selected = direction_matrix[i][j]
        
            if(selected == DIAGONAL):
                OUT1.append(self.SEQ1[i-1])
                OUT2.append(self.SEQ2[j-1])
                i = i -1
                j = j -1
            elif (selected == HORIZONTAL):
                OUT1.append('-')
                OUT2.append(self.SEQ2[j-1])
                j = j - 1
            elif (selected == VERTICAL):
                OUT1.append(self.SEQ1[i-1])
                OUT2.append('-')
                i = i - 1
            elif (selected == '0'):
                exit = 0
        
        for i in range(len(OUT1)):
            self.OUTPUT1.append(OUT1.pop())
        
        for i in range(len(OUT2)):
            self.OUTPUT2.append(OUT2.pop())

    def CALCULATE_SCORE(self):
        for i in range(len(self.OUTPUT1)):
            if (self.OUTPUT1[i] == '-' or self.OUTPUT2[i] == '-'):
                self.SCORE = self.SCORE + GAP
            else:
                self.SCORE = self.SCORE + int(self.RET_COST(self.OUTPUT1[i], self.OUTPUT2[i]))
        
def PrintCostMatrix(matrix, _gap):
    print("   -  A  T  C  G")
    print("- %+d" % (int(_gap)) + " %+d" % (int(_gap)) + " %+d" % (int(_gap)) + " %+d" % (int(_gap)) + " %+d" % (int(_gap)))
    print("A %+d" % (int(_gap)) + " %+d" % (int(matrix.AA)) + " %+d" % (int(matrix.TA)) + " %+d" % (int(matrix.CA)) + " %+d" % (int(matrix.GA)))
    print("T %+d" % (int(_gap)) + " %+d" % (int(matrix.TA)) + " %+d" % (int(matrix.TT)) + " %+d" % (int(matrix.CT)) + " %+d" % (int(matrix.GT)))
    print("C %+d" % (int(_gap)) + " %+d" % (int(matrix.CA)) + " %+d" % (int(matrix.CT)) + " %+d" % (int(matrix.CC)) + " %+d" % (int(matrix.GC)))
    print("G %+d" % (int(_gap)) + " %+d" % (int(matrix.GA)) + " %+d" % (int(matrix.GT)) + " %+d" % (int(matrix.GC)) + " %+d" % (int(matrix.GG)))
    return ''

# --- MAIN ---
MAX_COST = COST([0,0,0,0,0,0,0,0,0,0])
MAX_COMP = COMPARISON("","","")

with open('costs.txt') as file: read = file.readlines()
for i in range(len(read)): read[i] = read[i].replace('\n', '')

costs = [x.strip().split(',') for x in read] 

COST_LIST = []

for i in range(len(costs)):
    COST_LIST.append(COST(costs[i]))

with open('sequences.txt') as file: sequences = file.readlines()
for i in range(len(sequences)): sequences[i] = sequences[i].replace('\n', '')

for i in range(len(costs)):
    C_LIST = []
    for j in range (1, len(sequences)):
        C_LIST.append(COMPARISON(sequences[0], sequences[j], COST_LIST[i]))

    print("COST#"+ str(i+1) +" ------------------------------------------\n")
    
    for k in range(0, len(C_LIST)):
        print(str(k+1) + " ------------------------------------------\n")
        print("\nDIRECTION MATRIX:")
        print(C_LIST[k].DIRECTION_MATRIX)
        print("\nSCORING MATRIX:")
        print(C_LIST[k].SCORING_MATRIX)
        print("\nOUTPUTS:")
        print(''.join(C_LIST[k].OUTPUT1))
        print(''.join(C_LIST[k].OUTPUT2))
        print("\n")
        print("SCORE: " + str(C_LIST[k].SCORE))
        print("\nCOST MATRIX:")
        print(PrintCostMatrix(COST_LIST[i], GAP))
        print("\n-----------------------------------------------\n\n")
        if(C_LIST[k].SCORE > MAX_COMP.SCORE):
            MAX_COMP = C_LIST[k]
            MAX_COST = COST_LIST[i]
        
print("\n-----------------------------------------------------------------------------------")
print("\n-----------------------------------------------------------------------------------")
print("\n-----------------------------------------------------------------------------------\n")
print("MAXIMUM SCORE WITH PROVIDING COST MATRIX ------------------------------------------\n")
print("\nDIRECTION MATRIX:")
print(MAX_COMP.DIRECTION_MATRIX) 
print("\nSCORING MATRIX:")
print(MAX_COMP.SCORING_MATRIX)
print("\n")
print(''.join(MAX_COMP.OUTPUT1))
print(''.join(MAX_COMP.OUTPUT2))
print("\n")
print("SCORE: " + str(MAX_COMP.SCORE))
print("\nCOST MATRIX:")
print(PrintCostMatrix(MAX_COST, GAP))
print("\n-----------------------------------------------------------------------------------")
print("\n-----------------------------------------------------------------------------------")
print("\n-----------------------------------------------------------------------------------\n")
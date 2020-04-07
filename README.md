# BIL458 BIOINFORMATICS HOMERWORK 1
###### Prepared By: [Alperen Köylü](https://github.com/alperenkoylu "Alperen Köylü")
###### Github Repository: [BIOINFORMATICS](https://github.com/alperenkoylu/BIOINFORMATICS "Link")
------------
### Included Algorithms
1. Needleman-Wunsch Global Alignment Algorithm
1. Smith-Waterman Local Alignment Algorithm
1. ~~tBLASTn Algorithm~~ 
1. ~~Star Aligment Algorithm~~ 
1. ~~CLUSTALW Algorithm (UPGMA)~~ 
------------
### Usage
- **Sequences**, can be determine in the sequences.txt
    - Ps: First sequence line will be compared by other sequences, consider as a master sequence.)
------
- **Cost Matrices**, can be set via editing cost.txt

    - A line of costs.txt, eg. **1, 2, 3, 4, 5, 6, 7, 8, 9, 10** will be equivalent to pseudo matrix below
    
    - Pseudo Cost Matrix:
    
      |   | A | T | C | G |
      | ------------ | ------------ | ------------ | ------------ | ------------ |
      | A | **1** | 2 | 4 | 7 |
      | T | **2** | **3** | 5 | 8 |
      | C | **4** | **5** | **6** | 9 |
      | G | **7** | **8** | **9** | **10** |

    - Ps: If you consider cost matrix as in figure above every line of costs.txt will represent a single cost matrix. 
------
- **Gap** value is set to the -6. You can change it through the algorithms .py file.

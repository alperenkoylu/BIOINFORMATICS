# BIL458 BIOINFORMATICS HOMEWORK 1
### Prepared By: [Alperen Köylü](https://github.com/alperenkoylu "Alperen Köylü")
Thanks to [Can Okan Taşkıran](https://github.com/CantOkan "Can Okan Taşkıran") and [Şeref Fatih Yılmaz](https://github.com/sfatihyilmaz "Şeref Fatih Yılmaz") for their contribution in order to building the logic behind this algorithm.
###### Final Report: [Click to View](https://github.com/alperenkoylu/BIOINFORMATICS/blob/master/report.pdf "Click to View")
------------
### Getting Started
- In this project, I aimed to compare the master sequence with the other 26 slave sequences and to find the best global and local alignment. 

- All sequences and cost matrices will be taken from sequences.txt and costs.txt file respectively. The first line of the sequences.txt file represents the master sequence, others represent slave sequences, and each line of the costs.txt file represents a separate cost matrix. Detailed information is given in the usage section below.
------------
### About The Logic
- In this project, dynamic programming has been used on the basis of being as close as possible to the OOP programming approach. All sequence comparisons were kept in a class, and the cost matrix used to score sequences, score matrices, direction matrices, and sequences were kept in the same class for comfortable comparison while finding the best result.
------------
### Included Algorithms
1. Needleman-Wunsch Global Alignment Algorithm
1. Smith-Waterman Local Alignment Algorithm
------------
### Preparing the Parameters to be Used 
- **Sequences**, can be determine in the sequences.txt. First line of .txt file represent the master sequence while rest of them is represents the slave ones.
    - Ps: First sequence line will be compared by other sequences, consider as a master sequence.
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
- **Gap** value is set to the -6. You can change it through the each algorithm's .py file.
------
### Usage
- In order to observe all result I would recommend to use **CMD (Windows) or Terminal (Linux\Unix)**.
- Python IDLE or Powershell or any other python compiler will not show you all result due to their constraints.
- No extra arguments need to run the algorithms.
```
C:\Folder\That\Contains\py\Files>algorithm.py
```

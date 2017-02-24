# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternMatching(Pattern, Text, d):
    positions = [] # initializing list of positions
    # your code here
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Pattern, Text[i:i+len(Pattern)]) <= d:
            positions.append(i)
    return positions



# Input:  Two strings, Pattern and Genome
# Output: A list containing all starting positions where Pattern appears as a substring of Genome
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    # your code here
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(' '.join([str(i) for i in PatternMatching(lines[0],lines[1])]))




**************************************************************************************************


# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
    revComp = '' # output variable
    # your code here
    for x in reverse(Pattern):
        revComp = revComp + complement(x)
    return revComp


# Copy your reverse function from the previous step here.
def reverse(text):
    temp =""    
    for i in range(len(text)-1, -1, -1):
        temp = temp + text[i]       
    return temp

# HINT:   Filling in the following function is optional, but it may come in handy when solving ReverseComplement
# Input:  A character Nucleotide
# Output: The complement of Nucleotide
def complement(Nucleotide):
    comp = '' # output variable
    # your code here
    if Nucleotide =='A':
        comp = 'T'
    elif Nucleotide =='T':
        comp = 'A'
    elif Nucleotide =='C':
        comp = 'G'   
    elif Nucleotide =='G':
        comp = 'C'        
    return comp



### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
print(ReverseComplement(sys.stdin.read().strip()))


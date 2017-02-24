# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = [] # output variable
    # your code here
    skewDict = Skew(Genome)
    mini = skewDict[min(skewDict, key = skewDict.get)]
    for i in range(len(skewDict)):
        if skewDict[i] ==  mini:
            positions.append(i)
    return positions



# Input:  A String Genome
# Output: Skew(Genome)
def Skew(Genome):
    skew = {} #initializing the dictionary
    # your code here
    skew[0] = 0
    for i in range( len(Genome)):
        skew[i+1] = skew[i]
        if Genome[i] =="G":
            skew[i+1] = skew[i] +1
        if Genome[i] =="C":
            skew[i+1] = skew[i] -1
    return skew


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys


skew = Skew("GATACACTTCCCGAGTAGGTACTG")
print (' '.join([str(skew[i]) for i in sorted(skew.keys())]))
print (skew)

print (skew[min(skew, key = skew.get)])


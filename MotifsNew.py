
# import Python's 'random' module here
import random
# Input:  A list of strings Dna, and integers k and t
# Output: RandomMotifs(Dna, k, t)
# HINT:   You might not actually need to use t since t = len(Dna), but you may find it convenient
def RandomMotifs(Dna, k, t):
    # place your code here.
    randomMotifs=[]
    for i in range (t):
        start = random.randint(0,(len(Dna[i])-k))
        result = Dna[i][start:(start + k)]
        randomMotifs.append(result)
    return randomMotifs



# Input:  A profile matrix Profile and a list of strings Dna
# Output: Motifs(Profile, Dna)
def Motifs(Profile, Dna):
    # insert your code here
    Motifs = []
    t = len(Dna)
    for i in range(t):
        Text = Dna[i]
        result = ProfileMostProbablePattern(Text, 4, Profile)
        Motifs.append(result)
    return Motifs

# Insert your ProfileMostProbablePattern(Text, k, Profile) and Pr(Pattern, Profile) functions here.
# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def Pr(Text, Profile):
    # insert your code here
    p =1
    for i in range (len(Text)):
        p = p * Profile[Text[i]][i]
    return p

# Input:  String Text, an integer k, and profile matrix Profile
# Output: ProfileMostProbablePattern(Text, k, Profile)
def ProfileMostProbablePattern(Text, k, Profile):
    # insert your code here. Make sure to use Pr(Text, Profile) as a subroutine!
    result = Text[:k]
    pMax = 0
    for i in range(len(Text) - k + 1):
        currentText = Text[i:(i + k)]
        p = Pr(currentText, Profile)
        if p > pMax:
            result = currentText
            pMax = p
    return result

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
A = [float(c) for c in lines[0].split()]
C = [float(c) for c in lines[1].split()]
G = [float(c) for c in lines[2].split()]
T = [float(c) for c in lines[3].split()]
Profile = {'A':A,'C':C,'G':G,'T':T}
Dna = lines[4:]
print('\n'.join(Motifs(Profile,Dna)))
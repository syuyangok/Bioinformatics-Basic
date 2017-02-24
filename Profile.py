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


BestMotifs = []
for i in range(0, t):
    BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n - k + 1):
        Motifs = []
        Motifs.append(Dna[0][i:i + k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
            if Score(Motifs) < Score(BestMotifs):
                BestMotifs = Motifs
return BestMotifs

# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearch(Dna, k, t):
    # type your GreedyMotifSearch code here.
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs
### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
Text = lines[0]
A = [float(c) for c in lines[1].split()]
C = [float(c) for c in lines[2].split()]
G = [float(c) for c in lines[3].split()]
T = [float(c) for c in lines[4].split()]
Profile = {'A':A, 'C':C, 'G':G, 'T':T}
print(Pr(Text,Profile))



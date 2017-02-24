# import the random package here
import random


# Input:  Positive integers k and t, followed by a list of strings Dna
# Output: RandomizedMotifSearch(Dna, k, t)
def RandomizedMotifSearch(Dna, k, t):
    # insert your code here
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M

    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs
            # Insert necessary subroutines here, including RandomMotifs(), ProfileWithPseudocounts(), Motifs(), Score(),


# and any subroutines that these functions need.
def RandomMotifs(Dna, k, t):
    # place your code here.
    randomMotifs = []
    for i in range(t):
        start = random.randint(0, (len(Dna[i]) - k))
        result = Dna[i][start:(start + k)]
        randomMotifs.append(result)
    return randomMotifs


def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}  # output variable
    # your code here
    profile = CountWithPseudocounts(Motifs)
    total = 0
    for symbol in "ACGT":
        for j in range(k):
            profile[symbol][j] = (profile[symbol][j]) / (t + 4)
    return profile


def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    # insert your code here
    count = {}
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)

    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1

    for x in "ACGT":
        for j in range(k):
            count[x][j] += 1
    return count


def Score(Motifs):
    # Insert code here
    k = len(Motifs[0])
    t = len(Motifs)
    total = 0
    consen = Consensus(Motifs)
    for j in range(k):
        symbol = consen[j]
        for i in range(t):
            if Motifs[i][j] != symbol:
                total += 1
    return total


def Consensus(Motifs):
    # insert your code here
    k = len(Motifs[0])
    count = CountWithPseudocounts(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus


def Motifs(Profile, Dna):
    # insert your code here
    Motifs = []
    t = len(Dna)
    for i in range(t):
        Text = Dna[i]
        result = ProfileMostProbablePattern(Text, k, Profile)
        Motifs.append(result)
    return Motifs


# Insert your ProfileMostProbablePattern(Text, k, Profile) and Pr(Pattern, Profile) functions here.
# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def Pr(Text, Profile):
    # insert your code here
    p = 1
    for i in range(len(Text)):
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
def RepeatedRandomizedMotifSearch(Dna, k, t):
    BestScore = float('inf')
    BestMotifs = []
    for i in range(1000):
        Motifs = RandomizedMotifSearch(Dna, k, t)
        CurrScore = Score(Motifs)
        if CurrScore < BestScore:
            BestScore = CurrScore
            BestMotifs = Motifs
    return BestMotifs


import sys

lines = sys.stdin.read().splitlines()
k, t = lines[0].split()
k = int(k)
t = int(t)

print('\n'.join(RepeatedRandomizedMotifSearch(lines[1:], k, t)))
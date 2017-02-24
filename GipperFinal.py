# first, import the random package
import random


# Input:  Integers k, t, and N, followed by a collection of strings Dna
# Output: GibbsSampler(Dna, k, t, N)
def GibbsSampler(Dna, k, t, N):
    BestMotifs = []  # output variable
    # your code here
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    for j in range(N):
        i = random.randint(1, t - 1)
        Profile = ProfileWithPseudocounts(M)  # profile matrix formed from all strings in Motifs except for Motifi

        M[i] = ProfileGeneratedString(Dna[i], Profile, k)  # Profile-randomly generated k-mer in the i-th string
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
    return BestMotifs


# place all subroutines needed for GibbsSampler below this line

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


# Input: A dictionary Probabilities, where keys are k-mers and values are the probabilities of these k-mers (which do not necessarily sum up to 1)
# Output: A normalized dictionary where the probability of each k-mer was divided by the sum of all k-mers' probabilities
def Normalize(Probabilities):
    # your code here
    total = 0
    for x in Probabilities.values():
        total += x
    for key, value in Probabilities.items():
        Probabilities[key] = value / total
    return Probabilities


# Input:  A dictionary Probabilities whose keys are k-mers and whose values are the probabilities of these kmers
# Output: A randomly chosen k-mer with respect to the values in Probabilities
def WeightedDie(Probabilities):
    kmer = ''  # output variable
    # your code here
    p = random.uniform(0, 1)
    start = 0
    for key, value in Probabilities.items():
        if p >= start and p <= value + start:
            kmer = key
            return kmer
        start += value
    return kmer


# Input:  A string Text, a profile matrix Profile, and an integer k
# Output: ProfileGeneratedString(Text, profile, k)
def ProfileGeneratedString(Text, profile, k):
    # your code here
    n = len(Text)
    probabilities = {}
    for i in range(0, n - k + 1):
        probabilities[Text[i:i + k]] = Pr(Text[i:i + k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)
# first, import the random package
import random


# then, copy Pr, Normalize, and WeightedDie below this line

# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def Pr(Text, Profile):
    # insert your code here
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p


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


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys

it, Text, profile, k = sys.stdin.read().splitlines()
it = int(it)
profile = eval(profile)
k = int(k)
print('\n'.join([ProfileGeneratedString(Text, profile, k) for i in range(it)]))
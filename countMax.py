
def CountDict(Text, k):

    Count = {} # output variable

    # your code here

    for i in range (len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i]= PatternCount(Pattern, Text)
    return Count

def PatternCount(Pattern, Text):

    count = 0 # output variable

    # your code here

    for i in range(len(Text)-len(Pattern)+1):

        if Text[i:i+len(Pattern)] == Pattern:

            count = count+1

    return count


Count = CountDict("atgaccgggatactgataaaaaaaagggggggggcgtacacattagataaacgtatgaagtacgttagactcggcgccgccgacccctattttttgagcagatttagtgacctggaaaaaaaatttgagtacaaaacttttccgaataaaaaaaaaggggggga" , 15)
text = "atgaccgggatactgataaaaaaaagggggggggcgtacacattagataaacgtatgaagtacgttagactcggcgccgccgacccctattttttgagcagatttagtgacctggaaaaaaaatttgagtacaaaacttttccgaataaaaaaaaaggggggga"

m = max(Count.values())

for i in range(len(Count)):
    if Count[i] == m:
        print (text[i:i+15])


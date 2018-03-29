#Maia Reynolds
#3/30/18
#stringIntersect.py - letters in both words

def stringIntersect(word1,word2):
    final=""
    word1=word1.lower()
    word2=word2.lower()
    for ch in word1:
        if ch in word2 and ch not in final:
            final+=ch
    return final

print(stringIntersect("Mississippi","Pennsylvania"))
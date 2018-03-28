#Maia Reynolds
#3/28/18
#stringUnion.py - two strings to non-repeating characters

def stringUnion(word1,word2):
    final=""
    for ch in word1:
        if ch not in final:
            final+=ch
    for ch in word2:
        if ch not in final:
            final+=ch
    print(final)

stringUnion("mississipe","mauiadbaoysifybsdiofbyiosdzvgbgz")
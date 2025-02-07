# Given two strings, s and t, return True if t is an anagram of s, and False otherwise.
# An anagram is a word that can be formed by rearranging the letters of another word.

s = "listen"
t = "silent"


def main(s,t):
    return print(sorted(s) == sorted(t))

main(s,t)

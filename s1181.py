import sys
N = int(input())
words = [sys.stdin.readline().rstrip() for _ in range(N)]

words = set(words)
words = list(words)
words.sort()
words.sort(key=len)

for word in words:
    print(word)
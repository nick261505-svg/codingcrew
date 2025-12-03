from collections import defaultdict

sentence="apple banana apple cherry banana apple"
words=sentence.split()

word_counts=defaultdict(int)
for word in words:
    word_counts[word] = word_counts[word]+1
    # 처음에는 존재하지 않으면 ->기본값 0

print("단어별빈도수: ", word_counts)

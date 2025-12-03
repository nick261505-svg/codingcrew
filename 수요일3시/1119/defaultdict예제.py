from collections import defaultdict, OrderedDict

text="""
The quick brown fox jumps over the lazy dog.
The dog runs fast, but the fox is quicker.
The jumps of the fox are amazing.
"""

#전처리 작업
#구두점 제거 및 소문자 변환
cleaned_text=text.lower().replace(',','').replace('.','')
words=cleaned_text.split()

#불용어 제거
stopwords={'the', 'a', 'is', 'are','but', 'to','of'}
filtered_words=[word for word in words if word not in stopwords]

word_counts=defaultdict(int)
for word in filtered_words:
    #word_counts[word]가 존재하지않으면 word_counts[word]=0자동으로 실행후 1을 더함
    word_counts[word] += 1

print(dict(word_counts))
print("------------------------")
item_list=list(word_counts.items())
print(item_list)


sorted_items=sorted(item_list, key=lambda item:item[1], reverse=True)


ordered_word_counts=OrderedDict(sorted_items)
print("------------------------")
#상위 3개만
for i,item in enumerate( ordered_word_counts.items()):
    if i==3:break    
    print(i,":",item)
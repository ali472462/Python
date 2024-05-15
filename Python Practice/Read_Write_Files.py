"""
word_stats={}

with open("poem.txt","r") as f:
    for line in f:
      words=line.split(' ')
      for word in words:
        if word in word_stats:
          word_stats[word]+=1
        else:
          word_stats[word] = 1

print(f"Dictionary :.{word_stats}")

word_occurances = list(word_stats.values())
print(f"List :{word_occurances}")
max_count = max(word_occurances)
print("Max occurances of any word is:",max_count)

print("Words with max occurances are: ")
for word, count in word_stats.items():
    if count==max_count:
        print(word)

poem={}

with open("poem.txt","r") as v:
    for line in v:
        word=line.split(' ')
        for w in word:
            if w not in poem:
                poem[w]=1
            else:
                poem[w]+=1
print(f"Dictionary: {poem}")

l_word=list(poem.values())
print(l_word)

m_val=max(l_word)
print(m_val)

for word,count  in poem.items():
    if count==m_val:
        print(word)
"""
stocks={}

with open("stocks.csv", "r") as f, open("output.csv", "w") as out:
    out.write("Company Name,PE Ratio, PB Ratio\n")
    next(f)  # This will skip first line in the file which is a header
    for line in f:
        tokens = line.split(',')
        stock = tokens[0]
        price = float(tokens[1])
        eps = float(tokens[2])
        book = float(tokens[3])
        pe = round(price / eps, 2)
        pb = round(price / book, 2)
        out.write(f"{stock},{pe},{pb}\n")

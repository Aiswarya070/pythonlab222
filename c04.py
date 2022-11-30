lineText="this is a web page"
words={}
for word in lineText.split(" "):
    if word in words.keys():
        words[word]+=1
    else:
        words[word]=1
print(words)   
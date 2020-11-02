def freq_count():
    str=('sheena loves eating apple and mango . her sister also loves eating apple and mango .')
    count={}
    words=str.split()
    for word in words:
        if word not in count:
            count[word]=1
        else:
            count[word]+=1

        #count[word]=count.get(word,0)+1
    print(count)
freq_count()
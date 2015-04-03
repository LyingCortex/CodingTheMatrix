#LL=['Hello , everyone !', 'hi , boys and girls .', 'hi , Hello , hi ,   I love this world Hello  action', 'do it','action']
LL = ['hello world','hello','hello cat','hellolot of cats']
LL_set = [set(x.split()) for x in LL]
set_L =set()
for i in range(len(LL_set)):
    set_L= set_L | LL_set[i]

dict_L =set_L # Dictionary
print (dict_L)

postinglist ={}

for word in dict_L:
    postinglist[word]=set()
    for i in range(len(LL_set)):
        if word in LL_set[i]:
            postinglist[word]|={i}


print(postinglist)

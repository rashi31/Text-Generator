# Write your code here
from nltk import regexp_tokenize
from collections import Counter
import random
import re

fn = input()
f = open(fn, "r", encoding="utf-8")
token = []
for line in f:
    token += regexp_tokenize(line, r'[^\s\t\n]+')

trigrams = []
i = 0
j = 1
k = 2

while i < (len(token)-2):
    big = [token[i], token[j]]
    bigram = ' '.join(big)
    sub = [bigram, token[k]]
    trigrams.append(sub)
    i = i + 1
    j = j + 1
    k = k + 1

new = []
for w in trigrams:
    if re.match('^[A-Z]', w[0]):
        z = w[0].split()
        if z[0].endswith(('.', '!', '?', ';')):
            continue
        else:
            new.append(w[0])

outer = 1

while outer <= 10:
    fl = []
    user = random.choice(new)
    fl.append(user)
    inner = 1
    while True:
        t = []
        for i in trigrams:
            if i[0] == user:
                t.append(i[1])

        c = Counter(t).most_common()
        w = []
        lt = []

        for x, y in c:
            lt.append(x)
            w.append(y)

        a = random.choices(lt, weights=w)
        fl.extend(a)

        if len(fl) > 3 and a[0].endswith(('.', '!', '?', ';')):
            break

        inner = inner + 1

        user =[user.split()[1], a[0]]
        user = ' '.join(user)

    s = ' '
    print(s.join(fl))
    outer = outer + 1

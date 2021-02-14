ls = list(input().split())

substr = "de"

for word in ls:
    if substr in word:
        print(word);

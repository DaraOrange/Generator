import re
import random
import operator

dic = {}
def gen(file):
	f = open(file)
	sentences = f.read().lower()
	sentences = re.split(r'[.!?]', sentences)
	for s in sentences:
		s = re.findall(r'([\w]+)', s)
		for i in range(len(s)-1):
			if not (s[i] in dic):
				dic[s[i]] = {}
			if not (s[i+1] in dic[s[i]]):
				dic[s[i]][s[i+1]] = 0
			dic[s[i]][s[i+1]] += 1
	for w in dic:
		dic[w] = sorted(dic[w].items(), key=operator.itemgetter(1))

def get(num):
	word = random.choice(list(dic.items()))[0]
	ans = []
	ans.append(word)
	for i in range(num-1):
		if not(word in dic):
			get(num)
			break
		word = dic[word][0][0]
		ans.append(word)
	print(" ".join(ans))

if __name__ == '__main__':
        print("Input names of files")
        files = str(input())
        files = files.split(' ')
        for f in files:
                gen(f)
        print("Input number of words in sentence")
        n = int(input())
        get(n)




from trie import *
import timeit
from flask import Flask,jsonify,request
from itertools import combinations


t = Trie()
english_words = {}

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

def search_word(word):
	return t.search(word)


def generate_anagrams(word):
	word = ''.join(sorted(word.lower()))
	anagrams = set()
	for i in range(1,len(word)+1):
		for x in combinations(word,i):
			anagrams.add("".join(x))
	#print(anagrams)
	return anagrams

def search_anagram_list(anagrams):
	result = set()
	for word in anagrams:
		a,b = search_word(word)
		#print(word,a,b)
		if a == True:
			for x in b:
				result.add(x)
	return result


@app.route("/") 
def home_view(): 
        return "<h1>Welcome to Geeks for Geeks</h1>"

app = Flask(__name__)
@app.route("/process",methods=['POST'])
def process():


	start = timeit.default_timer()
	print("Request Recieved on Server")
	content = request.get_json()
	word = str(content["text"])
	anagrams = generate_anagrams(word)
	res = search_anagram_list(anagrams)
	result = []
	for x in res:
		result.append(x)
	#print(result)
	stop = timeit.default_timer()
	print(stop- start)
	return jsonify(result)

if __name__ == '__main__':
    english_words = load_words()

    start = timeit.default_timer()
    # length print
    #print(len(english_words))

    for word in english_words:
    	#word = ''.join(sorted(word)) 
    	t.insert(word)

    stop = timeit.default_timer()
    print("Time to insert in trie : ",stop - start)

    start = timeit.default_timer()
    #for word in english_words:
    	#word = ''.join(sorted(word)) 
    	#search_word(word)
    	#print(word,t.search(word))

    stop = timeit.default_timer()
    #print(stop - start)

    #start = timeit.default_timer()
    #generate_anagrams(''.join(sorted("helloworl")))
    #anagrams = generate_anagrams("HelloWorld")
    #result = search_anagram_list(anagrams)
    #print(result)

    #stop = timeit.default_timer()
    #print(stop - start)


    #app.run(host='0.0.0.0',port=233,debug=True)
    app.run()

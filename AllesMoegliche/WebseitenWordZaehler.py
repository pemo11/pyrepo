# Zählen der Worte auf einer Webseite
# Wichtig: https-Sites gehen in dieser Version leider nicht
import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

def start(url):
    wordlist = []
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, "html.parser")
    
    # Willkürliche Annahme, dass sich der Text in div-Kästen befindet
    for each_text in soup.find_all('div'):
        content = each_text.text
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        # print(wordlist)
        cleanlist = clean_wordlist(wordlist)
        return create_dictionary(cleanlist)
    
def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '
        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')
        if len(word) > 0:
            clean_list.append(word)
    return clean_list

def create_dictionary(clean_list):
    word_count = {}
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

if __name__ == '__main__':
    url = "http://www.activetraining.de"
    url = "http://www.vhs-esslingen.de"
    wordDic = start(url)
    # print(wordDic)

    c = Counter(wordDic)
    top = c.most_common(10)
    print(top)
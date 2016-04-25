from __future__ import unicode_literals

from glob import glob
try: reduce
except: from functools import reduce
import os
import time

class SearchResult():
    
    def __init__(self):
        start_time = time.time()
        self.texts, self.words = self.parsetexts()
        print("--- Parsing took time in seconds ---  %s" % (time.time() - start_time))
        start_time = time.time()
        self.finvindex = self.getInvIndex()
        print("--- Indexing took time in seconds ---  %s" % (time.time() - start_time))

    def parsetexts(self):
        #print "Entered the parsetexts "
        texts, words = {}, set()
        # Here path can be changed as per the redis code folder in your local machine
        for root, directories, filenames in os.walk('D:/Word Searcher/redis-unstable'):
            for filename in filenames:
                fileglob = os.path.join(root, filename)
                for txtfile in glob(fileglob):
                    with open(txtfile, 'r') as f:
                        txt = f.read().split()
                        words |= set(txt)
                        words = words.union(set(txt))
                        texts[txtfile.split('\\')[-1]] = txt
                        texts[txtfile] = txt
                        print words
            break
        return texts, words
    
    def getInvIndex(self):
        texts = self.texts
        words = self.words
        finvindex = {word:set((txt, wrdindx)
                              for txt, wrds in texts.items()
                              for wrdindx in (i for i, w in enumerate(wrds) if word == w)
                              if word in wrds)
                     for word in words}
        return finvindex
    
    def termsearch(self, terms):  # Searches full inverted index
        texts = self.texts
        words = self.words
        finvindex =  self.finvindex
        if not set(terms).issubset(words):
            return set()
        return reduce(set.intersection,
                      (set(x[0] for x in txtindx)
                       for term, txtindx in finvindex.items()
                       if term in terms),
                      set(texts.keys()))
     
    def phrasesearch(self, phrase):
        #print "Entered the PharseSearch ",phrase
        #texts = self.texts
        words = self.words
        finvindex =  self.finvindex
        wordsinphrase = phrase.strip().strip('"').split()
        if not set(wordsinphrase).issubset(words):
            return set()
        firstword, otherwords = wordsinphrase[0], wordsinphrase[1:]
        found = []
        for txt in self.termsearch(wordsinphrase):
            for firstindx in (indx for t, indx in finvindex[firstword] if t == txt):
                if all((txt, firstindx + 1 + otherindx) in finvindex[otherword]
                       for otherindx, otherword in enumerate(otherwords)):
                            if txt not in found: found.append(txt)
        return found

a = SearchResult()
a.phrasesearch("Test")


class ExtractionTools:
    """Extraction tools provide an interface to nltk functions"""

    re = __import__('re')
    nltk = __import__('nltk')

    grammar = r"""
        NBAR:
            {<NN.*|JJ>*<NN.*>}
        NP:
            {<NBAR>}
            {<NBAR><IN><NBAR>}
    """

    stemmer = nltk.stem.porter.PorterStemmer()
    lemmatizer = nltk.WordNetLemmatizer()
    stopwords = nltk.corpus.stopwords.words('english')

    tagger = nltk.tag.perceptron.PerceptronTagger()
    chunker = nltk.RegexpParser(grammar)

    def strip(self, word):
        "Strip all ancilary content from word"

        return self.re.sub(r'\W+','',word).lower()

    def stem(self, word):
        "Stem the given word"

        return self.stemmer.stem_word(word)

    def lemmatize(self, word):
        "Lemmatize the given word"

        return self.lemmatizer.lemmatize(word)

    def synsets(self, word):
        "Find synsets for the given word"

        return self.nltk.corpus.wordnet.synsets(word)

    def word_tokenize(self, text):
        "Tokenize the given text into words"

        return self.nltk.tokenize.word_tokenize(text)

    def sent_tokenize(self, text):
        "Tokenize the given text into sentences"

        return self.nltk.tokenize.sent_tokenize(text)

    def tag(self, words):
        "Position tag the given word"

        return self.nltk.tag._pos_tag(words, None, self.tagger)

    def parse(self, position_tokens):
        "Parse the given position tokens into a tree"

        return self.chunker.parse(position_tokens)


if (__name__ == "__main__"):
    extraction_tools = ExtractionTools()
    assert('tabl' == extraction_tools.stem('tables'))
    assert('table' == extraction_tools.lemmatize('tables'))
    assert([('good','JJ'),('code','NN')] == extraction_tools.tag(['good','code']))

    
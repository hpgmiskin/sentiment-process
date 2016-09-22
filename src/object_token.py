from extraction_tools import ExtractionTools

class Token(object):
    "Token represnts a single word along with a tag"

    tools = ExtractionTools()

    def __init__(self,word,tag):
        "Initilize the token with word and tag"

        # Strip word to most basic form
        word = self.tools.strip(word)
        word = self.tools.stem(word)
        word = self.tools.lemmatize(word)

        # Set default count to 0
        self.count = 0

        # Store tag and word
        self.tag = tag
        self.word = word

    def __hash__(self):
        "Return hash of the token"

        return hash(self.word)

    def __nonzero__(self):
        "Check if word meets criteria for analysis"

        return bool(
            (2 <= len(self.word) <= 40) and
            (self.word not in self.tools.stopwords) and
            (self.tools.synsets(self.word))
        )

    def __str__(self):
        "Return string representation of token"

        return self.word

    def __eq__(self,token):
        "Check if this token represents the same word as another"

        return (self.word == token.word)
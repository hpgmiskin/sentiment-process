from object_text import Text
from object_token import Token
from object_feature import Feature

class Sentence(Text):
    "Sentence is a type of text which is contained within a document"

    def __init__(self,text):

        # Store the text
        self.text = text

        # Tokenize, tag and create tree from text
        words = self.tools.word_tokenize(self.text)
        tokens = self.tools.tag(words)
        tree = self.tools.parse(tokens)

        # Store acceptable tokens for entire text
        self.tokens = []
        for word, tag in tokens:
            token = Token(word, tag)
            if (token): self.tokens.append(token)

        # Create empty list of features
        self.features = []

        # Loop through all subtrees containing a noun phrase
        for subtree in tree.subtrees(filter = lambda t: t.label()=='NP'):

            # Create empty list to store tokens
            words = []
            tokens = []

            # For all words in subtree create token
            for word, tag in subtree.leaves():

                # Create a token
                token = Token(word, tag)
                words.append(word)

                # If token acceptable and not in list append
                if (token and (token not in tokens)):
                    tokens.append(token)

            # If there are acceptable tokens create feature
            if (len(tokens) > 0):
                text = ' '.join(words)
                feature = Feature(tokens,text)
                self.features.append(feature)



class Feature(object):
    "Feature respresents a collection of tokens"

    def __init__(self,tokens,text=None,sentiment=0):
        self.count = 1

        if (text is None):
            text = ' '.join([str(token) for token in tokens]).lower()

        self.tokens = tuple(tokens)
        self.text = text
        self._sentiment = sentiment


    def combine(self,feature):
        "Combine this feature with another feature"

        # If features are equal
        if (self == feature):

            # Sum count and _sentiment
            self.count += feature.count
            self._sentiment += feature._sentiment

            # If other feature text is more concise replace
            if (len(feature.text) < len(self.text)):
                self.text = feature.text
                

    def sentiment(self):
        "Return the average sentiment"

        return (self._sentiment/float(self.count))

    def to_dict(self):
        "Return dictionary representation of feature"

        return dict(
            text = self.text,
            count = self.count,
            tokens = self.tokens,
            sentiment = self.sentiment(),
            sentences = [
                dict(
                    text = sentence.text,
                    tokens = tuple(sentence.tokens),
                    sentiment = sentence.sentiment
                )
                for sentence in self.sentences
            ]
        )

    def __hash__(self):
        "Return hash value of feature"

        return hash(self.tokens)

    def __repr__(self):
        "Return string representation of token"

        return str([str(token) for token in self.tokens])

    def __eq__(self,feature):
        "Check if this contains the same tokens as provided feature"

        return (self.tokens == feature.tokens)


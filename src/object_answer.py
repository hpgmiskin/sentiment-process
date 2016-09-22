from object_text import Text
from object_sentence import Sentence

class Answer(Text):
    "Answer is a type of text which stores a list of sentences"

    def __init__(self,text):
        "Initilize answer class and add sentences"

        sentences = self.tools.sent_tokenize(text)
        self.sentences = [Sentence(sentence) for sentence in sentences]

    def get_elements(self):
        "Return all elmements contained within the sentences"

        elements = []
        for sentence in self.sentences:
            for feature in sentence.features:
                element = dict(
                    sentence = dict(
                        text = sentence.text,
                        tokens = list(map(str,sentence.tokens))
                    ),
                    feature = dict(
                        text = feature.text,
                        tokens = list(map(str,feature.tokens))
                    )
                )
                elements.append(element)

        return elements

if (__name__ == "__main__"):
    answer = Answer('I really like this brand')
    elements = answer.get_elements()
    assert(elements[0]['feature']['text'] == 'brand')
    assert(elements[0]['feature']['tokens'] == ['brand'])
    assert(elements[0]['sentence']['text'] == 'I really like this brand')
    assert(elements[0]['sentence']['tokens'] == ['really','like','brand'])

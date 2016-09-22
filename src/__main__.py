import json

from object_answer import Answer

def main():

    answer = Answer('I really like this brand because there are many computers. And there is a fluffy animal')
    elements = answer.get_elements()
    print(json.dumps(elements,indent=4))

if (__name__ == "__main__"):
    main()
import requests

QUIZ_URL = "https://bjornkjellgren.se/quiz/v2/questions"


class Question:
    id: int
    prompt: str
    times_asked: int
    times_correct: int
    answers: list

    def __init__(self, id_, prompt, times_asked, times_correct, answers):
        self.id = int(id_)
        self.prompt = prompt
        self.times_asked = int(times_asked)
        self.times_correct = int(times_correct)
        self.answers = answers

    def percent_correct(self) -> str:
        # ex: "34%"
        pass




"Fråga 10. [34% har svarat rätt] Vad är en int?"

ex_q = {'id': '1',
        'prompt': 'Vilken funktion använder du för att skriva ut text i terminalen?',
        'times_asked': '35',
        'times_correct': '16',
        'answers':
            [{'answer': 'print',
              'correct': True},
             {'answer': 'input',
              'correct': False},
             {'answer': 'import',
              'correct': False},
             {'answer': 'sys.exit',
              'correct': False}]}


def get_questions():
    response = requests.get(QUIZ_URL)
    return response


def parse_question(q) -> Question:
    return Question(q['id'], q['prompt'], q['times_asked'], q['times_correct'], q['answers'])

if __name__ == '__main__':
    question = parse_question(ex_q)

    print(question.prompt)
    print(type(question.id))
    print(type(question))
    print(question.answers)
    # res = get_questions()
    # print(res.json())
    # questions = res.json()
    #
    # print(questions['questions'][0]['prompt'])

class Answer:
    # Implementera klassen Answer
    # Vilka attribut skall den ha?
    # Vilka metoder behöver vi?
    answer: str
    correct: bool

    def __init__(self, answer, correct):
        self.answer = answer
        self.correct = correct

    def __str__(self):
        return self.answer


class Question:
    id: int
    prompt: str
    times_asked: int
    times_correct: int
    answers: list[Answer]

    def __init__(self, id_, prompt, times_asked, times_correct, answers: list[Answer]):
        self.id = int(id_)
        self.prompt = prompt
        self.times_asked = int(times_asked)
        self.times_correct = int(times_correct)
        self.answers = answers

    def percent_correct(self) -> str:
        return f"{self.times_correct / self.times_asked:.0%}"

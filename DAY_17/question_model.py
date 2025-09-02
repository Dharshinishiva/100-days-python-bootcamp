class Question:  # a class called question is created

    def __init__(self, text, answer):

        self.text = text
        self.answer = answer

    def __repr__(self):  # or __str__
        return f"Question(text={self.text!r}, answer={self.answer!r})"

class LetterState:
    def __init__(self, character: str):
        self.character: str = character
        self.isInWord: bool = False
        self.isInPosition: bool = False

    def __repr__(self):
        return f"[{self.character} isInWord: {self.isInWord} isInPosition: {self.isInPosition}]"
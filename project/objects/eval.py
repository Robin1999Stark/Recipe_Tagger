from typing import Dict


class PREvalData():
    def __init__(self, all: float, singles: Dict[str, float]) -> None:
        self.all = all
        self.singles = singles

    def print(self):
        print(f"All: {self.all}")
        print(f"Singles: ")
        for k, v in list(self.singles.items()):
            print(f"{k}: {v}")


class EvalData():
    def __init__(self, title: str, accuracy: float, precision: PREvalData, recall: PREvalData, f1_score: float):
        self.title = title
        self.accuracy = accuracy
        self.precision = precision
        self.recall = recall
        self.f1_score = f1_score

    def print(self):
        print(f"Evaluation: {self.title}")
        print(f"Accuracy: {self.accuracy}")
        print(f"Precision: ")
        self.precision.print()
        print(f"Recall: ")
        self.recall.print()
        print(f"f1_score: {self.f1_score}")

from ..objects.receipe import Receipe

class LabelExtractorInterface:
    def __init__(self, receipe: Receipe):
        self.receipe = receipe
    
    def run(self) -> Receipe:
        """Run"""
        pass
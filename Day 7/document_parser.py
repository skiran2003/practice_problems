from abc import ABC,abstractmethod
class DocumentParser(ABC):
    @abstractmethod
    def parse(self,filepath):
        pass

class PDFParser(DocumentParser):
    def parse(self,filepath):
        if '.pdf' in filepath:
            print(f"Parsing pdf file: {filepath}")

class WordParser(DocumentParser):
    def parse(self,filepath):
        if '.doc' in filepath:
            print(f"Parsing word file: {filepath}")

parsers=[PDFParser(),WordParser()]
for parser in parsers:
    parser.parse("sample_file.pdf")

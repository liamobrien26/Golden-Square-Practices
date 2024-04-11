class GrammarStats:
    def __init__(self):
        self.total_texts_checked = 0
        self.passed_texts_count = 0
        
    def check(self,text):
        self.total_texts_checked += 1
        for char in text:
            if char.isupper():
                self.passed_texts_count +=1
                return True
        return False

    def percentage_good(self):
        if self.total_texts_checked == 0:
            return 0
        return (self.passed_texts_count / self.total_texts_checked) * 100
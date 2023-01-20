class Students:    
    def __init__(self, name, group_number, score):
        self.name = name
        self.group_number = group_number
        self.score = score
        def __str__(self):
            return f'name: {self.name}, group_number: {self.group_number}, score: {self.score}, scholarship: {self.scholarship}'    


class Bakalavriat(Students):
    def __init__(self, name, group_number, score):
        super().__init__(name, group_number, score)
        self.scholarship()

    def scholarship(self):
        score = self.score
        if score == 5:
            self.scholarship = 3000
        elif 4 <= score < 5:
            self.scholarship = 2000
        elif 3 <= score < 4:
            self.scholarship = 1500


class Aspirantura(Students):
    def __init__(self, name, group_number, score):
        super().__init__(name, group_number, score)
        self.scholarship()

    def scholarship(self):
        score = self.score
        if score == 5:
            self.scholarship = 5000
        elif 4 <= score < 5:
            self.scholarship = 4500
        elif 3 <= score < 4:
            self.scholarship = 3500

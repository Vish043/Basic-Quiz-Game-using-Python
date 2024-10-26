import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.total_questions = len(questions)

    def shuffle_options(self, options):
        random.shuffle(options)
        return options

    def ask_question(self, question_data):
        question, options, correct_answer = question_data
        shuffled_options = self.shuffle_options(options.copy())  # Shuffle options for this question
        print(f"\n{question}")
        for i, option in enumerate(shuffled_options):
            print(f"{i + 1}. {option}")

        try:
            answer = int(input("Enter the option number: "))
            selected_option = shuffled_options[answer - 1]
        except (ValueError, IndexError):
            print("Invalid input! Moving to the next question.")
            return False

        if selected_option == correct_answer:
            print("Correct!")
            return True
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")
            return False

    def run_quiz(self):
        random.shuffle(self.questions)  # Shuffle the questions before starting the quiz
        for cnt, question_data in enumerate(self.questions):
            if cnt == 10:  # Limit to 10 questions
                break
            if self.ask_question(question_data):
                self.score += 1

    def display_result(self):
        percentage = (self.score / 10) * 100
        print(f"\nYou got {self.score} out of {10} correct.")
        print(f"Your percentage: {percentage:.2f}%")

# Define the quiz questions
quiz_questions = [
    ("Who developed the theory of relativity?", ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"], "Albert Einstein"),
    ("What is the capital city of Japan?", ["Seoul", "Beijing", "Tokyo", "Bangkok"], "Tokyo"),
    ("Who is known as the father of computers?", ["Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs"], "Charles Babbage"),
    ("Which planet is known as the 'Red Planet'?", ["Mars", "Jupiter", "Venus", "Saturn"], "Mars"),
    ("What is the square root of 64?", ["6", "8", "10", "12"], "8"),
    ("Which country is the largest by land area?", ["China", "USA", "Canada", "Russia"], "Russia"),
    ("What year did World War II end?", ["1941", "1945", "1939", "1950"], "1945"),
    ("Which continent is known as the 'Dark Continent'?", ["Asia", "Africa", "South America", "Australia"], "Africa"),
    ("What gas do plants absorb from the atmosphere?", ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "Carbon Dioxide"),
    ("Which planet has the most moons?", ["Earth", "Mars", "Jupiter", "Saturn"], "Saturn"),
    ("Which year did the Titanic sink?", ["1905", "1912", "1920", "1935"], "1912"), 
    ("What is the freezing point of water in Celsius?", ["0°C", "32°C", "100°C", "-32°C"], "0°C"),
    ("Which country is known as the Land of the Rising Sun?", ["China", "Japan", "South Korea", "Thailand"], "Japan"), 
    ("What is the largest desert in the world?", ["Gobi Desert", "Arabian Desert", "Sahara Desert", "Antarctic Desert"], "Antarctic Desert"), 
    ("What is the most spoken language in the world?", ["English", "Spanish", "Mandarin", "Hindi"], "Mandarin"), 
    ("What is the most spoken language in the world?", ["English", "Spanish", "Mandarin", "Hindi"], "Mandarin"),
]

# Create a quiz instance and run it
quiz = Quiz(quiz_questions)
quiz.run_quiz()
quiz.display_result()
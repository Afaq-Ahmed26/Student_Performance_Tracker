class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self):
        # Define the passing threshold (e.g., 40)
        passing_score = 33
        return all(score >= passing_score for score in self.scores)

    def display_performance(self):
        average = self.calculate_average()
        status = "Passing" if self.is_passing() else "Needs Improvement"
        print(f"Student: {self.name}, Average Score: {average:.2f}, Status: {status}")

class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        if not self.students:
            return 0
        total_average = sum(student.calculate_average() for student in self.students.values())
        return total_average / len(self.students)

    def display_student_performance(self):
        if not self.students:
            print("No students to display.")
            return
        for student in self.students.values():
            student.display_performance()

def main():
    tracker = PerformanceTracker()
    print("Welcome to the Student Performance Tracker")
    
    while True:
        # Get the student's name
        name = input("Enter the student's name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break

        # Initialize an empty list to store scores for three subjects
        scores = []
        subjects = ["Math", "Science", "English"]
        
        for subject in subjects:
            while True:
                try:
                    # Prompt for score and convert to integer
                    score = int(input(f"Enter {name}'s score in {subject}: "))
                    if 0 <= score <= 100:
                        scores.append(score)
                        break
                    else:
                        print("Score should be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

        # Add the student and their scores to the PerformanceTracker
        tracker.add_student(name, scores)
        print(f"Added {name} to the tracker.\n")

    # Display student performances
    print("\nStudent Performance Summary:")
    tracker.display_student_performance()

    # Calculate and display the class average
    class_average = tracker.calculate_class_average()
    print(f"\nClass Average Score: {class_average:.2f}")

# Run the main function to start the tracker
main()

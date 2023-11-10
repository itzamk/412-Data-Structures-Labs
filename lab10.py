class StrengthTrainingTracker:
    def __init__(self):
        self.workouts = {}  # Dictionary to hold workout data
        self.exercises_done = set()  # Set to hold unique exercises

    def add_workout(self, date, exercise, sets, reps, weight):
        # Add the exercise to the set of exercises done
        self.exercises_done.add(exercise)
        
        # If the date doesn't exist in the workouts dictionary, create a new list
        if date not in self.workouts:
            self.workouts[date] = []
        
        # Append the exercise details to the list of workouts on that date
        self.workouts[date].append({
            'exercise': exercise,
            'sets': sets,
            'reps': reps,
            'weight': weight
        })

    def get_workout(self, date):
        # Return the workout details for the given date
        return self.workouts.get(date, "No workout found on this date.")

    def update_workout(self, date, exercise, sets, reps, weight):
        # Check if the workout exists for the given date
        if date in self.workouts:
            for workout in self.workouts[date]:
                if workout['exercise'] == exercise:
                    workout['sets'] = sets
                    workout['reps'] = reps
                    workout['weight'] = weight
                    return "Workout updated."
            return "Exercise not found on this date."
        else:
            return "No workout found on this date."
    
    def list_exercises(self):
        # Return a list of all unique exercises done
        return list(self.exercises_done)

# Example usage:
stt = StrengthTrainingTracker()
stt.add_workout('2023-11-07', 'Bench Press', 3, 10, 185)
stt.add_workout('2023-11-07', 'Deadlift', 2, 5, 225)
stt.add_workout('2023-11-09', 'Squats', 4, 8, 200)

print(stt.get_workout('2023-11-07'))
stt.update_workout('2023-11-07', 'Bench Press', 3, 12, 185)
print(stt.get_workout('2023-11-07'))
print(stt.list_exercises())

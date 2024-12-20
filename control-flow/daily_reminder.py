# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task using if-elif-else
if priority == "high":
    reminder = f"'{task}' is a high priority task."
elif priority == "medium":
    reminder = f"'{task}' is a medium priority task."
elif priority == "low":
    reminder = f"'{task}' is a low priority task."
else:
    reminder = "Invalid priority level entered."

# Modify the reminder based on time sensitivity
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
elif time_bound == "no":
    reminder += " Consider completing it when you have free time."
else:
    reminder += " Time-sensitivity information is unclear."

# Print the customized reminder
print("\nReminder:", reminder)


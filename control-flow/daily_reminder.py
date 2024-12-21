# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use if-elif-else for priority
if priority == "high":
    message = f"'{task}' is a high priority task."
elif priority == "medium":
    message = f"'{task}' is a medium priority task."
elif priority == "low":
    message = f"'{task}' is a low priority task."
else:
    message = f"'{task}' has an undefined priority level."

# Check time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += " Consider completing it when you have free time."

# Print the reminder
print(f"Reminder: {message}")


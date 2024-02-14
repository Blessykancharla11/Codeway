import tkinter as tk
from tkinter import messagebox

# Create a function to check the answer and update the score
def check_answer():
    global score
    global question_no
    
    selected_option = selected_option_var.get()
    
    # Check if question number is valid
    if question_no in correct_answers:
        correct_answer = correct_answers[question_no]
        
        if selected_option == correct_answer:
            score += 1
            messagebox.showinfo("Correct", "You got 1 point! Well done!")
        else:
            messagebox.showerror("Incorrect", f"Wrong answer! The correct answer is: {options[question_no][correct_answer]}")
        
        # Move to the next question
        question_no += 1
        
        if question_no <= 5:
            display_question()
    else:
        # End of the quiz
        messagebox.showinfo("Quiz Finished", f"Your final score is: {score} out of 5")
        window.destroy()  # Close the window after finishing the quiz

# Function to display the next question
def display_question():
    question_label.config(text=f"Question {question_no}: {questions[question_no]}")
    for i in range(4):
        option_buttons[i].config(text=options[question_no][i+1])

# Initialize global variables
score = 0
question_no = 1

# Define questions, options, and correct answers
questions = {
    1: 'What does CPU stand for?',
    2: 'What does GPU stand for?',
    3: 'What does RAM stand for?',
    4: 'What does PSU stand for?',
    5: 'What does ROM stand for?'
}

options = {
    1: {2: 'Central Processing Unit', 1: 'Central Processor Unit', 3: 'Computer Personal Unit', 4: 'Central Process Unit'},
    2: {3: 'Graphics Processing Unit', 2: 'Graphics Processor Unit', 1: 'Graphics Process Unit', 4: 'Graphical Processing Unit'},
    3: {4: 'Random Access Memory', 2: 'Randomly Accessible Memory', 3: 'Read Access Memory', 1: 'Readily Accessible Memory'},
    4: {1: 'Power Supply Unit', 2: 'Power Source Unit', 3: 'Processing Supply Unit', 4: 'Powerful Supply Unit'},
    5: {2: 'Read Only Memory', 1: 'Random Operation Memory', 3: 'Read Operation Memory', 4: 'Real Operation Memory'}
}

correct_answers = {
    1: 2,
    2: 3,
    3: 4,
    4: 1,
    5: 2
}

# Create the main window
window = tk.Tk()
window.title("Quiz Game")

# Set window size and position
window.geometry("500x300")
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x_offset = (window.winfo_screenwidth() - width) // 2
y_offset = (window.winfo_screenheight() - height) // 2
window.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

# Set background color
window.config(bg="#ffffff")  # White background

# Create a label for the question
question_label = tk.Label(window, text=f"Question {question_no}: {questions[question_no]}", bg="#ffffff", fg="#000000")
question_label.pack(pady=(50, 10))  # Add vertical padding to center the label

# Create radio buttons for options
selected_option_var = tk.IntVar()
option_buttons = []
for i in range(4):
    option_button = tk.Radiobutton(window, text='', variable=selected_option_var, value=i+1, bg="#ffffff", fg="#000000")
    option_button.pack(anchor='w')
    option_buttons.append(option_button)

# Create a button to submit the answer
submit_button = tk.Button(window, text="Submit", command=check_answer, bg="#008000", fg="#ffffff")  # Green button
submit_button.pack(pady=5)

# Create a button to close the window
close_button = tk.Button(window, text="Close", command=window.destroy, bg="#FF0000", fg="#ffffff")  # Red button
close_button.pack(pady=5)

# Display the first question
display_question()

# Run the Tkinter event loop
window.mainloop()

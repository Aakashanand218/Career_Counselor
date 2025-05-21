import json
import tkinter as tk
from tkinter import messagebox, ttk
from counselor import get_career_recommendation

# Predefined options (expanded to match counselor.py logic)
skill_options = [
    "Python", "Java", "Data Analysis", "Machine Learning", "Web Development",
    "Frontend", "Backend", "Mobile Development", "Networking", "Cloud", "Social Media"
]
interest_options = [
    "AI", "Web", "Mobile Apps", "Gaming", "Data Science", "Cybersecurity", "DevOps",
    "Game Development", "Finance", "Graphic Design", "Marketing", "Education", "Law",
    "Biology", "Entrepreneurship"
]
strength_options = [
    "Problem Solving", "Creativity", "Teamwork", "Leadership", "Communication",
    "Economics", "Writing", "Teaching", "Debate", "Medicine"
]

def get_recommendation():
    name = entry_name.get()
    skill = skill_var.get()
    interest = interest_var.get()
    strength = strength_var.get()

    profile = {
        "name": name,
        "skills": [skill],
        "interests": [interest],
        "strengths": [strength]
    }

    recommendation = get_career_recommendation(profile)
    messagebox.showinfo("Career Recommendation", f"{recommendation}")

# UI Setup
root = tk.Tk()
root.title("AI Career Counselor")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, padx=20, pady=20, bg="#ffffff", relief=tk.RIDGE, bd=2)
frame.pack(pady=20, fill="both", expand=True)

label_title = tk.Label(frame, text="Student Career Input", font=("Arial", 16, "bold"), bg="#ffffff")
label_title.grid(row=0, column=0, columnspan=2, pady=10)

# Input Fields
label_name = tk.Label(frame, text="Name:", bg="#ffffff")
label_name.grid(row=1, column=0, sticky="e")
entry_name = tk.Entry(frame, width=30)
entry_name.grid(row=1, column=1)

# Skills Dropdown
label_skills = tk.Label(frame, text="Skill:", bg="#ffffff")
label_skills.grid(row=2, column=0, sticky="e")
skill_var = tk.StringVar()
skill_menu = ttk.Combobox(frame, textvariable=skill_var, values=skill_options, state="readonly")
skill_menu.grid(row=2, column=1)
skill_menu.current(0)

# Interests Dropdown
label_interests = tk.Label(frame, text="Interest:", bg="#ffffff")
label_interests.grid(row=3, column=0, sticky="e")
interest_var = tk.StringVar()
interest_menu = ttk.Combobox(frame, textvariable=interest_var, values=interest_options, state="readonly")
interest_menu.grid(row=3, column=1)
interest_menu.current(0)

# Strengths Dropdown
label_strengths = tk.Label(frame, text="Strength:", bg="#ffffff")
label_strengths.grid(row=4, column=0, sticky="e")
strength_var = tk.StringVar()
strength_menu = ttk.Combobox(frame, textvariable=strength_var, values=strength_options, state="readonly")
strength_menu.grid(row=4, column=1)
strength_menu.current(0)

btn_submit = tk.Button(frame, text="Get Recommendation", command=get_recommendation, bg="#4CAF50", fg="white", font=("Arial", 12))
btn_submit.grid(row=5, column=0, columnspan=2, pady=20)

root.mainloop()

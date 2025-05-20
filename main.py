import json
from counselor import get_career_recommendation
import os

def load_student_profile(file="student.json"):
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)

if __name__ == "__main__":
    print("Looking in:", os.getcwd())
    print("Files:", os.listdir())

    profile = load_student_profile()
    name = profile.get('name', 'the student')
    print(f"\nAI Career Counseling for {name}...\n")
    recommendation = get_career_recommendation(profile)
    print(recommendation)

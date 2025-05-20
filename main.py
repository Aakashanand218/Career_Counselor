import json
from counselor import get_career_recommendation
import os
print("Looking in:", os.getcwd())
print("Files:", os.listdir())

def load_student_profile(file="student.json"):
     with open(file, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    profile = load_student_profile()
    name = profile.get('name', 'the student')
    print(f"\nAI Career Counseling for {name}...\n")
    recommendation = get_career_recommendation(profile)
    print(recommendation)

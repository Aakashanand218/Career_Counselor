import json
from counselor import get_career_recommendation

def load_student_profile(file='student_input.json'):
    with open(file, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    profile = load_student_profile()
    print(f"\nAI Career Counseling for {profile['name']}...\n")
    recommendation = get_career_recommendation(profile)
    print(recommendation)

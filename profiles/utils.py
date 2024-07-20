
from openai import OpenAI

client = OpenAI(api_key='')
import json
import re


def get_match_score(profile1, profile2):
    prompt = f"Compare the following two user profiles and rate their compatibility on a scale of 0 to 100:\n\nProfile 1:\n{json.dumps(profile1, indent=2)}\n\nProfile 2:\n{json.dumps(profile2, indent=2)}"

    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a compatibility scoring assistant."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=150)

    score_text = response.choices[0].message.content.strip()
    print(f"Response from OpenAI: {score_text}")  # For debugging purposes

    # Use regular expressions to find the numeric score in the response text
    match = re.search(r'\b(\d{1,3})\b', score_text)
    if match:
        score = int(match.group(1))
    else:
        score = 0  # Default to 0 if no valid score is found

    return score

def find_best_matches(new_profile, user_profiles):
    matches = []
    for profile in user_profiles:
        score = get_match_score(new_profile, profile)
        matches.append((profile, score))
    matches.sort(key=lambda x: x[1], reverse=True)
    return matches

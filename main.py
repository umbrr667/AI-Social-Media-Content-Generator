from groq import Groq
from dotenv import load_dotenv
import os

from prompts import create_prompt
from utils import save_output

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
while True:
print("="*60)
print("SOCIAL MEDIA CONTENT GENERATOR")
print("="*60)

# Get user input
product = input("\nEnter Product/Brand Name: ")

description = input("\nEnter Product Description: ")

print("\nChoose Platform")
print("1. LinkedIn")
print("2. Instagram")
print("3. X (Twitter)")

choice = input("\nEnter your choice (1-3): ")

if choice == "1":
    platform = "LinkedIn"
elif choice == "2":
    platform = "Instagram"
elif choice == "3":
    platform = "X (Twitter)"
else:
    print("Invalid choice! Defaulting to Instagram.")
    platform = "Instagram"

days = input("\nEnter number of days for Content Calendar: ")
prompt = create_prompt(
    product,
    description,
    platform,
    days
)

completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

response = completion.choices[0].message.content

print("\n" + "="*60)
print("GENERATED CONTENT")
print("="*60)

print(response)

filename = save_output(response)

print("\n" + "="*60)
print(f"Content saved successfully in:\n{filename}")
print("="*60)
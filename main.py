# This code helps to bypass school/admin blocks websites like ChatGPT
# by IbrahemVX2000 on Replit
import openai
import json
import os

openai.api_key = "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"

def askquestion(question):
  completion = openai.Completion.create(
    engine="text-davinci-003",
    prompt=question,
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=0.5,
  )

  response = completion.choices[0].text
  return response

print("Hi, I'm a ChatGPT based AI. How can I help you today?")

while True:
    question = input("You: ")

    if question.lower() == "exit":
      print("Bye! Have a great day.")
      break

    response = askquestion(question)
    print("ChatGPT: " + response)
print("\nMade by IbrahemVX2000")

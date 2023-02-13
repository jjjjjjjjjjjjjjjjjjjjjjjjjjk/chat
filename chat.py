import openai
openai.api_key = "YOUR_API_KEY"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

while True:
    user_input = input("You: ")
    prompt = "You: " + user_input + "\nBot:"
    bot_response = generate_response(prompt)
    print("Bot:", bot_response)

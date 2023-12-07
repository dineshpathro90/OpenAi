import openai

openai.api_key = "YOUR API"

messages = [{"role": "system", "content": "You are a kind, helpful assistant."}]

while True:
    user_message = input("User: ")
    if user_message:
        messages.append({"role": "user", "content": user_message})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

        assistant_reply = chat['choices'][0]['message']['content']
        print(f"ChatGPT: {assistant_reply}")
        
        messages.append({"role": "assistant", "content": assistant_reply})
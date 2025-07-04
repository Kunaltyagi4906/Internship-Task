import datetime

# Chatbot Logic Function
def AI_CHATBOT(user_input):
    user_input = user_input.lower().strip()

    if any(greeting in user_input for greeting in ["hello", "hi", "hey"]):
        return "Hello! How can I assist you today?"
    
    elif "pav bhaji" in user_input:
        return "Ohh! It's a famous street food in Maharashtra. 🌶️"
    
    elif "weather" in user_input:
        return "I'm sorry, I don't have access to real-time weather information."

    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is: {current_time}."

    elif any(emotion in user_input for emotion in ["sad", "happy"]):
        return "I'm here to chat and support you. 😊"

    elif "bored" in user_input:
        return "Ohh! Do your favourite activity or take a short walk. 🚶"

    elif "joke" in user_input:
        return "Why don’t scientists trust atoms? Because they make up everything! 😄"

    elif any(farewell in user_input for farewell in ["bye", "goodbye", "see you"]):
        return "Goodbye! Feel free to come back anytime."

    else:
        return "I'm not sure how to respond to that. Please ask me something else."

# Main Loop
print("🤖 AIBOT: Hello! I'm your AI Chatbot. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("AIBOT: Goodbye! 👋")
        break

    response = AI_CHATBOT(user_input)
    print("AIBOT:", response)

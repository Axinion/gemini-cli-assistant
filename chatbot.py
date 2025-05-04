from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import json

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

chatHistory = [
    SystemMessage(
        content="You are a helpful assistant that helps users with their questions."
    )
]

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    chatHistory.append(HumanMessage(content=user_input))

    result = model.invoke(chatHistory)

    # ✅ Fix: Only append if result.content is non-empty
    if result.content:
        chatHistory.append(AIMessage(content=result.content))
        print(f"AI: {result.content}")
    else:
        print("AI did not return a response.")

# Save chat history to a JSON file
with open("chat_history.json", "w") as f:
    json.dump([message.dict() for message in chatHistory], f, indent=4)


# Save chat history to a file
# with open("chat_history.txt", "w") as f:
#     for message in chatHistory:
#         if isinstance(message, HumanMessage):
#             f.write(f"You: {message.content}\n")
#         elif isinstance(message, AIMessage):
#             f.write(f"AI: {message.content}\n")
#         else:
#             f.write(f"System: {message.content}\n")

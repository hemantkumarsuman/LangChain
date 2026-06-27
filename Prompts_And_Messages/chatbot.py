from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

# while(True):
#     user_input = input("You: ")
#     if user_input.lower() == "exit":
#         print("Exiting the chatbot. Goodbye!")
#         break

#     result = model.invoke(user_input)
#     print("AI:", result.content)


# Problem in above code is that it will not store the context of the conversation. 
# To maintain context, we can use a list to store the conversation history and pass it to the model for each new input.
#  Here's an updated version of the code that maintains context:

# list_of_messages = []

# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "exit":
#         print("Exiting the chatbot. Goodbye!")
#         break

#     list_of_messages.append(user_input)

#     result = model.invoke(list_of_messages)
#     print("AI:", result.content)

# Here we are storing the user input in a list called list_of_messages. 
# Each time the user provides input, we append it to the list. 
# When invoking the model, we pass the entire list of messages, 
# allowing the model to maintain context and provide more coherent responses based on the conversation history.

# But here as chat grows we do not understand which message is from user and which is from AI. 
# So we can use a messages langchain_core.messages module to store the messages in a structured way.

chat_history = [
    SystemMessage(content="You are a helpful assistant that provides information about recipes."),
]

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Exiting the chatbot. Goodbye!")
        break

    chat_history.append(HumanMessage(content=user_input))

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))

    print("AI:", result.content)

print(chat_history)  # This will print the entire conversation history, including system, user, and AI messages.


    
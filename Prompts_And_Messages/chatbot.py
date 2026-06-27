from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

while(True):
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Exiting the chatbot. Goodbye!")
        break

    result = model.invoke(user_input)
    print("AI:", result.content)


# Problem in above code is that it will not store the context of the conversation. 
# To maintain context, we can use a list to store the conversation history and pass it to the model for each new input.
#  Here's an updated version of the code that maintains context:



    
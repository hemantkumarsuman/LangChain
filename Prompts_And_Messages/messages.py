from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

messages = [
    SystemMessage(content="You are a helpful assistant that provides information about recipes."),
    HumanMessage(content="Can you suggest a recipe for a vegetarian pasta dish?"),
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)
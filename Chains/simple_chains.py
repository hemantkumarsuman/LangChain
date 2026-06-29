from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

prompt = PromptTemplate(
    template="Give me 3 interating facts about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model| parser

result = chain.invoke({'topic': 'F1 racing'})

print(result)

# chain.get_graph().print_ascii()


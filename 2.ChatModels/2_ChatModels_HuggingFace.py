from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

from dotenv import load_dotenv
import os
load_dotenv()

print("Hugging Face API Token:", os.getenv("HUGGINGFACEHUB_API_TOKEN"))

model = HuggingFaceEndpoint(
    repo_id="google/flan-t5-large",
    task="text2text-generation",
)

# model = ChatHuggingFace(llm=llm, temperature=0.2)

result = model.invoke("What is the capital of India?")

print(result)
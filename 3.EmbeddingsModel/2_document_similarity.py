from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", output_dimensionality=768)
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about bumrah'

query_vector = embeddings.embed_query(query)
document_vectors = embeddings.embed_documents(documents)

scores = cosine_similarity([query_vector], document_vectors)

index, score = max(enumerate(scores[0]), key=lambda x: x[1])
print(f"Most similar document: {documents[index]}")
print(f"Similarity score: {score}")
print(f"Scores for all documents: {scores}")
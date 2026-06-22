from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", output_dimensionality=768)
text = "Hello, how are you?"

result_vector = embeddings.embed_query(text)
print(result_vector)
print(f"Length of the embedding vector: {len(result_vector)}")



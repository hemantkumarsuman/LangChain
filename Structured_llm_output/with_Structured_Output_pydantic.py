from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

class Student(BaseModel):
    name: str = Field(description="Name of the student")
    age: int = Field(description="Age of the student")
    grade: str = Field(description="Grade of the student")
    subjects: list[str] = Field(description="List of subjects the student is studying")
    gpa: float = Field(description="Grade Point Average of the student")    

structured_student = model.with_structured_output(Student)

result = structured_student.invoke("Hemant scored 95% in his final exams. He is 16 years old and studying in 10th grade. He is taking Math, Science, and English as his subjects. His GPA is 3.8. ")

print(result)
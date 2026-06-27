# json structured output in used when we want to get the output in a structured format like json.
# useful when we want to share the output with other systems or when we want to store the output in a structured format 
# for further processing.
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

schema = {
    "title": "Student",
    "description": "Schema for a student object",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "Name of the student"
        },
        "age": {
            "type": "integer",
            "description": "Age of the student"
        },
        "grade": {
            "type": "string",
            "description": "Grade of the student"
        },
        "subjects": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "List of subjects the student is studying"
        },
        "gpa": {
            "type": "number",
            "description": "Grade Point Average of the student"
        }
    },
    "required": ["name", "age", "grade", "subjects", "gpa"]
}

structured_student = model.with_structured_output(schema)

result = structured_student.invoke("Hemant scored 95% in his final exams. He is 16 years old and studying in 10th grade. He is taking Math, Science, and English as his subjects. His GPA is 3.8. ")

print(result)
print(type(result))  # This will print the type of the result, which should be a dictionary representing the structured output.
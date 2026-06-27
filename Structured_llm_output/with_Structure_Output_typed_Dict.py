from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

class BattingRecord(TypedDict):
    match_type: Annotated[str, "Type of cricket match (e.g., Test, ODI, T20)"]
    matches: Annotated[int, "Number of matches played"]
    innings: Annotated[int, "Number of innings played"]
    runs: Annotated[int, "Total runs scored"]
    average: Annotated[float, "Batting average"]
    strike_rate: Annotated[float, "Strike rate"]
    centuries: Annotated[int, "Number of centuries scored"]
    half_centuries: Annotated[int, "Number of half-centuries scored"]
    wickets: Annotated[Optional[int], "Number of wickets taken (if applicable)"]


structured_batting_record = model.with_structured_output(BattingRecord)


result = structured_batting_record.invoke("Give me cricket batting records of Virat Kohli in a structured format")

print(result)
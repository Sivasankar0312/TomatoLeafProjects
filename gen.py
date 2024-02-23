import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
os.environ['GOOGLE_API_KEY'] = "AIzaSyBgA3p1LfxP27iQuEq--UHSbHJugUEE_MA"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

from IPython.display import Markdown
def function():
    text="tomato leaf disease early blight?"
    text2="what is the solution for "+text+"in 100 words write in paragraph"
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    print(text2)
function()
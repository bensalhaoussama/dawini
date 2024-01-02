
import pandas as pd
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_google_genai import GoogleGenerativeAI

df = pd.read_csv('liste_amm.csv')
agent = create_csv_agent(GoogleGenerativeAI(model="models/text-bison-001", google_api_key="AIzaSyAq8MZcFOpr_vs5VRl5bl7T65Mh-ms41f4"), 
                         'liste_amm.csv', 
                         verbose=True)

input_variable = input("Enter your message (type 'exit' to quit): ")
agent.run(input_variable)
    

print("Exiting the application.")
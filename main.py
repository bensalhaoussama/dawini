import google.generativeai as genai

genai.configure(api_key="AIzaSyAq8MZcFOpr_vs5VRl5bl7T65Mh-ms41f4")
llm = genai.GenerativeModel('gemini-pro')
chat = llm.start_chat(history=[])

while True:
    input_variable = input("Enter your message (type 'exit' to quit): ")
    
    if input_variable.lower() == 'exit':
        break

    response = chat.send_message(input_variable)
    print(response.text)

print("Exiting the application.")

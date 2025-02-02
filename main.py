from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from constants import MODEL_NAME, template


model = OllamaLLM(model=MODEL_NAME)
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to AI chatbot, tupe 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        result = chain.invoke({
            "context": context,
            "question": user_input
        })
        print(f"Bot: ", result)
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()
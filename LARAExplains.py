import json
import openai

repository_path = "repository.json"
openai.api_key = "<INPUT API KEY OF OPENAI>"

def getExplanationFromRepository(repository_path,term):
    with open(repository_path) as file:
        data = json.load(file)
       
    if term.lower() in data:
        return "\n" + term + " is " + data[term.lower()]
    else:
        return "not found"


def getExplanationFromChatGPT(term):
    prompt = f"What is the meaning of the word '{term}'? Make it in 1 sentence"

    # Call the OpenAI GPT-3 API
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.0
    )

    # Access the explanation response
    generated_text = response.choices[0].text

    return generated_text


def explainMeThis():
    print("\n")
    print("======================================================")
    print("L.A.R.A. EXPLAINS")
    print("Provides explanation of technical terms")
    print("======================================================")
    print("\n")

    print("L.A.R.A is ready.\n")

    while True:
        print("Input 'quit' to return to Home\n")
        term = input("Enter an unkown term: ")

        if term.lower() == 'quit':
            break

        explanation = getExplanationFromRepository(repository_path,term)

        if explanation == 'not found':
            explanation = getExplanationFromChatGPT(term)
        
        print(explanation)
        print("\n")
        print("===========================================")
        print("\n")
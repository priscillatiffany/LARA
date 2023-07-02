import openai

openai.api_key = '<INPUT API KEY OF OPENAI>'

def summarizeDiscussion(filename):
    print("\n")
    print("======================================================")
    print("L.A.R.A. SUMMARIZES")
    print("Provides summary of meetings")
    print("======================================================")
    print("\n")

    print("L.A.R.A is summarizing.\n")

    input_text = ""
    with open(filename, "r") as file:
        for i in range(3):
            next(file)
        for line in file:
            input_text += line
    
    prompt = f"Summarize: '{input_text}'"

    # Call the OpenAI GPT-3 API
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1500,
        temperature=1.0,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    # Access the summary response
    summary = response.choices[0].text.strip()

    transcriptFile = open(filename, "a")

    transcriptFile.write("\n\n---\n")
    transcriptFile.write("\nMeeting Summary\n\n")
    transcriptFile.write(summary)
    transcriptFile.close()
    print("Summary is ready.\n")
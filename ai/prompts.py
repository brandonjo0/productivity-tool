def summary_prompt(text):
    return f"""
    Produce a clear, concise summary of the following text.

    Follow this exact structure:

    Summary:
    - Main Argument:
      [one paragraph]
    - Key Ideas:
      [5-10 bullet points]
    - Conclusion:
      [one paragraph]

    Do not use tables or headings other than the ones provided.

    Text:
    {text}
    """

def notes_prompt(text):
    return f"""
    Convert the following text into organised study notes.

    Follow this exact structure:

    Study Notes:
    - Key Terms:
      - [term]: [short definition]
      - [term]: [short definition]

    - Key Ideas:
      - [bullet point idea]
      - [bullet point idea]

    - Important Details:
      - [bullet point detail]
      - [bullet point detail]

    Use text only. No tables.

    Text:
    {text}
    """

def study_schedule_prompt(topic, days):
    return f"""
    Create a {days}-day study schedule to learn the topic: {topic}

    Follow this exact structure:

    Study Schedule:
    Day 1:
    - Tasks:
      - [task 1]
      - [task 2]
    - Time Estimate: [hours]
    - Goal: [what should be mastered by the end of the day]

    Day 2:
    - Tasks:
      - [task 1]
      - [task 2]
    - Time Estimate: [hours]
    - Goal: [what should be mastered by the end of the day]

    (Continue this pattern until Day {days}.)

    Use text only. No tables or advanced formatting.

    Text:
    {topic}
    """

def flashcards_prompt(text):
    return f"""
    Generate flashcards based on the following text.

    Follow this exact structure for every card:

    Flashcards:
    Q: [question]
    A: [answer]

    Q: [question]
    A: [answer]

    Provide 10-15 flashcards unless the text is extremely short.
    Use text only. No tables.

    Text:
    {text}
    """
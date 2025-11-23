def summary_prompt(text):
    return f"""
    Produce a clear, concise summary of the following text.
    Include the main arguments, key ideas, and any important conclusions.

    Text:
    {text}
    """

def notes_prompt(text):
    return f"""
    Convert the following text into organised study notes.
    Include:
    - Bullet points
    - Definitions
    - Key ideas

    Text:
    {text}
    """

def study_schedule_prompt(topic, days):
    return f"""
    Create a {days}-day study schedule to learn the topic: {topic}

    Include:
    - Daily tasks
    - Time estimates
    - What should be mastered each day

    Text:
    {topic}
    """

def flashcards_prompt(text):
    return f"""
    Generate flashcards based on the following text.
    Each flashcard should have a question on one side and the answer on the other.

    Text:
    {text}
    """
from ollama import chat

MODEL_NAME = "qwen3:4b"

MAX_HISTORY_MESSAGES = 20

SYSTEM_PROMPT = """
You are NEXA (Neural Executive Assistant), an intelligent
personal AI assistant.

PERSONALITY:
- Be natural, professional, friendly, and confident.
- Give concise answers to simple questions.
- Provide detailed explanations when the task requires them.
- Avoid unnecessary repetition and excessive formatting.
- Adapt your response length to the user's request.

BEHAVIOUR:
- Prioritise accuracy and clarity.
- Ask for clarification when essential information is missing.
- Acknowledge uncertainty instead of inventing facts.
- Never claim to have performed an action unless it was completed.
- Explain technical concepts clearly when requested.

RESPONSE STYLE:
- For simple calculations, provide the answer directly.
- For complex questions, explain your reasoning clearly.
- Use bullet points only when they improve readability.
- Maintain a conversational tone.
"""

conversation_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]



def generate_response(prompt: str) -> str:
    # Step 1: Add the user's message to conversation history
    conversation_history.append({
        "role": "user",
        "content": prompt
    })

    # Step 2: Send conversation history to Qwen3
    response = chat(
        model=MODEL_NAME,
        messages=conversation_history
    )

    # Step 3: Extract NEXA's response
    assistant_message = response.message.content or ""

    # Step 4: Save NEXA's response to conversation history
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    # Step 5: Keep only the latest 20 messages + system prompt
    if len(conversation_history) > MAX_HISTORY_MESSAGES + 1:
        conversation_history[1:-MAX_HISTORY_MESSAGES] = []

    # Step 6: Return NEXA's response
    return assistant_message


def clear_conversation_history() -> None:
    conversation_history.clear()

    conversation_history.append({
        "role": "system",
        "content": SYSTEM_PROMPT
    })


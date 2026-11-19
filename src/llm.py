
from ollama import chat
from src.tools.calculator import calculate


MODEL_NAME = "qwen3:4b"
MAX_HISTORY_MESSAGES = 20
MAX_TOOL_ROUNDS = 5

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
    conversation_history.append({
        "role": "user",
        "content": prompt
    })

    for _ in range(MAX_TOOL_ROUNDS):
        response = chat(
            model=MODEL_NAME,
            messages=conversation_history,
            tools=[calculate]
        )

        conversation_history.append(
            response.message.model_dump(exclude_none=True)
        )

        # No tool requested: return the final answer
        if not response.message.tool_calls:
            assistant_message = response.message.content or ""

            if len(conversation_history) > MAX_HISTORY_MESSAGES + 1:
                conversation_history[1:-MAX_HISTORY_MESSAGES] = []

            return assistant_message

        # Execute each requested tool
        for tool_call in response.message.tool_calls:
            function_name = tool_call.function.name
            arguments = tool_call.function.arguments

            if function_name == "calculate":
                try:
                    result = calculate(**arguments)
                    tool_result = str(result)
                except (ValueError, TypeError) as error:
                    tool_result = f"Calculator error: {error}"
            else:
                tool_result = f"Unknown tool: {function_name}"

            print(f"[TOOL] {function_name}: {tool_result}")

            conversation_history.append({
                "role": "tool",
                "tool_name": function_name,
                "content": tool_result
            })

    # Safety limit: stop after too many tool rounds
    conversation_history.append({
        "role": "assistant",
        "content": "I reached my tool execution limit."
    })

    if len(conversation_history) > MAX_HISTORY_MESSAGES + 1:
        conversation_history[1:-MAX_HISTORY_MESSAGES] = []

    return "I reached my tool execution limit. Please simplify your request."


def clear_conversation_history() -> None:
    conversation_history.clear()

    conversation_history.append({
        "role": "system",
        "content": SYSTEM_PROMPT
    })


from ollama import chat

from src.tools.registry import get_tool_definitions, execute_tool


# Model configuration
MODEL_NAME = "qwen3:4b"

# Memory and tool execution limits
MAX_HISTORY_MESSAGES = 20
MAX_TOOL_ROUNDS = 5


# NEXA personality
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
- Use available tools when accurate calculations or external
  information are required.
- Never invent tool results.


TOOL USAGE:
- When asked for the current date or time, always use get_current_datetime.
- If the user asks for the time on their computer, use timezone="local".
- Never ask for the user's timezone when their local computer time is requested.
- For another city's time, use its IANA timezone identifier.
- Never guess the current date or time.
- Use calculator tools for arithmetic when appropriate.


RESPONSE STYLE:
- For simple calculations, provide the answer directly.
- For complex questions, explain clearly.
- Use bullet points only when they improve readability.
- Maintain a conversational tone.
- Never use emojis, emoticons, or decorative Unicode symbols.
- Use plain text for all responses, including greetings and confirmations.
- Maintain a clean, professional, conversational tone.
"""


# Short-term conversation memory
conversation_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


def trim_conversation_history() -> None:
    """Keep the system prompt and recent conversation messages."""

    if len(conversation_history) > MAX_HISTORY_MESSAGES + 1:
        conversation_history[1:-MAX_HISTORY_MESSAGES] = []


def generate_response(prompt: str) -> str:
    """Generate a response using Qwen3 and registered tools."""

    # Step 1: Store the user's message
    conversation_history.append({
        "role": "user",
        "content": prompt
    })

    # Step 2: Allow multiple rounds of tool execution
    for _ in range(MAX_TOOL_ROUNDS):

        response = chat(
            model=MODEL_NAME,
            messages=conversation_history,
            tools=get_tool_definitions()
        )

        # Step 3: Store the assistant response
        conversation_history.append(
            response.message.model_dump(exclude_none=True)
        )

        # Step 4: Return when no more tools are requested
        if not response.message.tool_calls:

            assistant_message = response.message.content or ""

            trim_conversation_history()

            return assistant_message

        # Step 5: Execute requested tools
        for tool_call in response.message.tool_calls:

            function_name = tool_call.function.name
            arguments = tool_call.function.arguments

            tool_result = execute_tool(
                function_name,
                arguments
            )

            print(f"[TOOL] {function_name}: {tool_result}")

            # Step 6: Send the tool result back to Qwen3
            conversation_history.append({
                "role": "tool",
                "tool_name": function_name,
                "content": tool_result
            })

    # Step 7: Stop if the model requests too many tool rounds
    limit_message = (
        "I reached my tool execution limit. "
        "Please simplify your request."
    )

    # Discard any unfinished tool exchange at the limit
    clear_conversation_history()

    return limit_message


def clear_conversation_history() -> None:
    """Reset conversation memory while preserving NEXA's personality."""

    conversation_history.clear()

    conversation_history.append({
        "role": "system",
        "content": SYSTEM_PROMPT
    })

from src.llm import generate_response

def test_generate_response():
    prompt = "What is artificial intelligence? Answer in one sentence."

    response = generate_response(prompt)

    print("\nNEXA:", response)

    assert isinstance(response, str)
    assert len(response.strip()) > 0


if __name__ == "__main__":
    test_generate_response()

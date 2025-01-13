import openai

openai.api_key = "your_openai_api_key"

def get_support_response(query):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Provide technical support advice for the following issue: {query}",
            max_tokens=150
        )
        support_response = response.choices[0].text.strip()
        if "escalate" in support_response or len(support_response) < 50:
            return "need_ticket"
        return support_response
    except Exception as e:
        return f"Error: {str(e)}"

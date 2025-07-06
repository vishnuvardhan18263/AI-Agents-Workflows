import os
import requests
from dotenv import load_dotenv
# from glom import glom    

load_dotenv()

OPANAI_API_KEY = os.getenv("OPANAI_API_KEY")

def gen_post(topic: str) ->str:
    
    prompt = f"""you are an social media expert and generate a post, {topic}
                """
    
    payload = {
        "model": "gpt=4o",
        "input": prompt
    }
    response = requests.post(
        "https://api.openai.com/v1/responses", 
        json=payload,
        headers={
            "Content Type":"application/json",
            "Authorization": f"Bearer {OPANAI_API_KEY}"
        }
    )
    
    response_text = response.json().get("output",[{}])[0].get("content",[{}])[
        0].get("text","")
    # response_text = glom(response.json(), ("output", [0], "content", [0], "text"), default="")
    # response_text = response.json()["output"][0]["content"][0]["text"]
    return response_text


def main():
    print("Initiating the AI Flow!")
    
    user_input = input("Enter the content:")
    post = gen_post(user_input)
    print(post)

if __name__ == "__main__":
    main()

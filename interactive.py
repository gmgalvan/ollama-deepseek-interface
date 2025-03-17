import requests
import json

def stream_ollama_response(prompt, model="deepseek-r1:8b"):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model,
        "prompt": prompt
    }
    
    # Make a POST request with stream=True to get the response as it comes
    response = requests.post(url, json=data, headers=headers, stream=True)
    
    # Initialize a buffer for complete response
    full_response = ""
    
    # Process the streaming response
    for line in response.iter_lines():
        if line:
            # Decode the JSON data from each line
            json_response = json.loads(line.decode('utf-8'))
            
            # Extract the token/response part
            token = json_response.get("response", "")
            
            # Print without newline and flush immediately to see it in real-time
            print(token, end="", flush=True)
            
            # Append to full response
            full_response += token
            
            # Check if we're done
            if json_response.get("done", False):
                break
    
    print("\n\nComplete response:")
    print(full_response)
    
    return full_response

if __name__ == "__main__":
    # Get user input for the prompt
    user_prompt = input("Enter your prompt: ")
    
    # Optional: Allow user to specify a different model
    model_name = input("Enter model name (press Enter for default 'deepseek-r1:8b'): ")
    if not model_name:
        model_name = "deepseek-r1:8b"
    
    stream_ollama_response(user_prompt, model_name)
import requests
import json

def stream_ollama_chat(prompt, model="deepseek-r1:8b", system_prompt=None):
    url = "http://localhost:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    
    # Create the messages array
    messages = []
    
    # Add system message if provided
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    
    # Add user message
    messages.append({"role": "user", "content": prompt})
    
    data = {
        "model": model,
        "messages": messages,
        "stream": True
    }
    
    # Make a POST request with stream=True
    response = requests.post(url, json=data, headers=headers, stream=True)
    
    # Initialize a buffer for complete response
    full_response = ""
    
    # Process the streaming response
    for line in response.iter_lines():
        if line:
            # Decode the JSON data from each line
            json_response = json.loads(line.decode('utf-8'))
            
            # Extract the message content
            if "message" in json_response:
                token = json_response["message"].get("content", "")
                # Print without newline and flush immediately
                print(token, end="", flush=True)
                full_response += token
            
            # Check if we're done
            if json_response.get("done", False):
                break
    
    print("\n\nComplete response:")
    print(full_response)
    
    return full_response

if __name__ == "__main__":
    # Get user input for the prompt
    user_prompt = input("Enter your message: ")
    
    # Optional: Allow user to specify a system prompt
    system_prompt = input("Enter optional system prompt (press Enter to skip): ")
    if not system_prompt:
        system_prompt = None
    
    # Optional: Allow user to specify a different model
    model_name = input("Enter model name (press Enter for default 'deepseek-r1:8b'): ")
    if not model_name:
        model_name = "deepseek-r1:8b"
    
    stream_ollama_chat(user_prompt, model_name, system_prompt)
import requests
import json

def stream_ollama_chat(messages, model="deepseek-r1:8b"):
    url = "http://localhost:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    
    data = {
        "model": model,
        "messages": messages,
        "stream": True
    }
    
    # Make a POST request with stream=True
    response = requests.post(url, json=data, headers=headers, stream=True)
    
    # Initialize a buffer for complete response
    full_response = ""
    assistant_message = {}
    
    # Process the streaming response
    for line in response.iter_lines():
        if line:
            # Decode the JSON data from each line
            json_response = json.loads(line.decode('utf-8'))
            
            # Extract the message content
            if "message" in json_response:
                assistant_message = json_response["message"]
                token = assistant_message.get("content", "")
                print(token, end="", flush=True)
                full_response += token
            
            # Check if we're done
            if json_response.get("done", False):
                break
    
    print("\n\nComplete response:")
    print(full_response)
    
    # Return the full assistant message to add to context
    if assistant_message:
        return assistant_message
    return {"role": "assistant", "content": full_response}

if __name__ == "__main__":
    # Initialize conversation history
    conversation = []
    
    # Optional: Add a system message
    system_prompt = input("Enter optional system prompt (press Enter to skip): ")
    if system_prompt:
        conversation.append({"role": "system", "content": system_prompt})
    
    # Optional: Model selection
    model_name = input("Enter model name (press Enter for default 'deepseek-r1:8b'): ")
    if not model_name:
        model_name = "deepseek-r1:8b"
    
    # Main conversation loop
    while True:
        # Get user input
        user_message = input("\nYour message (or type 'exit' to quit): ")
        
        if user_message.lower() == 'exit':
            break
        
        # Add user message to conversation
        conversation.append({"role": "user", "content": user_message})
        
        # Get response from Ollama
        assistant_message = stream_ollama_chat(conversation, model_name)
        
        # Add assistant response to conversation history
        conversation.append(assistant_message)
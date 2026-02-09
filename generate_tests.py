import os
from langchain_ollama import OllamaLLM
#
# Initialize the generator
generator = OllamaLLM(model="llama3.2:latest")
#
print("🧪 Starting Synthetic Security Log Generation...")
#
for i in range(1, 101):
    prompt = f"""
    Generate a unique, realistic Nmap or security scan log for test case #{i}.
    Vary the vulnerabilities: sometimes it's an open port 80, sometimes an old SSH version, 
    sometimes an unencrypted database. 
    Make it look like a raw .txt scan output. 
    Be creative but keep it concise.
    """
    
    unique_log = generator.invoke(prompt)
    
    filename = f"logs/synthetic_test_{i}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(unique_log)
    
    print(f"  ✅ Created: {filename}")
#
print("\n🏆 100 unique test cases generated!")
from src.prompts.prompts import START_GM_PROMPT, GM_PROMPT, NPC_PROMPT
from src.llm.g4f_adapter import G4fClient
    
client = G4fClient()

response = client.user_prompt_chat(
    user_prompt=GM_PROMPT,
    stream=True
)
for resp in response:
    print(resp, end="", flush=True)
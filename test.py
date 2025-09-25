from src.agents.npc_agent import NPCAgent
from src.prompts.prompts import game_history, artem

npc_artem = NPCAgent(artem)

print(npc_artem.decide(game_history=game_history))
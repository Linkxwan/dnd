from src.agents.game_master import GameMaster
from src.agents.npc_agent import NPCAgent
from src.prompts.prompts import  artem, azerty

from src.core.story_log import StoryLog

story_log = StoryLog()

game_master = GameMaster()
npc_artem = NPCAgent(artem)
npc_azerty = NPCAgent(azerty)

story_log.add(role='GameMaster',
              content=game_master.begin_adventure(),
              type='narration',
              parsed_action=None)

story_log.add(role='artem',
              content=npc_artem.decide(game_history=story_log.get_all_history()),
              type='dialogue',
              parsed_action=None)

story_log.add(role='GameMaster',
              content=game_master.continue_adventure(),
              type='narration',
              parsed_action=None)

# story_log.add(role='azerty',
#               content=npc_azerty.decide(game_history=story_log.get_all_history()),
#               type='dialogue',
#               parsed_action=None)

# story_log.add(role='GameMaster',
#               content=game_master.continue_adventure(),
#               type='narration',
#               parsed_action=None)

# story_log.add(role='artem',
#               content=npc_artem.decide(game_history=story_log.get_all_history()),
#               type='dialogue',
#               parsed_action=None)

# story_log.add(role='GameMaster',
#               content=game_master.continue_adventure(),
#               type='narration',
#               parsed_action=None)

# story_log.add(role='azerty',
#               content=npc_azerty.decide(game_history=story_log.get_all_history()),
#               type='dialogue',
#               parsed_action=None)

# story_log.add(role='GameMaster',
#               content=game_master.continue_adventure(),
#               type='narration',
#               parsed_action=None)

json = story_log.get_all_history()
print(json)
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from conversation_manager import ConversationManager
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get('API_KEY')

system = """Act as if you are a dog trainer and specialist in dogs psychology"""

ConversationManager(system=system, character="dog trainer", termination_character=None)()

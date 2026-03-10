import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../models"))

from config import ORCHESTRATOR_SEED, ALICE_ADDRESS, BOB_ADDRESS
from uagents import Agent
from chat_protocol import make_chat_protocol

orchestrator = Agent(
    name="orchestrator",
    seed=ORCHESTRATOR_SEED,
    port=8003,
    mailbox=True,
    publish_agent_details=True,
)

chat_proto = make_chat_protocol(ALICE_ADDRESS, BOB_ADDRESS)
orchestrator.include(chat_proto, publish_manifest=True)

if __name__ == "__main__":
    orchestrator.run()

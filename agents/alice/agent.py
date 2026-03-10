import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../models"))

from config import ALICE_SEED
from uagents import Agent
import chat_protocol

alice = Agent(
    name="alice",
    seed=ALICE_SEED,
    port=8001,
    mailbox=True,
    publish_agent_details=True,
)

# -------------------------------------------------------
# YOUR CODE GOES HERE
# This function is called whenever alice receives a message.
# `text` is the incoming message content as a string.
# Return your response as a string.
# -------------------------------------------------------
async def get_response(text: str) -> str:
    return f"Hi from Alice! You said: {text}"

chat_protocol.get_response = get_response
alice.include(chat_protocol.chat_proto, publish_manifest=True)

if __name__ == "__main__":
    alice.run()

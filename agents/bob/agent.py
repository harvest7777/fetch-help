import os
from dotenv import load_dotenv
from uagents import Agent
import chat_protocol

load_dotenv()

bob = Agent(
    name="bob",
    seed=os.getenv("BOB_SEED_PHRASE"),
    port=8002,
    mailbox=True,
    publish_agent_details=True,
)

# -------------------------------------------------------
# YOUR CODE GOES HERE
# This function is called whenever bob receives a message.
# `text` is the incoming message content as a string.
# Return your response as a string.
# -------------------------------------------------------
async def get_response(text: str) -> str:
    return f"Hey from Bob! You said: {text}"

chat_protocol.get_response = get_response
bob.include(chat_protocol.chat_proto, publish_manifest=True)

if __name__ == "__main__":
    bob.run()

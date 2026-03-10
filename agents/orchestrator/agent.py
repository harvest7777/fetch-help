import os
from dotenv import load_dotenv
from uagents import Agent
from uagents_core.identity import Identity
import chat_protocol

load_dotenv()

orchestrator = Agent(
    name="orchestrator",
    seed=os.getenv("ORCHESTRATOR_SEED_PHRASE"),
    port=8003,
    mailbox=True,
    publish_agent_details=True,
)

# Derive alice and bob's addresses from their seeds so we know where to route
ALICE_ADDRESS = Identity.from_seed(seed="soiufisdfkjsjflksdowo24792834", index=0).address
BOB_ADDRESS = Identity.from_seed(seed=str(os.getenv("BOB_SEED_PHRASE")), index=0).address

chat_protocol.ALICE_ADDRESS = ALICE_ADDRESS
chat_protocol.BOB_ADDRESS = BOB_ADDRESS

orchestrator.include(chat_protocol.chat_proto, publish_manifest=True)

if __name__ == "__main__":
    orchestrator.run()

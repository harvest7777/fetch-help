from agents.models.config import ORCHESTRATOR_SEED, ALICE_ADDRESS, BOB_ADDRESS
from agents.models.models import AgentState
from agents.orchestrator.chat_protocol import make_chat_protocol, send_agent_result_back_to_user
from uagents import Agent, Context

orchestrator = Agent(
    name="orchestrator",
    seed=ORCHESTRATOR_SEED,
    port=8003,
    mailbox=True,
    publish_agent_details=True,
)

chat_proto = make_chat_protocol(ALICE_ADDRESS, BOB_ADDRESS)
orchestrator.include(chat_proto, publish_manifest=True)


@orchestrator.on_message(AgentState)
async def handle_agent_response(ctx: Context, sender: str, msg: AgentState):
    await send_agent_result_back_to_user(ctx, msg)


if __name__ == "__main__":
    orchestrator.run()

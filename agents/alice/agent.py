from agents.models.config import ALICE_SEED
from agents.models.models import AgentState
from uagents import Agent, Context

alice = Agent(
    name="alice",
    seed=ALICE_SEED,
    port=8001,
    mailbox=True,
    publish_agent_details=True,
)


def super_cool_alice_workflow(state: AgentState) -> AgentState:
    state.result = f"Alice says: {state.query}"
    return state


@alice.on_message(AgentState)
async def handle_message(ctx: Context, sender: str, msg: AgentState):
    state = super_cool_alice_workflow(msg)
    await ctx.send(sender, state)


if __name__ == "__main__":
    alice.run()

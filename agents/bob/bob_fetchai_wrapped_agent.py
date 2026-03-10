from agents.models.config import BOB_SEED
from agents.models.models import SharedAgentState
from uagents import Agent, Context

bob = Agent(
    name="bob",
    seed=BOB_SEED,
    port=8002,
    mailbox=True,
    publish_agent_details=True,
)


def super_cool_bob_workflow(state: SharedAgentState) -> SharedAgentState:
    state.result = f"Bob says: {state.query}"
    return state


@bob.on_message(SharedAgentState)
async def handle_message(ctx: Context, sender: str, msg: SharedAgentState):
    state = super_cool_bob_workflow(msg)
    await ctx.send(sender, state)


if __name__ == "__main__":
    bob.run()

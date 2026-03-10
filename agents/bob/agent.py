from agents.models.config import BOB_SEED
from agents.models.models import AgentState
from uagents import Agent, Context

bob = Agent(
    name="bob",
    seed=BOB_SEED,
    port=8002,
    mailbox=True,
    publish_agent_details=True,
)


def super_cool_bob_workflow(state: AgentState) -> AgentState:
    state.result = f"Bob says: {state.query}"
    return state


@bob.on_message(AgentState)
async def handle_message(ctx: Context, sender: str, msg: AgentState):
    state = super_cool_bob_workflow(msg)
    await ctx.send(sender, state)


if __name__ == "__main__":
    bob.run()

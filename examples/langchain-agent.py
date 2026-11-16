from langchain.agents import create_agent
from langchain_core.utils.uuid import uuid7


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(model= "bedrock_converse:global.amazon.nova-2-lite-v1:0", 
                    tools=[get_weather])

# it won't use a tool here, verify in the full response
config = {"configurable": {"thread_id": str(uuid7())}}
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the altitude of San Francisco?"}]},
    config=config,
)
print(result)

# it should use a tool here, again check it in the full response
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]},
    config=config,
)
print (result)

# printing only the actual response, without the "metadata"
print(result["messages"][-1].content_blocks)

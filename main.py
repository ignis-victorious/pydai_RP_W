#
#  Import LIBRARIES
from typing import Any

import requests
from pydantic_ai import Agent, AgentRunResult

#  Import FILES

#  ______________________
#


agent: Agent[None, str] = Agent(
    model="google-gla:gemini-2.5-flash",
    instructions="Help users with cat breeds. Be concise.",
)


@agent.tool_plain
def find_breed_info(breed_name: str) -> Any | dict[str, str]:
    """Find information about a cat breed."""
    response: requests.Response = requests.get(url="https://api.thecatapi.com/v1/breeds")
    response.raise_for_status()
    json_response = response.json()
    for breed in json_response:
        if breed["name"] == breed_name:
            return breed
    return {"error": "Breed not found"}


result: AgentRunResult[str] = agent.run_sync(user_prompt="Tell me about the Siamese cats.")
print(result.output)

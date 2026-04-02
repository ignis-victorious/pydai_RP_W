#
#  Import LIBRARIES
from pydantic_ai import Agent, AgentRunResult

#  Import FILES
from models import CityInfo

#  ______________________
#


agent: Agent[None, CityInfo] = Agent(
    model="google-gla:gemini-2.5-flash",
    output_type=CityInfo,
)

result: AgentRunResult[CityInfo] = agent.run_sync(user_prompt="Tell me about Tokyo")
result.output
# CityInfo(
#     name='Tokyo',
#     country='Japan',
#     population=13960000,
#     fun_fact='Tokyo has the most Michelin stars of any city in the world.'
# )


print(f"{result.output.name}, {result.output.country}")
print(f"Population: {result.output.population:,}")
print(f"Fun fact: {result.output.fun_fact}")

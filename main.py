#
#  Import LIBRARIES
from pydantic_ai import Agent, AgentRunResult

#  Import FILES
#  ______________________
#


agent: Agent = Agent(
    model="google-gla:gemini-2.5-flash",
    instructions="You're a Python Expert. Reply in one sentence.",
)

result: AgentRunResult[str] = agent.run_sync(user_prompt="What is Pydantic AI?")
print(result.output)


# def main():
#     print("Hello from pydai-rp-w!")


# if __name__ == "__main__":
#     main()

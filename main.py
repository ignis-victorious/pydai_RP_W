#
#  Import LIBRARIES
from pydantic_ai import Agent

#  Import FILES
#  ______________________
#


agent = Agent(
    "google-gla:gemini-2.5-flash",
    instructions="You're a Python Expert. Reply in one sentence.",
)

result = agent.run_sync("What is Pydantic AI?")
print(result.output)


# def main():
#     print("Hello from pydai-rp-w!")


# if __name__ == "__main__":
#     main()

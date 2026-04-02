#
#  Import LIBRARIES

import requests
from pydantic_ai import Agent, AgentRunResult, RunContext
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider

#  Import FILES
from models import UserDatabase, UserSummary
from settings import settings

#  ______________________
#


#  Create a Provider explicitly with the new key - This "wraps" your API key so GoogleModel doesn't have to look at environment variables.
google_provider = GoogleProvider(api_key=settings.google_api_key)

# Explicitally create the model using the key from my settings - It tells the Agent: "Do not guess. Use THIS key."
model = GoogleModel(model_name="gemini-2.5-flash-lite", provider=google_provider)

agent: Agent[UserDatabase, UserSummary] = Agent(
    model=model,
    # model="google-gla:gemini-2.5-flash",
    output_type=UserSummary,
    deps_type=UserDatabase,
    instructions=(
        "You retrieve user information from an external database. "
        "Use the available tools to gather user info, "
        "then return a structured summary."
    ),
)


@agent.tool
def fetch_user(ctx: RunContext[UserDatabase], user_id: int) -> str:
    """Fetch user profile from the service."""
    try:
        user = ctx.deps.get_user_info(user_id=user_id)
        return str(object=user)
    except requests.HTTPError:
        return f"User with ID {user_id} not found"


db = UserDatabase()
# This print will prove you using the new key
print(f"🔑 Using Key from settings.py: {settings.google_api_key[:8]}...")

try:
    result: AgentRunResult[UserSummary] = agent.run_sync(
        user_prompt="Get a summary for user 7",
        deps=db,  # Inject the database
    )
    print(f"Name: {result.output.name}")
    print(f"Email: {result.output.email}")
    print(f"Company: {result.output.company}")
except Exception as e:
    print(f"\n❌ ERROR: {e}")

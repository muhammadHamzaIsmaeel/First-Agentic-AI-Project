from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from agents.run import RunConfig
from dotenv import load_dotenv
import os
load_dotenv()

@function_tool
async def calculate_numbers(a: int, b: int, operation: str) -> float:
    """
    Performs basic math operations on two numbers.
    
    Args:
        a: First number (e.g., 2)
        b: Second number (e.g., 3)
        operation: Math operation to perform ('add', 'subtract', 'multiply', or 'divide')
    
    Returns:
        Result of the operation as float
    
    Examples:
        calculate_numbers(2, 3, 'add') → 5.0
        calculate_numbers(5, 2, 'subtract') → 3.0
        calculate_numbers(4, 3, 'multiply') → 12.0
        calculate_numbers(10, 2, 'divide') → 5.0
    """
    try:
        if operation == 'add':
            return float(a + b)
        elif operation == 'subtract':
            return float(a - b)
        elif operation == 'multiply':
            return float(a * b)
        elif operation == 'divide':
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return float(a / b)
        else:
            raise ValueError(f"Invalid operation: {operation}")
    except Exception as e:
        raise ValueError(f"Calculation error: {str(e)}")

external_client = AsyncOpenAI(
    api_key=os.getenv("gemini_api_key"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
agent = Agent(name="Assistant", instructions="You are a helpful assistant", tools=[calculate_numbers])
result = Runner.run_sync(agent, "aj ka weather kaisa hai", run_config=config)
print(result.final_output)
# Core Challenge for Module 03
import json
from typing import Callable, Dict, List
from pydantic import BaseModel

class AgentState(BaseModel):
    history: List[str] = []

class Orchestrator:
    def __init__(self, model: Callable[[str], str], tool_registry: Dict[str, Callable]):
        self.model = model
        self.tool_registry = tool_registry

    def run(self, initial_prompt: str) -> str:
        # Implement the orchestration loop
        pass

# --- Simulation Components ---
def simulated_llm(prompt: str) -> str:
    """Simulates an LLM that can either answer or call a tool."""
    if "time" in prompt.lower():
        return json.dumps({"tool_name": "get_time", "arguments": {}})
    return "I'm not sure how to answer that."

def get_time() -> str:
    """A simple tool that returns the current time."""
    return "The current time is 12:00 PM."

# Example Usage:
# tool_registry = {"get_time": get_time}
# orchestrator = Orchestrator(model=simulated_llm, tool_registry=tool_registry)
# final_answer = orchestrator.run("What time is it?")
# assert "12:00 PM" in final_answer

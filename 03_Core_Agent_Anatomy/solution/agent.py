import json
from typing import Callable, Dict, List, Any
from pydantic import BaseModel, Field

class AgentState(BaseModel):
    """
    Manages the agent's memory (conversation history).
    Using Pydantic ensures the state is well-structured.
    """
    history: List[str] = Field(default_factory=list)

    def add_to_history(self, message: str):
        self.history.append(message)

    def get_full_history(self) -> str:
        return "\n".join(self.history)

class Orchestrator:
    """
    The governing process managing planning, memory (state),
    and multi-step execution paths.
    """
    def __init__(self, model: Callable[[str], str], tool_registry: Dict[str, Callable]):
        self.model = model
        self.tool_registry = tool_registry

    def run(self, initial_prompt: str, max_loops: int = 5) -> str:
        """
        Runs the main orchestration loop.
        """
        state = AgentState()
        state.add_to_history(f"User: {initial_prompt}")
        
        for _ in range(max_loops):
            # 1. Call the model with the current history
            prompt = state.get_full_history()
            model_output = self.model(prompt)
            
            # 2. Parse the model's output
            try:
                # Assume tool call if output is valid JSON
                tool_call = json.loads(model_output)
                tool_name = tool_call.get("tool_name")
                
                if tool_name in self.tool_registry:
                    print(f"Orchestrator: Executing tool '{tool_name}'")
                    # 3. Execute the tool and update history
                    tool_function = self.tool_registry[tool_name]
                    result = tool_function() # Simplified: no args
                    state.add_to_history(f"Tool Result: {result}")
                    # Continue the loop to re-prompt the model with the new info
                    continue
                else:
                    # If JSON is not a valid tool, treat as final answer
                    state.add_to_history(f"Assistant: {model_output}")
                    return model_output

            except json.JSONDecodeError:
                # If output is not JSON, it's a final answer
                print("Orchestrator: Received final answer.")
                state.add_to_history(f"Assistant: {model_output}")
                return model_output
        
        return "Agent reached maximum loops without a final answer."

# --- Simulation Components ---

def simulated_llm(prompt: str) -> str:
    """Simulates an LLM that can either answer or call a tool."""
    print(f"\nLLM received prompt:\n---\n{prompt}\n---")
    # If the tool result is in the history, the LLM can now form a final answer
    if "Tool Result:" in prompt:
        return "Based on my tools, the current time is 12:00 PM."
    # Otherwise, if it sees the word "time", it decides to call a tool
    elif "time" in prompt.lower():
        print("LLM decided to call a tool.")
        return json.dumps({"tool_name": "get_time", "arguments": {}})
    
    return "I'm not sure how to answer that."

def get_time() -> str:
    """A simple tool that returns the current time."""
    return "12:00 PM"

# --- Main Execution ---
tool_registry = {"get_time": get_time}
orchestrator = Orchestrator(model=simulated_llm, tool_registry=tool_registry)

final_answer = orchestrator.run("What time is it?")

print(f"\nFinal Answer from Agent: {final_answer}")
assert "12:00 PM" in final_answer
print("\nSolution for Module 3 is correct.")

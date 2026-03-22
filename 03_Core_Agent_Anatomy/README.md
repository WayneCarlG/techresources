# Module 03: Core Agent Anatomy

This module deconstructs an agent into its functional systems. We will build a simplified agent from scratch to understand the interplay between the Model, Tools, and Orchestration.

## Core Concepts
*   **The Architectural Loop:** Model (Brain), Tools (Hands), Orchestration (Nervous System), and Deployment (Body).
*   **Taxonomy of Capabilities:** From single agents (Level 0) to multi-agent systems (Level 3).

## Core Challenge
Your task is to build a `BasicAgent` class that integrates the core components.

1.  Create a `BasicAgent` class that is initialized with a `model` (a function that simulates an LLM call) and a `tool_registry` (a dictionary of callable functions).
2.  Implement a `Pydantic` model for `AgentState` to manage the agent's memory (conversation history).
3.  Implement an `Orchestrator` class with a `run(initial_prompt: str) -> str` method. This method should:
    a.  Call the model with the current history.
    b.  **Parse the model's output.** For this challenge, assume the model can output either a final answer or a JSON string for a tool call (e.g., `{"tool_name": "get_time", "arguments": {}}`).
    c.  If it's a tool call, execute the corresponding function from the `tool_registry`, update the history with the result, and repeat the loop.
    d.  If it's a final answer, return it.

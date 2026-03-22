# Module 01: The Prompt Engineering Layer

This module provides the foundation for steering the "Brain" of the agent. We will explore how to structure prompts to elicit desired behaviors and reasoning patterns from the language model.

## Core Concepts
*   **Prompting Taxonomy:** System, Contextual, and Role Prompting.
*   **Advanced Reasoning Patterns:** Chain-of-Thought (CoT) and ReAct (Reason & Act).
*   **Output Configurations:** Managing non-determinism via Temperature, Top-K, and Top-P.

## Core Challenge
Your task is to implement a `PromptManager` class. This class will be responsible for assembling a final prompt from different components and simulating an LLM call with specific output configurations.

1.  Create a `PromptManager` that can accept a `system_prompt`, `context_prompt`, and `role_prompt`.
2.  Implement a method `generate_react_prompt(thought: str, action: str) -> str` that formats a prompt according to the ReAct framework.
3.  Implement a method `call_llm(prompt: str, temperature: float, top_p: float) -> str` that simulates a call to a language model. For the simulation, it should return a deterministic string but print the sampling parameters (`temperature`, `top_p`) that it *would* have used.

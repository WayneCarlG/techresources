# Module 04: Agent Quality & Observability

This module focuses on transitioning from proofs-of-concept to production-grade reliability. We will build a simple observability stack from scratch to gain a "Glass Box" view into our agent's behavior.

## Core Concepts
*   **The Four Pillars of Quality:** Effectiveness, Efficiency, Robustness, and Safety.
*   **The "Glass Box" View:** Moving beyond final output checks to Trajectory Evaluation.
*   **Technical Observability Stack:** Logging, Tracing, and Metrics.
*   **Automated Evaluation:** Implementing LLM-as-a-Judge.

## Core Challenge
Your task is to implement a `SimpleTracer` and an `LLMAsJudge` class.

1.  Create a `SimpleTracer` class with a `add_span(span_name: str, metadata: dict)` method. A "span" represents a single operation (e.g., an LLM call or a tool call).
2.  Modify the `Orchestrator` from Module 3 to accept this tracer and record spans for each model call and tool execution.
3.  Implement an `LLMAsJudge` class with a method `evaluate(prompt: str, agent_output: str) -> dict`. This method should simulate a call to an LLM to score the agent's output based on a simple rubric (e.g., helpfulness and correctness).
4.  The `Orchestrator`'s `run` method should use the `LLMAsJudge` to evaluate the final answer before returning it.

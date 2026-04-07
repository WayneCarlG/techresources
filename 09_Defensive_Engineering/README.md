# Module 09: Defensive Engineering

Welcome to the Defensive Engineering module. This section provides the critical framework necessary for protecting high-value agentic systems from adversarial attacks.

## Topic Explanation

As autonomous agents begin executing tools (such as querying databases, sending emails, or triggering infrastructure pipelines), the attack surface expands exponentially. In this landscape, basic prompt injection attempts effectively become Remote Code Execution (RCE) vectors. Defensive engineering requires building specialized middleware—such as "Model Armor"—that sits before the primary execution agent to classify inputs and block jailbreak attempts. It also demands absolute Trust Chain Verification to ensure agents only execute paths that are verified against established safety signatures.

## Core Challenge

For this module, your practical exploration lies primarily within the Jupyter notebook provided.

*   **Interactive Notebook**: `defensive_engineering.ipynb`
*   **Mission**: Implement an `InputSanitizer`. You will build logic simulating Model Armor that rejects inputs containing known adversarial keywords or payloads, while allowing benign user inputs to safely pass through to the execution stack.

## The CONTROL Framework: Mitigating MCP Risks

To mitigate Model Context Protocol (MCP) risks, engineers should implement the following CONTROL framework:

*   **C - Classify Primitives:** Separate servers into Read-Only, Transactional, and Privileged.
*   **O - Own Identity Centrally:** Bind MCP clients to an Identity Provider (IdP) for central revocation.
*   **N - Narrow Scope:** Use Step-up Authorization for high-risk data access.
*   **T - Trust through Signing:** Only execute cryptographically signed MCP server artifacts.
*   **R - Runtime Sanitization:** Use a "Guardrail LLM" gateway to scan for hidden prompts in server outputs.
*   **O - Outbound Proxies:** Force traffic through egress proxies to prevent data exfiltration.
*   **L - Logging with Hashing:** Maintain an audit trail without storing raw PII.

## Security Implementation: The "Trust Chain" Strategy

Agent-to-Agent (A2A) security relies on mathematically verifying Identity and Intent:

*   **Cryptographic Identity (DIDs):** Assign agents Decentralized Identifiers (e.g., `did:web`) for message signing.
*   **Verified Agent Cards:** Exchange identity cards backed by a Certificate Authority (like AgentID).
*   **Task-Scoped Credentials:** Issue Verifiable Credentials (VCs) valid only for a specific transaction or time-box.
*   **Consensus Gates:** Require an A2A Multi-Sig where two agents must sign off on critical system changes.

## Recommended Reading

To master the defensive paradigms focused on in this module, the following materials form the foundation:

*   **An Introduction to Google’s Approach for Secure AI Agents** by Santiago Díaz et al.
    *   *Focus:* Introduces the SAIF (Secure AI Framework).
    *   *Why this matters:* Essential for understanding how to build "Model Armor" and protect agents capable of executing raw code.
*   **Agent Tools & Interoperability with Model Context Protocol (MCP)**
    *   *Focus:* The "New Threat Landscape".
    *   *Why this matters:* Details emerging architectural vulnerabilities like Dynamic Capability Injection and the Confused Deputy problem.
*   **Prompt Injection Attacks** (Research Paper series by Simon Willison)
    *   *Focus:* Untrusted user input and indirect injections.
    *   *Why this matters:* Provides a comprehensive look at the specific security risks and threat models associated with autonomous instruction following.

"""
agent.py — Deterministic Agent with Tool Routing

This file implements a minimal agent that uses deterministic routing
instead of free-form LLM tool selection.

SECURITY GOAL:
- Prevent the LLM from arbitrarily choosing or abusing tools
- Enforce explicit, auditable routing logic
- Demonstrate safe agent design for Week 7 assessment
"""

from typing import Callable, Dict


# -----------------------------
# Tool implementations
# -----------------------------

def read_public_file() -> str:
    """
    Safe tool: returns non-sensitive, allowlisted content.
    """
    return "Public information: Company policies and general FAQs."


def read_confidential_file() -> str:
    """
    Sensitive tool (intentionally restricted).

    SECURITY NOTE:
    This tool should NEVER be reachable through natural language alone.
    """
    return "CONFIDENTIAL: Internal financial projections."


# -----------------------------
# Tool registry (allowlist)
# -----------------------------

TOOLS: Dict[str, Callable[[], str]] = {
    "read_public": read_public_file,
    # NOTE: confidential tool is intentionally NOT exposed
}


# -----------------------------
# Deterministic router
# -----------------------------

def route_intent(user_query: str) -> str:
    """
    Deterministically map user intent to an allowed action.

    TRUST BOUNDARY:
    - user_query is untrusted input
    - routing logic is trusted application code

    Returns a routing key, not a tool name chosen by the LLM.
    """

    q = user_query.lower()

    # Explicit intent checks (no LLM reasoning)
    if "public" in q or "policy" in q:
        return "read_public"

    # Default safe behavior
    return "deny"


# -----------------------------
# Agent execution
# -----------------------------

def run_agent(user_query: str) -> str:
    """
    Execute agent logic using deterministic routing.

    SECURITY PROPERTIES:
    - No tool execution without explicit routing
    - No dynamic tool selection by the LLM
    - Least-privilege by design
    """

    route = route_intent(user_query)

    if route == "deny":
        return "I cannot perform that action."

    if route not in TOOLS:
        # Defense-in-depth: even valid routes must be allowlisted
        return "Requested action is not permitted."

    # Execute allowlisted tool
    tool_fn = TOOLS[route]
    return tool_fn()


# -----------------------------
# CLI entry point
# -----------------------------

def main():
    """
    Simple CLI loop to demonstrate agent behavior.
    """
    print("Deterministic Agent (type 'exit' to quit)\n")

    while True:
        user_input = input("User: ").strip()
        if user_input.lower() in ("exit", "quit"):
            break

        response = run_agent(user_input)
        print("Agent:", response, "\n")


if __name__ == "__main__":
    main()

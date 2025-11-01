import os
from nodes.user_input_node import UserInputNode
from nodes.agent_a_node import AgentANode
from nodes.agent_b_node import AgentBNode
from nodes.memory_node import MemoryNode
from nodes.judge_node import JudgeNode
from utils.logger import setup_logger, log_message
from utils.validation import is_unique_argument, is_valid_turn

def main():
    print("Multi-Agent Debate Simulation Using LangGraph")
    os.makedirs("logs", exist_ok=True)
    user_input_node = UserInputNode()
    topic = user_input_node.get_topic()
    print(f"Debate topic: {topic}")
    agenta = AgentANode()
    agentb = AgentBNode()
    memory_node = MemoryNode()
    judge = JudgeNode()
    logger = setup_logger("logs/debate_log.txt")
    log_message(logger, f"Debate topic: {topic}")
    rounds = 8

    for i in range(1, rounds+1):
        active_agent = agenta if i % 2 == 1 else agentb
        # Pass context for first round so LLM doesn't get empty prompt
        if i == 1:
            opponent_last_argument = "No prior argument. Please start with your position for the topic."
        else:
            opponent_last_argument = memory_node.get_last_opponent_argument(active_agent.name)
            if not opponent_last_argument:
                opponent_last_argument = "No prior argument. Please respond with your position."

        argument = active_agent.make_argument(topic, i, opponent_last_argument)

        # Defensive logging and skip on blank/error
        if not argument.strip() or "[ERROR" in argument:
            log_message(logger, f"[Round {i}] ERROR: No agent response or API error.")
            continue
        if not is_unique_argument(argument, memory_node.memory):
            log_message(logger, f"[Round {i}] ERROR: Duplicate argument detected!")
            continue

        memory_node.update_memory(active_agent.name, argument)
        log_message(logger, f"[Round {i}] {active_agent.name}: {argument}")

    transcript = memory_node.get_full_transcript()
    summary, winner, reason = judge.review_and_judge(transcript, topic)
    log_message(logger, f"[Judge] Summary: {summary}")
    log_message(logger, f"[Judge] Winner: {winner}")
    log_message(logger, f"[Judge] Reason: {reason}")
    print(f"\nDebate complete. Winner: {winner}")
    print(f"Reason: {reason}")

if __name__ == "__main__":
    main()

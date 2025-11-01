from utils.llm import generate_agent_argument

class AgentBNode:  # Philosopher
    def __init__(self):
        self.name = "Philosopher"
    def make_argument(self, topic, round_num, opponent_last_argument):
        return generate_agent_argument(self.name, topic, opponent_last_argument, round_num)

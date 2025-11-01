class MemoryNode:
    def __init__(self):
        self.memory = []  # Each entry is a tuple: (agent, text)

    def update_memory(self, agent, argument):
        self.memory.append((agent, argument))

    def get_last_opponent_argument(self, agent):
        # Returns the last argument not by 'agent', or '' if none exist
        for a, arg in reversed(self.memory):
            if a != agent:
                return arg
        return ""

    def get_full_transcript(self):
        # Returns all arguments as a transcript string
        return "\n".join(f"[Round {i+1}] {agent}: {arg}" for i, (agent, arg) in enumerate(self.memory))

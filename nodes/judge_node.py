from utils.llm import generate_judge_verdict

class JudgeNode:
    def review_and_judge(self, transcript, topic):
        judge_output = generate_judge_verdict(transcript, topic)
        # Expecting LLM output with [Summary], [Winner], [Reason] blocks
        summary, winner, reason = "", "", ""
        for line in judge_output.splitlines():
            if line.startswith("[Summary]"):
                summary = line[len("[Summary]"):].strip()
            elif line.startswith("[Winner]"):
                winner = line[len("[Winner]"):].strip()
            elif line.startswith("[Reason]"):
                reason = line[len("[Reason]"):].strip()
        return summary, winner, reason

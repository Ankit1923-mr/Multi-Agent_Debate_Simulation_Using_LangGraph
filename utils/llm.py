import requests
import os
from dotenv import load_dotenv
load_dotenv()
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")

def generate_agent_argument(role, topic, opponent_last_argument, round_num):
    if not OPENROUTER_API_KEY:
        raise ValueError("OPENROUTER_API_KEY not set!")
    # Ensure context always present
    if not opponent_last_argument:
        opponent_last_argument = "No prior argument. Begin the debate with your stance."
    prompt = (
        f"You are debating as a {role} on the topic: \"{topic}\".\n"
        f"Round {round_num}. Your opponent's last argument was:\n"
        f"\"{opponent_last_argument}\"\n"
        "Respond first with a direct rebuttal to their claim, then add a fresh point from your perspective. "
        "Be concise, persuasive, and do not repeat your own previous arguments."
    )
    data = {
        "model": "gpt-4o-mini",   # <-- use supported model
        "messages": [
            {"role": "system", "content": f"You are a highly knowledgeable {role} and a logical debater."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 160,
        "temperature": 0.7
    }
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://openrouter.ai",
        "X-Title": "Debate Simulator"
    }
    try:
        resp = requests.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers, timeout=30)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"LLM API error: {e}")
        return "[ERROR: LLM could not respond.]"

def generate_judge_verdict(transcript, topic):
    prompt = (
        f"The following is a debate transcript between a Scientist and a Philosopher about: \"{topic}\".\n"
        f"Transcript:\n{transcript}\n"
        "As an impartial judge, write a concise summary of the main arguments from both sides, "
        "then declare the winner and provide a logical justification citing points made. "
        "Clearly label your output as:\n"
        "[Summary]: ...\n[Winner]: ...\n[Reason]: ..."
    )
    data = {
        "model": "gpt-4o-mini",  # <-- use supported model here too
        "messages": [
            {"role": "system", "content": "You are an expert debate judge. Be impartial, logical, and reference arguments."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 320,
        "temperature": 0.6
    }
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://openrouter.ai",
        "X-Title": "Debate Judging"
    }
    try:
        resp = requests.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers, timeout=30)
        resp.raise_for_status()
        judge_output = resp.json()["choices"][0]["message"]["content"].strip()
        return judge_output
    except Exception as e:
        print(f"LLM API error (judge): {e}")
        return "[ERROR: LLM could not judge.]"

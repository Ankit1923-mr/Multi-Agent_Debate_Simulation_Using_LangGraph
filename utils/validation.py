def is_unique_argument(argument, memory):
    if argument.strip() == "" or "[ERROR" in argument:
        return False
    return argument not in [arg for (_, arg) in memory]

def is_valid_turn(round_num, agent_name):
    # Odd = Scientist (A); Even = Philosopher (B)
    if round_num % 2 == 1 and agent_name == "Scientist":
        return True
    if round_num % 2 == 0 and agent_name == "Philosopher":
        return True
    return False

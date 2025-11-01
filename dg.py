from graphviz import Digraph

dot = Digraph(comment='Debate DAG')

# Nodes
dot.node('U', 'UserInputNode\n(Topic)')
dot.node('A', 'AgentA\n(Scientist)')
dot.node('B', 'AgentB\n(Philosopher)')
dot.node('M', 'MemoryNode')
dot.node('J', 'JudgeNode')

# Edges (flow)
dot.edge('U', 'M', label='Store topic')
dot.edge('M', 'A', label='Give relevant memory')
dot.edge('A', 'M', label='Argument')
dot.edge('M', 'B', label='Give relevant memory')
dot.edge('B', 'M', label='Argument')

# Debate rounds loop
dot.edge('M', 'J', label='After Round 8\nPass memory')
dot.edge('J', 'M', label='Final judgment (Log/print)')

# Render diagram
dot.render('debate_dag', view=True, format='png')

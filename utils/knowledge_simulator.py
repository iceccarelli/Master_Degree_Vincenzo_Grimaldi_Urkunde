import numpy as np
import pandas as pd

class RLOntologySimulator:
    """
    Simulates the interaction and evolution of an RL-driven ontology for smart grids.
    This is a conceptual simulator to illustrate the principles of the thesis.
    """
    def __init__(self, num_agents=5, num_concepts=10, initial_knowledge_base=None):
        self.num_agents = num_agents
        self.num_concepts = num_concepts
        self.knowledge_base = self._initialize_knowledge_base(initial_knowledge_base)
        self.agent_states = np.random.rand(num_agents, num_concepts) # Agent's understanding of concepts

    def _initialize_knowledge_base(self, initial_kb):
        if initial_kb is not None:
            return initial_kb
        # Randomly initialize a conceptual knowledge base (e.g., concept relationships)
        kb = np.random.randint(0, 2, size=(self.num_concepts, self.num_concepts)) # Adjacency matrix
        np.fill_diagonal(kb, 1) # A concept is related to itself
        return kb

    def simulate_learning_step(self, agent_id, observed_data_concept_id, reward):
        """
        Simulates an RL agent learning from observed data and receiving a reward.
        The agent updates its understanding of the observed concept and related concepts.
        """
        if not (0 <= agent_id < self.num_agents):
            raise ValueError("Invalid agent_id")
        if not (0 <= observed_data_concept_id < self.num_concepts):
            raise ValueError("Invalid observed_data_concept_id")

        # Simple RL update rule: agent's understanding of the concept improves with positive reward
        # and influences related concepts based on the ontology
        learning_rate = 0.1
        self.agent_states[agent_id, observed_data_concept_id] += learning_rate * reward
        self.agent_states[agent_id, observed_data_concept_id] = np.clip(self.agent_states[agent_id, observed_data_concept_id], 0, 1)

        # Propagate learning through the ontology
        for related_concept_id in range(self.num_concepts):
            if self.knowledge_base[observed_data_concept_id, related_concept_id] == 1 and related_concept_id != observed_data_concept_id:
                self.agent_states[agent_id, related_concept_id] += learning_rate * reward * 0.5 # Weaker influence
                self.agent_states[agent_id, related_concept_id] = np.clip(self.agent_states[agent_id, related_concept_id], 0, 1)

    def get_agent_knowledge(self, agent_id):
        return self.agent_states[agent_id]

    def get_overall_knowledge_consensus(self):
        return np.mean(self.agent_states, axis=0)

class GridIntelligenceSimulator:
    """
    Simulates a simplified smart grid environment and the impact of intelligent agents.
    Focuses on concepts like stability and efficiency.
    """\n    def __init__(self, num_nodes=5, initial_stability=0.8, initial_efficiency=0.7):
        self.num_nodes = num_nodes
        self.node_stability = np.full(num_nodes, initial_stability)
        self.node_efficiency = np.full(num_nodes, initial_efficiency)
        self.grid_load = np.random.rand(num_nodes) * 100 # MW

    def apply_intelligent_action(self, node_id, action_strength, action_type=\'stability\'):
        """
        Simulates an intelligent agent's action on a specific grid node.
        Action strength can be positive (improvement) or negative (degradation).
        """
        if not (0 <= node_id < self.num_nodes):
            raise ValueError("Invalid node_id")

        if action_type == \'stability\':
            self.node_stability[node_id] += action_strength * 0.1
            self.node_stability[node_id] = np.clip(self.node_stability[node_id], 0, 1) # Stability between 0 and 1
        elif action_type == \'efficiency\':
            self.node_efficiency[node_id] += action_strength * 0.05
            self.node_efficiency[node_id] = np.clip(self.node_efficiency[node_id], 0, 1) # Efficiency between 0 and 1
        else:
            raise ValueError("Unknown action_type")

    def get_overall_grid_metrics(self):
        return {
            \'average_stability\': np.mean(self.node_stability),
            \'average_efficiency\': np.mean(self.node_efficiency),
            \'total_load\': np.sum(self.grid_load)
        }

    def simulate_time_step(self, external_disturbance=0.01):
        """
        Simulates a time step with some external disturbance affecting stability.
        """
        self.node_stability -= external_disturbance * np.random.rand(self.num_nodes)
        self.node_stability = np.clip(self.node_stability, 0, 1)
        self.grid_load = np.random.rand(self.num_nodes) * 100 # Load changes randomly

if __name__ == "__main__":
    print("\n--- RL Ontology Simulator Example ---")
    rl_sim = RLOntologySimulator()
    print("Initial Agent 0 Knowledge:", rl_sim.get_agent_knowledge(0))

    # Agent 0 observes data related to concept 3 and gets a positive reward
    rl_sim.simulate_learning_step(agent_id=0, observed_data_concept_id=3, reward=0.5)
    print("Agent 0 Knowledge after learning:", rl_sim.get_agent_knowledge(0))
    print("Overall Knowledge Consensus:", rl_sim.get_overall_knowledge_consensus())

    print("\n--- Grid Intelligence Simulator Example ---")
    grid_sim = GridIntelligenceSimulator()
    print("Initial Grid Metrics:", grid_sim.get_overall_grid_metrics())

    # Intelligent agent improves stability at node 2
    grid_sim.apply_intelligent_action(node_id=2, action_strength=0.7, action_type=\'stability\')
    grid_sim.simulate_time_step() # Simulate a time step with disturbance
    print("Grid Metrics after action and time step:", grid_sim.get_overall_grid_metrics())

    # Intelligent agent improves efficiency at node 0
    grid_sim.apply_intelligent_action(node_id=0, action_strength=0.9, action_type=\'efficiency\')
    grid_sim.simulate_time_step()
    print("Grid Metrics after another action and time step:", grid_sim.get_overall_grid_metrics())

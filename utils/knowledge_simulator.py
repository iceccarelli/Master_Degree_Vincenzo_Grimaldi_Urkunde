import numpy as np

class SimpleGridSimulator:
    """
    A very simple simulator illustrating basic ideas from my Master's thesis.
    It shows how reinforcement-learning-style actions can affect smart grid stability.
    """
    def __init__(self, num_nodes=5):
        self.num_nodes = num_nodes
        self.stability = np.full(num_nodes, 0.78)
        self.efficiency = np.full(num_nodes, 0.72)
    
    def apply_action(self, node_id, strength):
        """Simulate a simple RL-inspired improvement on a grid node."""
        if 0 <= node_id < self.num_nodes:
            self.stability[node_id] = min(1.0, self.stability[node_id] + strength * 0.09)
            self.efficiency[node_id] = min(1.0, self.efficiency[node_id] + strength * 0.05)
    
    def get_metrics(self):
        return {
            'avg_stability': round(float(np.mean(self.stability)), 3),
            'avg_efficiency': round(float(np.mean(self.efficiency)), 3)
        }

if __name__ == "__main__":
    print("Simple Grid Simulator")
    sim = SimpleGridSimulator()
    print("Initial metrics:", sim.get_metrics())
    
    sim.apply_action(1, 0.8)
    sim.apply_action(3, 0.6)
    
    print("Metrics after actions:", sim.get_metrics())
    print("\nThis is a basic demonstration only.")

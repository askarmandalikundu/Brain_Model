import numpy as np
import matplotlib.pyplot as plt

class HirayamaDiseaseSimulation:
    def __init__(self):
        # Basic simulation parameters
        self.time_steps = 500  # Total time steps for simulation
        self.disease_progression = 0.0  # Disease progression scale (0-1)
        self.muscle_weakness = 0.0
        self.atrophy = 0.0

        # Neurotransmitter levels (Dopamine, Serotonin, Cortisol)
        self.dopamine_level = 0.5
        self.serotonin_level = 0.5
        self.cortisol_level = 0.5

        # Environmental and Lifestyle factors
        self.stress = 0.0
        self.exercise = 0.5
        self.sleep = 0.7

        # Genetic predisposition factor (randomized for demonstration)
        self.genetic_factor = random.uniform(0.8, 1.2)  # Modify this for individual variability

        # Medication and Treatment effects
        self.medication_effects = {
            "dopamine_agonist": 0.1,
            "neuroinflammatory_inhibitor": 0.05,
        }
        
        # Disease Stages
        self.disease_stage = "Pre-symptomatic"  # Initial stage
        
        # Biomarkers for disease progression (e.g., neurofilament light chain)
        self.neurofilament_light_chain = 0.0  # Starting point
        
        # Cognitive and motor symptoms
        self.cognitive_decline = 0.0
        self.motor_skill_decline = 0.0

    def update_neurotransmitter_levels(self):
        """Update neurotransmitter levels based on interactions and lifestyle."""
        self.dopamine_level += (0.01 * self.exercise - 0.01 * self.stress)
        self.serotonin_level += (0.005 * self.sleep - 0.005 * self.stress)
        self.cortisol_level += (0.02 * self.stress - 0.01 * self.exercise)

        # Bound neurotransmitter levels between 0 and 1
        self.dopamine_level = max(0, min(1, self.dopamine_level))
        self.serotonin_level = max(0, min(1, self.serotonin_level))
        self.cortisol_level = max(0, min(1, self.cortisol_level))

    def apply_medication(self):
        """Apply medication effects to modify neurotransmitter levels."""
        if "dopamine_agonist" in self.medication_effects:
            self.dopamine_level += self.medication_effects["dopamine_agonist"]
        if "neuroinflammatory_inhibitor" in self.medication_effects:
            self.cortisol_level -= self.medication_effects["neuroinflammatory_inhibitor"]

        # Ensure neurotransmitter levels are bounded between 0 and 1
        self.dopamine_level = max(0, min(1, self.dopamine_level))
        self.cortisol_level = max(0, min(1, self.cortisol_level))

    def update_disease_stage(self):
        """Update disease stage based on disease progression and symptoms."""
        if self.disease_progression < 0.3:
            self.disease_stage = "Pre-symptomatic"
        elif self.disease_progression < 0.6:
            self.disease_stage = "Early stage"
        else:
            self.disease_stage = "Late stage"

    def simulate_progression(self):
        """Simulate disease progression based on neurotransmitter levels."""
        self.update_neurotransmitter_levels()
        self.apply_medication()
        self.update_disease_stage()

        # Simulate disease progression based on neurotransmitter levels
        if self.disease_stage == "Pre-symptomatic":
            self.disease_progression += 0.005 * self.genetic_factor
        elif self.disease_stage == "Early stage":
            self.disease_progression += 0.01 * self.genetic_factor
        else:
            self.disease_progression += 0.02 * self.genetic_factor

        # Impact of neurotransmitters on cognitive and motor skills
        self.cognitive_decline += 0.05 * (1 - self.dopamine_level)
        self.motor_skill_decline += 0.05 * (1 - self.serotonin_level)

        # Impact of cortisol on disease progression
        self.muscle_weakness += 0.01 * self.cortisol_level
        self.atrophy += 0.02 * self.cortisol_level

        # Update biomarkers like neurofilament light chain (NFL)
        self.neurofilament_light_chain += self.disease_progression * 0.05

    def run_simulation(self):
    # Track results over time
    time_points = []
    disease_progression = []
    dopamine_levels = []
    serotonin_levels = []
    cortisol_levels = []
    cognitive_decline = []
    motor_skill_decline = []
    neurofilament = []

    # Run simulation for each time step
    for time_step in range(self.time_steps):
        self.simulate_progression()

        # Record data for analysis
        time_points.append(time_step)
        disease_progression.append(self.disease_progression)
        dopamine_levels.append(self.dopamine_level)
        serotonin_levels.append(self.serotonin_level)
        cortisol_levels.append(self.cortisol_level)
        cognitive_decline.append(self.cognitive_decline)
        motor_skill_decline.append(self.motor_skill_decline)
        neurofilament.append(self.neurofilament_light_chain)

        # Optionally, apply medication after every few steps
        if time_step % 50 == 0:
            self.apply_medication()

    # Plot results
    self.plot_results(time_points, disease_progression, dopamine_levels, serotonin_levels, cortisol_levels)

def plot_results(self, time_points, disease_progression, dopamine_levels, serotonin_levels, cortisol_levels):
    """Visualize the simulation results using matplotlib."""
    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.plot(time_points, disease_progression, label='Disease Progression')
    plt.xlabel('Time (steps)')
    plt.ylabel('Disease Progression')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(time_points, dopamine_levels, label='Dopamine Level', color='green')
    plt.plot(time_points, serotonin_levels, label='Serotonin Level', color='blue')
    plt.plot(time_points, cortisol_levels, label='Cortisol Level', color='red')
    plt.xlabel('Time (steps)')
    plt.ylabel('Neurotransmitter Levels')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(time_points, cognitive_decline, label='Cognitive Decline', color='orange')
    plt.plot(time_points, motor_skill_decline, label='Motor Skill Decline', color='purple')
    plt.xlabel('Time (steps)')
    plt.ylabel('Decline')
    plt.legend()

    plt.tight_layout()
    plt.show()

    def introduce_genetic_factors(self):
    """Incorporate genetic factors that affect disease progression."""
    self.genetic_factor = random.uniform(0.9, 1.1)

def environmental_impact(self, stress, exercise, sleep):
    """Modify disease progression based on external environmental impacts."""
    self.stress = stress
    self.exercise = exercise
    self.sleep = sleep

def apply_combined_treatment(self):
    """Apply combination of treatments (e.g., medication and lifestyle factors)."""
    self.apply_medication()
    self.environmental_impact(stress=0.3, exercise=0.7, sleep=0.8)  # Adjust environmental factors

def introduce_genetic_factors(self):
    """Incorporate genetic factors that affect disease progression."""
    self.genetic_factor = random.uniform(0.9, 1.1)  # Slight variations based on genetics

def environmental_impact(self, stress, exercise, sleep):
    """Modify disease progression based on external environmental impacts."""
    self.stress = stress
    self.exercise = exercise
    self.sleep = sleep

def apply_combined_treatment(self):
    """Apply combination of treatments (e.g., medication and lifestyle factors)."""
    self.apply_medication()
    self.environmental_impact(stress=0.3, exercise=0.7, sleep=0.8)  # Adjust environmental factors

if __name__ == "__main__":
    # Create a simulation instance
    simulation = HirayamaDiseaseSimulation()

    # Introduce genetic factors and apply a treatment
    simulation.introduce_genetic_factors()

    # Run the simulation over the defined time steps
    simulation.run_simulation()

    # Plot the results at the end of the simulation
    simulation.plot_results(simulation.time_steps, simulation.disease_progression,
                            simulation.dopamine_level, simulation.serotonin_level,
                            simulation.cortisol_level)

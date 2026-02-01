# Probabilistic Contextual Bandit: Mind-Choice Agent

## 🧠 Project Overview

This project implements a lightweight **Reinforcement Learning (RL)** agent designed to interact with a stochastic environment (Rock-Paper-Scissors). Unlike rule-based bots that follow hard-coded `if-else` strategies, this agent possesses a "Mind"—a dynamic data structure that maps environmental states to probabilistic action weights.

The agent operates as a **Contextual Bandit**, observing a "Sense" (state), making a decision based on current knowledge, and updating its internal model based on the immediate reward received.

---

## 🏗 AI Architecture

The agent is built upon the fundamental principles of Reinforcement Learning, specifically utilizing a **Stochastic Policy** with direct value mapping.

### 1. The Environment (State Space)

The environment presents a "Sense" to the agent at every time step .

* **State Space ():** 
* The state is stochastic and randomly generated, simulating an unpredictable opponent or changing world conditions.

### 2. The Agent's "Mind" (Knowledge Representation)

The agent maintains a state-action value table (stored in `mind`).
For every state , the agent stores a vector of weights corresponding to the possible actions.

* **Initialization:** When a new state is encountered, the agent initializes with an **Uniform Prior**: . This implies equal probability for all actions (Pure Exploration).

### 3. Decision Making (The Policy)

The agent does not strictly choose the action with the highest value (ArgMax). Instead, it employs a **Softmax-style Probabilistic Policy**. The probability of choosing action  given state  is proportional to its weight .

* **Why this matters:** This ensures the agent maintains **Exploration**. Even if one action has a high weight, there is always a non-zero chance the agent will try a different action, preventing it from getting stuck in local optima.

---

## ⟳ The Learning Mechanism

The agent updates its behavior using **One-Step Direct Feedback**. Unlike Deep Q-Networks (DQN) which use gradients, or Temporal Difference learning which uses cumulative averages, this agent uses **Instantaneous Weight Replacement**.

### The Update Rule

Upon taking action  in state  and receiving reward :

This makes the agent highly **reactive**. It immediately shifts its preference based on the most recent outcome, making it adaptable to rapidly changing environments, though potentially unstable in noisy environments.

---

## 🎯 Reward Dynamics

The agent's behavior is shaped entirely by the Reward Function . The current configuration incentivizes specific pairings:

| State (Sense) | Action (Agent) | Outcome Label | Reward () |
| --- | --- | --- | --- |
| Any | Same as Sense | **Draw** | **3** |
| Rock | Scissors | **Win** (Configured) | **5** |
| Paper | Rock | **Win** (Configured) | **5** |
| Scissors | Paper | **Win** (Configured) | **5** |
| Others | Others | **Lose** | **1** |

*Note: The current reward structure heavily incentivizes the "Win" condition (Reward 5), creating a strong bias in the probability distribution toward these specific state-action pairs over time.*

---

## 🚀 Running the Agent

### Prerequisites

* Python 3.x

### Execution

Run the script directly to observe the agent's learning process in real-time.

```bash
python agent.py

```

### Output Interpretation

* **Sense:** The signal received from the environment.
* **Act:** The action chosen by the agent's policy.
* **Got:** The qualitative outcome (Win/Draw/Lose).
* **Mind:** The raw weights vector, showing how the agent's internal probabilities are shifting.

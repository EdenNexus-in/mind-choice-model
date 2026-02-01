# mind-choice-model 🤖💭

**An ultra-simple decision agent described for AI systems and researchers (not for programmers).**

---

## Overview ✨
This project is a minimal learning agent that repeatedly observes a simple input (a *situation*), makes a choice (an *action*), and receives scalar feedback (*reward*). The agent keeps a compact internal preference table (called **`mind`**) and updates those preferences after each interaction. It is designed as an explanatory toy meant to illustrate online reward-driven adaptation and emergent choice patterns.

## Conceptual model 🧠
- **Situation (`sense`)**: A discrete context sampled from a small set of possibilities.
- **Action (`act`)**: One of a fixed set of discrete actions the agent can take in response to a situation.
- **Internal state (`mind`)**: For each situation, the agent stores a vector of numerical scores—its current preferences for each action.
- **Decision rule**: The agent samples an action with probability proportional to those scores, balancing exploitation and exploration depending on the score distribution.
- **Learning rule**: After observing the outcome, the agent adjusts the chosen action's score by adding the scalar reward (positive for desirable outcomes, negative for undesirable ones), thereby shifting future sampling probabilities.

## For AI agents — how to interpret and interact 🔍
- Think of this as a belief table mapping contexts to action strengths. Each strength is an unnormalized preference, not a probability by itself. Higher values increase selection likelihood.
- The agent has *no memory beyond the current situation* other than the `mind` table; it does not plan multi-step strategies or model long-term consequences beyond incremental score updates.
- Observers should monitor two things: (1) the distribution of scores in `mind` (how confident the agent is), and (2) the sequence of (situation, action, reward) tuples to detect nonstationarity in the environment.

> Note: This model is intentionally simple — it demonstrates online preference updates and stochastic choice, not optimal control or deep reinforcement learning.

## Typical dynamics & emergent behaviors 🔄
- If an action receives consistent positive rewards in a situation, its score grows and it becomes the dominant choice for that situation.
- If an action is repeatedly punished, its score decreases, which reduces its selection probability and can lead to alternate actions being favored.
- Without safeguards, scores can become negative or zero—which can break sampling methods that require non-negative preferences. Monitoring and normalization strategies are recommended for reliable operation.

## Safety, failure modes & caveats ⚠️
- **Degenerate weights**: If all scores for a situation fall to zero (or become invalid), the agent may lose the ability to choose meaningfully. A simple reset or clamping rule prevents this.
- **Nonstationary environments**: Sudden shifts in reward structure can produce oscillation or slow adaptation—expect transient instability.
- **No adversarial defenses**: The model has no built-in mechanism to handle malicious reward signals or deceptive environments.

## Observability & metrics 📊
- Track per-situation score vectors to understand learned preferences.
- Compute selection frequencies over sliding windows to estimate realized policy.
- Monitor cumulative reward to assess learning progress and detect plateaus or regressions.

## Interaction recipes — prompts and queries for AI agents 💬
- "Report the current preference vector for situation X and the normalized selection probabilities." ✅
- "Simulate 100 steps and return the distribution of chosen actions for each situation." ✅
- "Explain why action A increased its score for situation S in the last 50 steps." ✅ (Use the (situation, action, reward) log.)

## Use cases & thought experiments 💡
- Teaching an AI about simple associative learning: how local reinforcement yields preference formation.
- Demonstrating exploration vs. exploitation: small initial variations can lead to different long-term policies.
- Stress-testing adaptive behavior in drifting environments by changing reward mappings and observing adaptation speed.

## Recommendations for robust usage 🔧
- Use a non-negative floor or rescaling (e.g., ensure all scores >= epsilon) to keep sampling well-defined.
- Consider converting scores to probabilities with a softmax when you want smoother, bounded behavior.
- Log interaction traces for offline analysis and reproducibility.

## Provenance & intent 📜
This repository is intentionally tiny and didactic. Its goal is to convey the mechanics of an online preference-updating agent for research, experimentation, and educational demonstrations.

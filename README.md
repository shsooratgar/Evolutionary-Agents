# 🧬 Evolutionary Agents

An interactive game where AI agents learn to navigate through obstacle-filled environments using **neuro-evolution**—a combination of neural networks and evolutionary algorithms. Over successive generations, agents improve their survival skills through **selection, crossover, and mutation**.

Each agent is controlled by a small neural network that evolves over time based on its performance (fitness), resulting in more intelligent behaviors for obstacle avoidance and survival.

---

## 🎮 Game Modes

This project includes **three distinct game modes**, each with its own physics and challenges:

| 🚁 Helicopter Mode | 🌌 Gravity Mode | 🚀 Thrust Mode |
|--------------------|------------------|------------------|
| <img src="https://github.com/shsooratgar/Evolutionary-Agents/blob/main/Pics/helicopter.png?raw=true" alt="Helicopter Mode" width="400"> | <img src="https://github.com/shsooratgar/Evolutionary-Agents/blob/main/Pics/gravity.png?raw=true" alt="Gravity Mode" width="400"> | <img src="https://github.com/shsooratgar/Evolutionary-Agents/blob/main/Pics/thrust.png?raw=true" alt="Thrust Mode" width="400"> |

- **Helicopter**: Simulates constant lift; agent must manage vertical motion to avoid obstacles.
- **Gravity**: Natural falling force is applied; agent must time upward motions precisely.
- **Thrust**: Similar to rocket mechanics; requires managing momentum and velocity over time.

---

## 🧠 How It Works

- **Neural Networks**: Each agent has a simple feedforward neural network to make movement decisions based on its current state.
- **Evolutionary Algorithm**:
  - **Fitness Evaluation**: Agents that survive longer and avoid more obstacles receive higher fitness.
  - **Selection**: Better-performing agents are more likely to be selected for reproduction.
  - **Crossover**: Neural weights from selected agents are recombined to create offspring.
  - **Mutation**: Small random changes are introduced to promote diversity and prevent stagnation.

The population evolves over generations, gradually learning to survive better in each game mode.

---

## 📦 Installation & Run

```bash
git clone https://github.com/shsooratgar/Evolutionary-Agents.git
cd Evolutionary-Agents
python main.py
```

*Requires Python 3 and [pygame](https://www.pygame.org/news).*

---

## 🤝 Contributors

Special thanks to:

- [Matin Tavakoli](https://github.com/MatinTavakoli/)
- [Hossein Zaredar](https://github.com/HosseinZaredar)

---

## 📌 Notes

- This project was created as part of a university assignment in **Computational Intelligence**.
- Feel free to fork, adapt, or expand upon the evolutionary logic or game design!

---

## 📷 Screenshots

Check out the evolution in action across game modes in the `Pics/` folder.

---

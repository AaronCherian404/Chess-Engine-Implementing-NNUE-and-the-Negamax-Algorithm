# ♟️ Implementing the Chess Engine using NNUE with Nega-Max Algorithm

An innovative optimization of a computational model through the analogue of a chess engine, integrating **NNUE (Efficiently Updatable Neural Network)** evaluation with the **Nega-Max search algorithm**.  
Our developed chess engine demonstrated **comparably superior performance** to the most powerful open-source chess engine, **Stockfish v16.0**, through intelligent evaluation and adaptive depth heuristics.

> 🏛️ *Published at the IEEE International Conference on Electronics, Computing and Communication Technologies (CONECCT), hosted at the Indian Institute of Science (IISc), Bengaluru.*  
> [View the IEEE Paper →](https://ieeexplore.ieee.org/document/10677087)

---

## 🚀 Project Overview

This project focuses on **enhancing classical search-based chess engines** with a **neuro-adaptive evaluation mechanism** inspired by **NNUE**.  
Unlike traditional handcrafted evaluation functions, NNUE learns optimal board representations, allowing the engine to assess positions with greater accuracy and computational efficiency.

### Key Goals
- Bridge the gap between **symbolic (rule-based)** and **connectionist (neural network)** paradigms.  
- Leverage **Nega-Max** for a cleaner, recursive minimax framework.  
- Optimize **evaluation speed** and **decision accuracy** under real-time constraints.

---

## 🧠 Core Concepts

### 1. NNUE (Efficiently Updatable Neural Network)
- Uses **incrementally updated features** to efficiently re-evaluate board states.  
- Reduces redundant computations during move generation.  
- Trained using high-quality datasets of chess positions and engine evaluations.

### 2. Nega-Max Algorithm
- Simplifies the Minimax approach using symmetry in game theory.  
- Incorporates **alpha-beta pruning** for enhanced search efficiency.  
- Integrates **dynamic depth adjustment** based on position complexity.

### 3. Hybrid Evaluation Strategy
- Combines **neural evaluation** and **heuristic-based scoring**.  
- Implements **adaptive weighting** to balance speed and precision.

---

- **Language:** C++ / Python (depending on implementation layer)  
- **Frameworks:** PyTorch / NumPy  
- **Dataset:** Self-generated and engine-annotated positions  
- **Evaluation Metrics:** Win rate, move accuracy, time per move

## 🧩 Features

- [x] Efficient move ordering and pruning  
- [x] Incremental neural evaluation  
- [x] Parallelized search with dynamic time management  
- [x] Modular design for training new NNUE models  
- [x] Configurable engine parameters for experimentation  


## 📄 Reference

**IEEE Citation:**

> A. M. Cherian, *“Implementing the Chess Engine using NNUE with Nega-Max Algorithm,”*  
> 2024 IEEE International Conference on Electronics, Computing and Communication Technologies (CONECCT), IISc Bengaluru, India, 2024.  
> DOI: [10.1109/CONECCT10677087](https://ieeexplore.ieee.org/document/10677087)

---

## 🧰 Future Work

- Integration of **Reinforcement Learning (RL)** for self-play training.  
- Incorporation of **Monte Carlo Tree Search (MCTS)** hybridization.  
- Implementation of **hardware-optimized NNUE inference** (FPGA/Edge devices).

---

## 🏅 Acknowledgements

Special thanks to the **IEEE CONECCT Conference Team** and the **Indian Institute of Science (IISc)** for providing a platform to present this research.

---

## 📬 Contact

**Author:** Aaron Mano Cherian  
**LinkedIn:** [linkedin.com/in/aaronmanocherian](https://www.linkedin.com/in/aaron-cherian/)  
**Email:** aaron.cherian@columbia.edu  
**Publication:** [IEEE Xplore Link](https://ieeexplore.ieee.org/document/10677087)

---

⭐ *If you found this project interesting, consider giving it a star!*


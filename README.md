# The-King-Algorithm

## Description

An algorithm of king that solves Byzantine generals problem is a type of algorithm that can achieve consensus among multiple parties in a distributed system, even if some of them are faulty or malicious. Byzantine generals problem is a classic problem in distributed computing that illustrates the difficulty of reaching agreement in the presence of unreliable communication and Byzantine faults. Byzantine faults are arbitrary failures or deviations from the expected behavior, such as lying, cheating, or sabotaging.

The King Consensus algorithm, is based on the concept of a leader election protocol. King Consensus is a mechanism that allows a group of parties to elect a leader who proposes a decision for the rest of the group to accept or reject. The leader election is done by randomly selecting one party as the king and having the others send their votes to the king. The king then broadcasts its decision based on the majority vote. King Consensus can tolerate up to one-half of the parties being Byzantine, as long as the communication channels are reliable and unauthenticated.

## Language

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Visualization

A red border means that the nodes are unreliable and are sending incorrect data. Each color means a different decision. In the end, there is only one decision.

https://github.com/Robert-Mal/The-King-Algorithm/assets/72407184/a464cb7d-6d84-4daf-9d14-81ec25639831

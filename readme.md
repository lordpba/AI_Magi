# Evangelion Magi System Simulation

This project is a simulation of the Magi System from the Neon Genesis Evangelion series. It uses the `crewai` package to create agents that represent the three supercomputers of the Magi System: Melchior, Balthasar, and Caspar.

## Code Overview

The script begins by importing necessary modules and setting up the language model to be used for the simulation. The language model is set to "gpt-3.5-turbo" with a temperature of 0.5.

The user is then prompted to input a question. This question is used as the basis for the tasks that the agents will perform.

Next, the `Agent` objects are defined. Each agent represents one of the supercomputers in the Magi System and is assigned a specific role and goal. For example, Melchior's role is 'Scientist' and its goal is 'Conduct technical analysis and provide logical conclusions.' Each agent also has a backstory based on the Evangelion lore.

## Evangelion Lore

In the Neon Genesis Evangelion series, the Magi System is a trio of supercomputers developed by Dr. Naoko Akagi of NERV. Each supercomputer represents a different aspect of Dr. Akagi's personality: Caspar represents her as a woman, Melchior represents her as a scientist, and Balthasar represents her as a mother. The Magi System is used to make all major decisions within NERV, and its consensus-based decision-making process is a key element of the series.

## Dependencies

This project uses several Python packages, including `crewai`, `langchain_openai`, `langchain_community.llms`, and `crewai_tools`. Make sure to install these packages before running the script. You can install them with pip:

# Evangelion Magi System Simulation

This project is a simulation of the Magi System from the Neon Genesis Evangelion series. It uses the `crewai` package to create agents that represent the three supercomputers of the Magi System: Melchior, Balthasar, and Caspar.

## Code Overview

The script begins by importing necessary modules and setting up the language model to be used for the simulation. The language model is set to "gpt-3.5-turbo" with a temperature of 0.5.

The user is then prompted to input a question. This question is used as the basis for the tasks that the agents will perform.

Next, the `Agent` objects are defined. Each agent represents one of the supercomputers in the Magi System and is assigned a specific role and goal. For example, Melchior's role is 'Scientist' and its goal is 'Conduct technical analysis and provide logical conclusions.' Each agent also has a backstory based on the Evangelion lore.

## Evangelion Lore

In the Neon Genesis Evangelion series, the Magi System is a trio of supercomputers developed by Dr. Naoko Akagi of NERV. Each supercomputer represents a different aspect of Dr. Akagi's personality: Caspar represents her as a woman, Melchior represents her as a scientist, and Balthasar represents her as a mother. The Magi System is used to make all major decisions within NERV, and its consensus-based decision-making process is a key element of the series.
Update: added an human intervention into the Diplomacy analysis, the system asks for a feedback, so we have more control on the decision process as some geo-politic is involved.

## Dependencies

This project uses several Python packages, use requirements.txt

## Help
This project is fan made and on going, searching for help!

## Example of a Magi response obtained:

Question: is good to use Ikari as pilot of the Eva01?

Answer: After conducting a thorough analysis of Shinji Ikari's mental and emotional well-being, readiness for responsibilities, and potential traumas associated with piloting Eva01, it is clear that caution must be exercised when considering him as the pilot. While Shinji possesses unique abilities and potential for growth, his struggles with psychological trauma, emotional intimacy issues, and the weight of responsibility pose significant challenges.

To formulate a comprehensive defense strategy, it is imperative to prioritize Shinji's well-being and readiness for the role. Adequate support and resources must be provided to address his emotional struggles and ensure his effectiveness as the pilot of Eva01. Additionally, ethical considerations regarding the impact on his mental health should not be overlooked.

While Shinji's abilities and potential are valuable assets, the decision to use him as the pilot of Eva01 must be made with a balance of strategic advantages and ethical considerations. Proceeding with caution, providing necessary support, and monitoring his well-being will be crucial in ensuring the success of the mission and the safety of all involved.
# Solar-System-Simulation

## Introduction
This project is a 2D physics simulation of the solar system using real physics.

Provided the initial conditions for all planets (mass, position and velocity), the simulation evolves following the Netwon's law of Universal Gravitation. The simulation updates all the parameters at periodic timeframes. At each timeframe, the forces that each planet receives from the others are calculated, and from this information the acceleration vector for each planet can be calculated and the new position and velocity can be derived from it. This methodology is repeated over and over, generating the trajectories of all planets.

If the real conditions for all planets (mass, position and velocity) are provided, the simulation evolves just like the real Solar System.

## Experiment
Lets test how robust is the simulation with the following experiment: set the real attributes of each planet, and let the code run simulating 29.4 Earth years, which is (approximately) the orbital time of Saturn.

In the picture below we can see the result. The pink planet is Saturn, and we can see that it did almost one orbit as expected!

_Disclaimer: I did not set the exact Saturn orbital time in order to not let it traverse a full orbit so it can be seen that it did 1 lap and not multiple ones_


![alt_text](https://github.com/ygbuil/Solar-System-Simulation/blob/master/images/simulation_results.png)

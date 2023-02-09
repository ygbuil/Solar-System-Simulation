# libraries
from dataclasses import dataclass


@dataclass
class Constants:
    '''
    Declares all the constants that will be using during the entire code.

    Parameters
    ----------
    run_time : float
        Total real time to simulate (in Earth years).
    delta_time : float
        Time interval between the recalculation of positions, velocities and
        forces between planets (in seconds). The lower the time interval, the higher the
        accuracy, but also the higher the computational time.
    planets : list
        List of all planets that will be involved in the simulation. Each
        planet is an instance of the class Planet and requires all its initial
        condiftions defined.

    Returns
    -------
    None.

    '''

    run_time: float
    delta_time: float
    planets: int

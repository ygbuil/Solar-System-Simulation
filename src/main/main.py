# libraries
import os
import sys
from pathlib import Path

# root path
path = Path('C:/Users/llorenc.buil/github/Solar-System-Simulation')
os.chdir(path)
if path not in sys.path:
    sys.path.append(path)

# local libraries
from src.constants.constants import c
from src.objects import functions as f


def main(c):
    '''
    Entire simualtion pipeline.

    Parameters
    ----------
    c : instance of class
        Instance of calss Constants that contains all constants.

    Returns
    -------
    None.

    '''

    steps = int(c.run_time*365*24*3600/c.delta_time)

    f.run_simulation(
        planets=c.planets, steps=steps, delta_time=c.delta_time
    )

    f.plot_simulation(planets=c.planets)


# run simulation
if __name__ == '__main__':
    main(c=c)

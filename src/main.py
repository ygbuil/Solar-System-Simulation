# local libraries
import objects.functions as f
from constants.constants import c


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


if __name__ == '__main__':
    main(c=c)

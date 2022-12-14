# libraries
import numpy as np
import matplotlib.pyplot as plt


# classes and functions
class Planet:
    def __init__(self, name, m, p, v):
        '''
        Planet attributes.

        Parameters
        ----------
        name : string
            Planet name.
        m : float
            Planet mass.
        p : numpy array
            2D position vector.
        v : numpy array
            2D velocity vector.

        Returns
        -------
        None.

        '''

        self.name = name
        self.m = m
        self.p = p
        self.p_history = []
        self.v = v


    def total_force(self, planets):
        '''
        Calculate the total gravitational force applied to a planet due to the
        effect of all other planets.

        Parameters
        ----------
        planets : list
            List of all planets.

        Returns
        -------
        F : numpy array
            2D array of the gravitational force resulting of all planet
            interactions.

        '''

        F = np.array([0., 0.])

        for planet in planets:
            if planet == self:
                continue

            new_F = gravitational_force(
                m1=self.m, m2=planet.m, p1=self.p, p2=planet.p
            )
            F += new_F

        return F


    def move_planet(self, planets, delta_time):
        '''
        Moves the planet, updating its postion, velocity, and keeping track of
        its historical positions.

        Parameters
        ----------
        planets : list
            List of all planets.
        delta_time : float
            Time interval between paramaters (positions, speeds, foreces)
            recalculation (in seconds).

        Returns
        -------
        None.

        '''

        self.p = self.p + self.v*delta_time
        self.p_history.append(self.p)
        self.v = self.v + (self.total_force(planets)/self.m)*delta_time


def gravitational_force(m1, m2, p1, p2):
    '''
    Calculates the gravitational force between two bodies.

    Parameters
    ----------
    m1 : int
        Mass of body 1.
    m2 : int
        Mass of body 2.
    p1 : numpy array
        2D array of position coordinates of body 1.
    p2 : numpy array
        2D array of position coordinates of body 2.

    Returns
    -------
    F : numpy array
        2D array of the gravitational force between the two bodies.

    '''

    # distance vector between two planets
    distance_vector = p2 - p1

    # distance modulus
    r = np.linalg.norm(distance_vector)

    # unitary distance vector
    u = distance_vector/r

    # gravitational force
    F = (6.674*10**(-11)*m1*m2)/(r**2) * u

    return F


def run_simulation(planets, steps, delta_time):
    '''
    Run the simulation.

    Parameters
    ----------
    planets : list
        List of all planets.
    steps : int
        Number of steps of the simulation.
    delta_time : float
        Time interval between paramaters (positions, speeds, foreces)
        recalculation (in seconds).

    Returns
    -------
    planets : list
        List of all planets.

    '''

    for _ in range(steps):
        for planet in planets:
            planet.move_planet(planets=planets, delta_time=delta_time)

    return planets


def plot_simulation(planets):
    '''
    Plot simulation results.

    Parameters
    ----------
    planets : list
        List of all planets.

    Returns
    -------
    None.

    '''

    xs = []
    ys = []
    for planet in planets:
        x_planet = [x[0] for x in planet.p_history]
        y_planet = [y[1] for y in planet.p_history]
        xs.append(x_planet)
        ys.append(y_planet)

    figura = plt.figure(figsize=(15, 15))
    for x, y, planet in zip(xs, ys, planets):
        plt.plot(x, y, label=planet.name)
    for x, y in zip(xs, ys):
        plt.scatter(x[-1], y[-1])
    ax = plt.gca()
    ax.set_xlim(-4.6e12, 4.6e12)
    ax.set_ylim(-4.6e12, 4.6e12)
    ax.set_xlabel('x (meters)')
    ax.set_ylabel('y (meters)')
    ax.set_aspect('equal')
    plt.legend(loc='upper left')
    plt.show()


def main(total_time, delta_time, planets):
    '''
    Entire simualtion pipeline.

    Parameters
    ----------
    total_time : float
        Simulated real time elapsed (in seconds).
    delta_time : float
        Time interval between paramaters (positions, speeds, foreces)
        recalculation (in seconds).
    planets : list
        List of all planets.

    Returns
    -------
    None.

    '''

    steps = int(total_time/delta_time)

    planets = run_simulation(
        planets=planets, steps=steps, delta_time=delta_time
    )

    plot_simulation(planets=planets)


# run simulation
main(
    total_time=9e8,
    delta_time=50000.,
    planets=[
        Planet(
            name='Sun', m=1.989e30, p=np.array([0., 0.]), v=np.array([0., 0.])
        ),
        Planet(
            name='Mercury', m=0.33e24, p=np.array([5.7e10, 0.]),
            v=np.array([0., 47900.])
        ),
        Planet(
            name='Venus', m=4.87e24, p=np.array([10.8e10, 0.]),
            v=np.array([0., 35000.])
        ),
        Planet(
            name='Earth', m=5.97e24, p=np.array([15.0e10, 0.]),
            v=np.array([0., 29800.])
        ),
        Planet(
            name='Mars', m=6.42e23, p=np.array([22.8e10, 0.]),
            v=np.array([0., 24100.])
        ),
        Planet(
            name='Jupiter', m=1.89e27, p=np.array([77.9e10 ,0.]),
            v=np.array([0., 13100.])
        ),
        Planet(
            name='Saturn', m=5.68e26, p=np.array([143.0e10 ,0.]),
            v=np.array([0., 9700.])
        ),
        Planet(
            name='Uranus', m=8.68e25, p=np.array([288.0e10 ,0.]),
            v=np.array([0., 6800.])
        ),
        Planet(
            name='Neptune', m=10.24e25, p=np.array([450.0e10 ,0.]),
            v=np.array([0., 5400.])
        )
    ]
)

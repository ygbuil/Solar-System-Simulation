# libraries
import numpy as np

# local libraries
from objects.constants import Constants
from objects import functions as f


c = Constants(
    run_time=29.4,
    delta_time=50000,
    planets = [
        f.Planet(
            name='Sun',
            m=1.989e30,
            p=np.array([0., 0.]),
            v=np.array([0., 0.])
        ),
        f.Planet(
            name='Mercury',
            m=0.33e24,
            p=np.array([5.7e10, 0.]),
            v=np.array([0., 47900.])
        ),
        f.Planet(
            name='Venus',
            m=4.87e24,
            p=np.array([10.8e10, 0.]),
            v=np.array([0., 35000.])
        ),
        f.Planet(
            name='Earth',
            m=5.97e24,
            p=np.array([15.0e10, 0.]),
            v=np.array([0., 29800.])
        ),
        f.Planet(
            name='Mars',
            m=6.42e23,
            p=np.array([22.8e10, 0.]),
            v=np.array([0., 24100.])
        ),
        f.Planet(
            name='Jupiter',
            m=1.89e27,
            p=np.array([77.9e10 ,0.]),
            v=np.array([0., 13100.])
        ),
        f.Planet(
            name='Saturn',
            m=5.68e26,
            p=np.array([143.0e10 ,0.]),
            v=np.array([0., 9700.])
        ),
        f.Planet(
            name='Uranus',
            m=8.68e25,
            p=np.array([288.0e10 ,0.]),
            v=np.array([0., 6800.])
        ),
        f.Planet(
            name='Neptune',
            m=10.24e25,
            p=np.array([450.0e10 ,0.]),
            v=np.array([0., 5400.])
        )
    ]
)

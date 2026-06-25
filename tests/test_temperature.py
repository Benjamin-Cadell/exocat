import numpy as np
from exocat.temperature import Temperature

def test_init():
    # Test initialization with a single temperature value
    temp = Temperature(300)
    assert np.array_equal(temp.temperature, np.array([300]))
    assert temp.classifications is None

    # Test initialization with an array of temperature values
    temp_array = np.array([250, 300, 400])
    temp = Temperature(temp_array)
    assert np.array_equal(temp.temperature, temp_array)
    assert temp.classifications is None

if __name__ == "__main__":
    test_init()
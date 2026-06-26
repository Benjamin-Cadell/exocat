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

def test_classify():
    # Test classification of a single temperature value
    temp = Temperature(300)
    classification = temp.classify()
    assert classification == "warm"

    # Test classification of an array of temperature values
    temp_array = np.array([250, 300, 400])
    temp = Temperature(temp_array)
    classifications = temp.classify()
    expected_classifications = np.array(["cold", "warm", "hot"])
    assert np.array_equal(classifications, expected_classifications)

def test_plot():
    # Test plotting functionality (this will not display the plot in a test environment)
    temp_array = np.array([250, 300, 400])
    temp = Temperature(temp_array)
    temp.classify()  # Classify before plotting
    try:
        temp.plot(bins=10)  # This should not raise any exceptions
    except Exception as e:
        assert False, f"Plotting raised an exception: {e}"

if __name__ == "__main__":
    test_init()
    test_classify()
    test_plot()

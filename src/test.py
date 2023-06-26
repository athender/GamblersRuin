from gambler import RandomWalk, ProbabilityMassFunction

def test_probability_mass_function():
    """
    Test the ProbabilityMassFunction class.
    
    Creates an instance of ProbabilityMassFunction with a predefined probability mass function
    and prints random variables generated from it, as well as the expected value of the distribution.
    """
    pmf = ProbabilityMassFunction({-1: 0.5, 1: 0.3, 10: 0.2})
    print(pmf.get_random_variable(), "\n")
    print(pmf.get_random_variable(), "\n")
    print(pmf.get_random_variable(), "\n")
    print(pmf.get_random_variable(), "\n")
    print(pmf.get_random_variable(), "\n")
    print(pmf.get_expected_value())

    print(str(pmf))


def test_random_walk():
    """
    Test the RandomWalk class.
    
    Creates an instance of RandomWalk with a predefined probability mass function representing
    the game, and simulates the player playing the game with a given initial amount of money
    and number of iterations.
    """
    random_walk = RandomWalk({-2: 0.25, -1: 0.25, 1: 0.25, 2: 0.25})
    random_walk.play_game(200, 50)


if __name__ == '__main__':
    """
    Main entry point of the test script.
    
    Calls the test functions to verify the behavior of the ProbabilityMassFunction and RandomWalk classes.
    """
    test_random_walk()
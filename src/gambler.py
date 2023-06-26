import numpy as np
from random import choices

class ProbabilityMassFunction:
    def __init__(self, pmf = {}):
        """
        Initialize the ProbabilityMassFunction.

        Args:
            pmf (dict): A dictionary representing the probability mass function.
                The keys are the possible outcomes, and the values are their respective probabilities.
        """
        if sum(pmf.values()) != 1:
            raise ValueError("Please enter a valid probability mass function.")

        self.outcomes = list(pmf.keys())
        self.probabilities = list(pmf.values())
        self.cumulative_probs = np.cumsum(self.probabilities)

    def __str__(self):
        """
        Return a string representation of the probability mass function.

        Returns:
            str: A string representation of the probability mass function.
        """
        rep = "-------------------\nDistribution\n-------------------\n"
        for outcome, probability in zip(self.outcomes, self.probabilities):
            rep += f"Chance of gaining/losing {outcome}: {round(100 * probability, 3)}%\n"

        return rep + "-------------------\n"

    def get_random_variable(self):
        """
        Get a random variable based on the probability mass function.

        Returns:
            Any: A random variable selected according to the probability mass function.
        """
        x = np.random.random()
        index = np.searchsorted(self.cumulative_probs, x, side="right")
        return self.outcomes[index]

    def get_expected_value(self):
        """
        Calculate the expected value of the probability mass function.

        Returns:
            float: The expected value.
        """
        expected_value = sum(outcome * probability for outcome, probability in zip(self.outcomes, self.probabilities))
        return round(expected_value, 3)


class RandomWalk:
    def __init__(self, pmf={-1: 0.5, 1: 0.5}, gain_streak_threshold=5, lose_streak_threshold=-5):
        """
        Initialize the RandomWalk game.

        Args:
            pmf (dict): A dictionary representing the probability mass function of the game.
                        The keys are the possible outcomes, and the values are their respective probabilities.
            gain_streak_threshold (int): The threshold for a winning streak.
            lose_streak_threshold (int): The threshold for a losing streak.
        """
        self.pmf = ProbabilityMassFunction(pmf)
        self.money = 0
        self.iterations = 0

        self.streak = 0
        self.gain_streak_threshold = gain_streak_threshold
        self.lose_streak_threshold = lose_streak_threshold

        self.current_gain_streak = 0
        self.current_lose_streak = 0

        self.gain_streaks = set()
        self.lose_streaks = set()
        self.money_set = set()

        self.threshold_gain = gain_streak_threshold
        self.threshold_lose = lose_streak_threshold

        print(str(self.pmf))

    def play_game(self, starting_money, num_iterations):
        """
        Simulate a player playing the game.

        Args:
            starting_money (int): The amount of money the player starts with.
            num_iterations (int): The number of times the player wants to play the game.
        """
        print("Playing Game...")
        self.money = starting_money
        self.iterations = num_iterations

        for i in range(num_iterations):
            result = self.pmf.get_random_variable()

            self.money += result
            self.streak += result

            if result > 0:
                self.current_gain_streak += result
                self.current_lose_streak = 0
                self.gain_streaks.add(self.current_gain_streak)
            else:
                self.current_gain_streak = 0
                self.current_lose_streak += result
                self.lose_streaks.add(self.current_lose_streak)

            self.money_set.add(self.money)

            self.print_game_status(i, self.streak, self.money)

        self.print_final_results(starting_money)

    def print_game_status(self, game_num, streak, money):
        """
        Print the game status based on the streak and money.

        Args:
            game_num (int): The current game number.
            streak (int): The current streak.
            money (int): The current amount of money.
        """
        if streak == self.gain_streak_threshold:
            print(f"Winning streak! {streak} win streak ended in game {game_num + 1}. Player has a total of {money}!")
            self.streak = 0

        if streak == self.lose_streak_threshold:
            print(f"Losing streak! {streak} losing streak ended in game {game_num + 1}. Player has a total of {money}!")
            self.streak = 0

    def print_final_results(self, starting_money):
        """
        Print the final results of the game.

        Args:
            starting_money (int): The amount of money the player started with.
        """
        print("\n-------------------\nResults\n-------------------")
        print(f"\nStarting wealth: ${starting_money}")
        print(f"Final wealth after {self.iterations} games: ${self.money}\n")
        print(f"Biggest win streak:   ${max(self.gain_streaks)}")
        print(f"Biggest lose streak: -${-min(self.lose_streaks)}")


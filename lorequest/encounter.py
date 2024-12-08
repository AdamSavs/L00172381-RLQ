import random
from lorequest.quest_system import Quest


class Encounter:
    """
    Represents an encounter during a quest.
    """

    def __init__(self, quest: Quest):
        self.quest = quest
        self.outcome = None  # Outcome of the encounter
        self.difficulty_modifiers = {"Easy": 2, "Medium": 5, "Hard": 8}

    def start_encounter(self) -> str:
        """
        Simulates an encounter and determines the outcome.

        Returns:
            str: Outcome of the encounter.
        """
        print(f"Encounter during quest: {self.quest.objective}")
        print(f"Difficulty: {self.quest.difficulty}")

        # Roll a 20-sided die to determine success
        player_roll = random.randint(1, 20)
        difficulty_threshold = self.difficulty_modifiers[self.quest.difficulty]

        print(f"You rolled: {player_roll}")
        print(f"Threshold to succeed: {10 + difficulty_threshold}")

        if player_roll >= 10 + difficulty_threshold:
            self.outcome = "success"
            print("You succeeded in the encounter!")
            return "success"
        else:
            self.outcome = "failure"
            print("You failed the encounter.")
            return "failure"

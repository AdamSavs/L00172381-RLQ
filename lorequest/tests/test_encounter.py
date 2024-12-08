import unittest
from unittest.mock import patch
from lorequest.quest_system import Quest
from lorequest.villager_gen import Villager
from lorequest.encounter import Encounter


class TestEncounter(unittest.TestCase):
    def setUp(self):
        # Create a sample quest for testing
        villager = Villager(
            "Aria", "A tale of adventure.", "Mountain Village", "Retrieve the ancient scroll."
        )
        self.quest = Quest(
            quest_giver=villager,
            objective="Retrieve the ancient scroll from the cave.",
            reward="Legendary Sword",
            difficulty="Medium",
        )
        self.encounter = Encounter(self.quest)

    @patch("random.randint", return_value=15)
    def test_successful_encounter(self, mock_randint):
        result = self.encounter.start_encounter()
        self.assertEqual(result, "success")
        self.assertEqual(self.encounter.outcome, "success")

    @patch("random.randint", return_value=5)
    def test_failed_encounter(self, mock_randint):
        result = self.encounter.start_encounter()
        self.assertEqual(result, "failure")
        self.assertEqual(self.encounter.outcome, "failure")


if __name__ == "__main__":
    unittest.main()

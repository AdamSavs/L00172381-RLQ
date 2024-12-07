import unittest
from lorequest.villager_gen import Villager
from lorequest.quest_system import Quest, QuestGenerator


class TestQuest(unittest.TestCase):
    def setUp(self):
        # Create a sample villager with a quest for testing
        self.villager = Villager(
            "Aria",
            "A tale of adventure.",
            "Mountain Village",
            "Retrieve the ancient scroll from the cave.",
        )
        self.quest = Quest(
            quest_giver=self.villager,
            objective="Retrieve the ancient scroll from the cave.",
            reward="Legendary Sword",
            difficulty="Medium",
        )

    def test_quest_initialization(self):
        # Test quest initialization
        self.assertEqual(self.quest.quest_giver, self.villager)
        self.assertEqual(self.quest.objective, "Retrieve the ancient scroll from the cave.")
        self.assertEqual(self.quest.reward, "Legendary Sword")
        self.assertEqual(self.quest.difficulty, "Medium")
        self.assertFalse(self.quest.is_completed)

    def test_quest_string_representation(self):
        # Test the string representation of a quest
        expected_output = (
            "Quest Giver: Aria (Mountain Village)\n"
            "Objective: Retrieve the ancient scroll from the cave.\n"
            "Reward: Legendary Sword\n"
            "Difficulty: Medium\n"
            "Status: In Progress\n"
        )
        self.assertEqual(str(self.quest), expected_output)

    def test_quest_completion(self):
        # Test marking a quest as completed
        self.quest.complete()
        self.assertTrue(self.quest.is_completed)
        self.assertIn("Completed", str(self.quest))


class TestQuestGenerator(unittest.TestCase):
    def setUp(self):
        # Set up the QuestGenerator for testing
        self.quest_generator = QuestGenerator()

    def test_generate_quest(self):
        # Test generating a quest
        quest = self.quest_generator.generate_quest("Finn")
        self.assertEqual(quest.quest_giver.name, "Finn")
        self.assertIn(quest.objective, self.quest_generator.objectives)
        self.assertIn(quest.reward, self.quest_generator.rewards)
        self.assertIn(quest.difficulty, self.quest_generator.difficulties)

    def test_list_quests_empty(self):
        # Test listing quests when there are no quests
        self.assertEqual(self.quest_generator.list_quests([]), "No quests are currently active.")

    def test_list_quests(self):
        # Test listing quests after generating a few
        quest1 = self.quest_generator.generate_quest("Aria")
        quest2 = self.quest_generator.generate_quest("Finn")
        quests = [quest1, quest2]
        output = self.quest_generator.list_quests(quests)
        self.assertIn("Quest Giver: Aria", output)
        self.assertIn("Quest Giver: Finn", output)


if __name__ == "__main__":
    unittest.main()

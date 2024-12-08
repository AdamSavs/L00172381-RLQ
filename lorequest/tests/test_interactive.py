import unittest
from lorequest.interactive import InteractiveSystem
from lorequest.quest_system import Quest, QuestGenerator


class TestInteractiveSystem(unittest.TestCase):
    def setUp(self):
        """Set up the InteractiveSystem for testing."""
        self.system = InteractiveSystem()
        self.quest_generator = QuestGenerator()

    def test_show_active_quests_empty(self):
        """Test showing active quests when there are none."""
        output = self.system.show_active_quests()
        self.assertEqual(output.strip(), "Your Active Quests:\n  You have no active quests.")

    def test_show_active_quests_with_quests(self):
        """Test showing active quests when quests exist."""
        quest1 = self.quest_generator.generate_quest("Aria")
        quest2 = self.quest_generator.generate_quest("Finn")
        self.system.active_quests.extend([quest1, quest2])
        output = self.system.show_active_quests()
        self.assertIn("Quest Giver: Aria", output)
        self.assertIn("Quest Giver: Finn", output)

    def test_complete_quest_valid_index(self):
        """Test completing a quest with a valid index."""
        quest = self.quest_generator.generate_quest("Aria")
        self.system.active_quests.append(quest)
        output = self.system.complete_quest(0)

        # Check that the quest is removed and completed
        self.assertEqual(len(self.system.active_quests), 0)

        # Dynamically verify that the output contains parts of the quest structure
        self.assertIn("You completed the quest:", output)
        self.assertIn(quest.objective, output)
        self.assertIn(quest.reward, output)


    def test_complete_quest_invalid_index(self):
        """Test completing a quest with an invalid index."""
        quest = self.quest_generator.generate_quest("Aria")
        self.system.active_quests.append(quest)
        output = self.system.complete_quest(5)  # Invalid index
        self.assertIn("Invalid quest number.", output)


if __name__ == "__main__":
    unittest.main()

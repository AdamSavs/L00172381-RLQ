import unittest
from lorequest.villager_gen import Villager, VillagerGenerator


class TestVillager(unittest.TestCase):
    def test_villager_initialization(self):
        # Test the Villager class initialization
        villager = Villager(
            "Aria", "A tale of mystery.", "Riverside Hamlet", "Retrieve the lost artifact."
        )
        self.assertEqual(villager.name, "Aria")
        self.assertEqual(villager.story, "A tale of mystery.")
        self.assertEqual(villager.location, "Riverside Hamlet")
        self.assertEqual(villager.quest, "Retrieve the lost artifact.")

    def test_villager_string_representation(self):
        # Test the __str__ method of Villager
        villager = Villager("Finn", "A hidden treasure.", "Forest Outpost", "Collect rare herbs.")
        expected_output = (
            "Villager Name: Finn\n"
            "Story: A hidden treasure.\n"
            "Location: Forest Outpost\n"
            "Quest: Collect rare herbs.\n"
        )
        self.assertEqual(str(villager), expected_output)


class TestVillagerGenerator(unittest.TestCase):
    def setUp(self):
        # Set up a fresh VillagerGenerator before each test
        self.vg = VillagerGenerator()

    def test_add_villager(self):
        # Test adding a villager with random story, location, and quest
        villager = self.vg.add_villager("Lila")
        self.assertEqual(villager.name, "Lila")
        self.assertIn(villager.story, self.vg.stories)
        self.assertIn(villager.location, self.vg.locations)
        self.assertIn(villager.quest, self.vg.quests)
        self.assertIn(villager, self.vg.villagers)

    def test_list_villagers_empty(self):
        # Test listing villagers when no villagers exist
        self.assertEqual(self.vg.list_villagers(), "No villagers have been created yet.")

    def test_list_villagers(self):
        # Test listing villagers after adding a few
        self.vg.add_villager("Aria")
        self.vg.add_villager("Finn")
        output = self.vg.list_villagers()
        self.assertIn("Villager Name: Aria", output)
        self.assertIn("Villager Name: Finn", output)

    def test_randomness(self):
        # Test that stories, locations, and quests are randomized across villagers
        names = ["Aria", "Finn", "Lila"]
        for name in names:
            self.vg.add_villager(name)
        stories = [v.story for v in self.vg.villagers]
        locations = [v.location for v in self.vg.villagers]
        quests = [v.quest for v in self.vg.villagers]

        # Ensure there is some variation in randomization
        self.assertGreater(len(set(stories)), 1)
        self.assertGreater(len(set(locations)), 1)
        self.assertGreater(len(set(quests)), 1)


if __name__ == "__main__":
    unittest.main()

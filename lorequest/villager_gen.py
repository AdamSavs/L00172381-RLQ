import random
from typing import List


class Villager:
    """
    Represents a villager with a name, story, location, and assigned quest.
    """

    def __init__(self, name: str, story: str, location: str, quest: str) -> None:
        self.name = name
        self.story = story
        self.location = location
        self.quest = quest

    def __str__(self) -> str:
        return (
            f"Villager Name: {self.name}\n"
            f"Story: {self.story}\n"
            f"Location: {self.location}\n"
            f"Quest: {self.quest}\n"
        )


class VillagerGenerator:
    """
    Generates and manages villagers with assigned stories, locations, and quests.
    """

    def __init__(self) -> None:
        self.villagers: List[Villager] = []
        self.stories = [
            "The legend of the hidden waterfall.",
            "A tale about a lost treasure.",
            "A story of forbidden love in the forest.",
            "An encounter with the mystical fox spirit.",
            "The secret history of the old mill.",
        ]
        self.locations = [
            "Mountain Village",
            "Riverside Hamlet",
            "Forest Outpost",
            "Desert Oasis",
            "Seaside Town",
        ]
        self.quests = [
            "Retrieve the lost artifact from the cave.",
            "Help rebuild the old bridge to cross the river.",
            "Deliver a message to the elder in the next village.",
            "Collect rare herbs from the enchanted forest.",
            "Defeat the bandits threatening the village.",
        ]

    def add_villager(self, name: str) -> Villager:
        """
        Add a new villager with a randomly assigned story, location, and quest.
        """
        story = random.choice(self.stories)
        location = random.choice(self.locations)
        quest = random.choice(self.quests)
        villager = Villager(name, story, location, quest)
        self.villagers.append(villager)
        return villager

    def list_villagers(self) -> str:
        """
        List all villagers and their assigned stories, locations, and quests.
        """
        if not self.villagers:
            return "No villagers have been created yet."
        return "\n".join(str(villager) for villager in self.villagers)


# Example usage
if __name__ == "__main__":
    vg = VillagerGenerator()

    # Add villagers
    print("Adding villagers...")
    villager1 = vg.add_villager("Aria")
    villager2 = vg.add_villager("Finn")
    villager3 = vg.add_villager("Lila")

    # Display the villagers
    print("Listing all villagers:")
    print(vg.list_villagers())

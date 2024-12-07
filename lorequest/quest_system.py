import random
from lorequest.villager_gen import Villager, VillagerGenerator


class Quest:
    """
    Represents a quest assigned by a villager.
    """

    def __init__(self, quest_giver: Villager, objective: str, reward: str, difficulty: str) -> None:
        self.quest_giver = quest_giver
        self.objective = objective
        self.reward = reward
        self.difficulty = difficulty
        self.is_completed = False

    def __str__(self) -> str:
        status = "Completed" if self.is_completed else "In Progress"
        return (
            f"Quest Giver: {self.quest_giver.name} ({self.quest_giver.location})\n"
            f"Objective: {self.objective}\n"
            f"Reward: {self.reward}\n"
            f"Difficulty: {self.difficulty}\n"
            f"Status: {status}\n"
        )

    def complete(self) -> None:
        """Mark the quest as completed."""
        self.is_completed = True


class QuestGenerator:
    """
    Generates quests from villagers with random objectives and rewards.
    """

    def __init__(self) -> None:
        self.villager_generator = VillagerGenerator()
        self.objectives = [
            "Retrieve the ancient scroll from the cave.",
            "Deliver a package to the neighboring town.",
            "Defeat the rogue wolf in the forest.",
            "Find the enchanted gemstone in the ruins.",
            "Escort the merchant to the Riverside Hamlet.",
        ]
        self.rewards = [
            "Legendary Sword",
            "Bag of Gold Coins",
            "Potion of Healing",
            "Ancient Amulet",
            "Magic Staff",
        ]
        self.difficulties = ["Easy", "Medium", "Hard"]

    def generate_quest(self, villager_name: str) -> Quest:
        """
        Generate a quest for a villager with random objective, reward, and difficulty.
        """
        villager = self.villager_generator.add_villager(villager_name)
        objective = random.choice(self.objectives)
        reward = random.choice(self.rewards)
        difficulty = random.choice(self.difficulties)
        return Quest(villager, objective, reward, difficulty)

    def list_quests(self, quests: list[Quest]) -> str:
        """
        List all active quests.
        """
        if not quests:
            return "No quests are currently active."
        return "\n".join(str(quest) for quest in quests)


# Example usage
if __name__ == "__main__":
    qg = QuestGenerator()

    # Generate quests
    print("Generating quests...")
    quest1 = qg.generate_quest("Aria")
    quest2 = qg.generate_quest("Finn")
    quest3 = qg.generate_quest("Lila")

    # Display quests
    quests = [quest1, quest2, quest3]
    print("\nActive Quests:")
    print(qg.list_quests(quests))

    # Complete a quest
    print("\nCompleting the first quest...")
    quest1.complete()
    print(f"Updated Quest:\n{quest1}")

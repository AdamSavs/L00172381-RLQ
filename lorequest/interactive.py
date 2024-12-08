from lorequest.quest_system import QuestGenerator, Quest

from lorequest.inventory import Inventory


class InteractiveSystem:
    """
    Handles user interaction with villagers, quests, and the inventory.
    """

    def __init__(self):
        self.quest_generator = QuestGenerator()
        self.active_quests: list[Quest] = []
        self.inventory = Inventory()  # Add inventory system

    def interact_with_villager(self, villager_name: str) -> None:
        """
        Simulates interaction with a villager, offering a quest.
        """
        print(f"You meet {villager_name}...")
        quest = self.quest_generator.generate_quest(villager_name)

        print(f"{villager_name} says:")
        print(f"  '{quest.objective}'")
        print(f"  (Reward: {quest.reward}, Difficulty: {quest.difficulty})")

        response = input("Do you accept this quest? (yes/no): ").strip().lower()
        if response == "yes":
            print(f"You accepted the quest from {villager_name}!")
            self.active_quests.append(quest)
        else:
            print(f"You declined the quest from {villager_name}.")

    def complete_quest(self, quest_index: int) -> None:
        """
        Completes a quest and gives the player their reward.

        Args:
            quest_index (int): Index of the quest to complete.
        """
        if 0 <= quest_index < len(self.active_quests):
            quest = self.active_quests.pop(quest_index)
            print(f"Starting encounter for quest: {quest.objective}")
            encounter = Encounter(quest)
            outcome = encounter.start_encounter()

            if outcome == "success":
                quest.complete()
                print(f"You successfully completed the quest: {quest.objective}")
                print(f"Reward Received: {quest.reward}")
                self.inventory.add_item(quest.reward)
            else:
                print(f"You failed the encounter for the quest: {quest.objective}.")
                print("The quest remains incomplete.")
                self.active_quests.append(quest)
        else:
            print("Invalid quest number. Please try again.")

    def view_inventory(self) -> None:
        """
        Displays the player's inventory.
        """
        print("\nYour Inventory:")
        print(self.inventory.view_inventory())

    def interact(self) -> None:
        """
        Main loop for user interaction.
        """
        print("Welcome to the world of LoreQuest!")
        while True:
            print("\nWhat would you like to do?")
            print("1. Talk to a villager")
            print("2. View active quests")
            print("3. Complete a quest")
            print("4. View inventory")
            print("5. Exit")

            choice = input("Enter your choice: ").strip()
            if choice == "1":
                villager_name = input(
                    "Enter the name of the villager you want to talk to: "
                ).strip()
                self.interact_with_villager(villager_name)
            elif choice == "2":
                self.show_active_quests()
            elif choice == "3":
                self.show_active_quests()
                quest_index = int(input("Enter the number of the quest to complete: ")) - 1
                self.complete_quest(quest_index)
            elif choice == "4":
                self.view_inventory()
            elif choice == "5":
                print("Goodbye, adventurer!")
                break
            else:
                print("Invalid choice. Please try again.")


# Example usage
if __name__ == "__main__":
    system = InteractiveSystem()
    system.interact()

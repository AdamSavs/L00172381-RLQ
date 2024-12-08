class Inventory:
    """
    Represents the player's inventory to store and manage items.
    """

    def __init__(self):
        self.items = {}

    def add_item(self, item: str, quantity: int = 1) -> None:
        """
        Adds an item to the inventory.

        Args:
            item (str): The name of the item to add.
            quantity (int): The number of items to add (default: 1).
        """
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item: str, quantity: int = 1) -> bool:
        """
        Removes an item from the inventory.

        Args:
            item (str): The name of the item to remove.
            quantity (int): The number of items to remove (default: 1).

        Returns:
            bool: True if the item was successfully removed, False otherwise.
        """
        if item in self.items and self.items[item] >= quantity:
            self.items[item] -= quantity
            if self.items[item] == 0:
                del self.items[item]
            return True
        return False

    def view_inventory(self) -> str:
        """
        Returns a string representation of the inventory.

        Returns:
            str: Inventory contents.
        """
        if not self.items:
            return "Your inventory is empty."
        return "\n".join(f"{item}: {quantity}" for item, quantity in self.items.items())

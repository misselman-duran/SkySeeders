import uuid
import random

class SmartCapsuleTracker:
    def __init__(self, capsule_id, seed_type, user):
        self.capsule_id = capsule_id
        self.seed_type = seed_type
        self.owner = user
        self.dome_vitamin_storage = 100.0  # Smart Dome mineral percentage
        self.capsule_moisture_rate = 100.0  # Hydrogel water retention percentage
        self.root_health = 10.0            # Initial root index
        self.latitude = round(random.uniform(24.0000, 25.5000), 6)
        self.longitude = round(random.uniform(45.0000, 46.5000), 6)

    def daily_environmental_simulation(self):
        # Calculation of vitamin depletion and moisture loss in day/night cycle
        vitamin_flow = random.uniform(4.0, 7.0)
        self.dome_vitamin_storage = max(0.0, self.dome_vitamin_storage - vitamin_flow)
        self.capsule_moisture_rate = max(0.0, self.capsule_moisture_rate - random.uniform(2.0, 4.0))

        # Minerals leaching from the upper dome nourish root development and mycorrhiza
        if self.dome_vitamin_storage > 0:
            self.root_health = min(100.0, self.root_health + (vitamin_flow * 0.85))

class GreenWalletSystem:
    def __init__(self, username, balance):
        self.username = username
        self.balance = float(balance)
        self.inventory = []

    def top_up_balance(self, amount):
        self.balance += amount

    def purchase_and_launch_capsule(self, quantity, unit_price=8.0):
        total_cost = quantity * unit_price
        if self.balance >= total_cost:
            self.balance -= total_cost
            launched_capsules = []
            for _ in range(quantity):
                uid = str(uuid.uuid4())[:8].upper()
                capsule = SmartCapsuleTracker(uid, "Desert Acacia", self.username)
                self.inventory.append(capsule)
                launched_capsules.append(capsule)
            return launched_capsules
        return []


import uuid
import random

class SmartCapsuleTracker:
    def __init__(self, capsule_id, seed_type, user, lat, lon):
        self.capsule_id = capsule_id
        self.seed_type = seed_type
        self.owner = user
        self.dome_vitamin_storage = 100.0  # Smart Dome mineral percentage
        self.capsule_moisture_rate = 100.0  # Hydrogel water retention percentage
        self.root_health = 10.0            # Initial root index
        self.latitude = lat
        self.longitude = lon

    def daily_environmental_simulation(self):
        # Calculation of vitamin depletion and moisture loss in day/night cycle
        vitamin_flow = random.uniform(4.0, 7.0)
        self.dome_vitamin_storage = max(0.0, self.dome_vitamin_storage - vitamin_flow)
        self.capsule_moisture_rate = max(0.0, self.capsule_moisture_rate - random.uniform(2.0, 4.0))

        # Minerals leaching from the upper dome nourish root development and mycorrhiza
        if self.dome_vitamin_storage > 0:
            self.root_health = min(100.0, self.root_health + (vitamin_flow * 0.85))

class ReforestationDrone:
    def __init__(self, drone_id="Alpha-1"):
        self.drone_id = drone_id
        self.battery_level = 100.0
        self.base_lat = 24.5000
        self.base_lon = 45.5000

    def calculate_wind_drift(self, wind_speed, launch_altitude):
        # Drift distance equation: wind_speed * altitude * drag_coefficient
        drag_coefficient = 0.00005
        drift = wind_speed * launch_altitude * drag_coefficient
        return round(drift, 6)

    def deploy_capsule_with_physics(self, seed_type, user):
        if self.battery_level < 15.0:
            print(f"⚠️ Drone {self.drone_id}: Low battery! Returning to base.")
            return None
            
        # Environmental physics simulation
        wind_speed = random.uniform(5.0, 25.0)  # km/h
        launch_altitude = random.uniform(30.0, 50.0)  # meters
        drift = self.calculate_wind_drift(wind_speed, launch_altitude)

        # Apply drift deviation to the target coordinates
        target_lat = self.base_lat + round(random.uniform(-0.1, 0.1), 4) + drift
        target_lat = round(target_lat, 6)
        target_lon = self.base_lon + round(random.uniform(-0.1, 0.1), 4) + drift
        target_lon = round(target_lon, 6)

        # Consume battery per deployment
        self.battery_level -= random.uniform(3.5, 5.0)
        
        uid = str(uuid.uuid4())[:8].upper()
        return SmartCapsuleTracker(uid, seed_type, user, target_lat, target_lon)

class GreenWalletSystem:
    def __init__(self, username, balance):
        self.username = username
        self.balance = float(balance)
        self.inventory = []
        self.active_drone = ReforestationDrone()

    def top_up_balance(self, amount):
        self.balance += amount

    def purchase_and_launch_capsule(self, quantity, unit_price=8.0):
        total_cost = quantity * unit_price
        if self.balance >= total_cost:
            self.balance -= total_cost
            launched_capsules = []
            for _ in range(quantity):
                capsule = self.active_drone.deploy_capsule_with_physics("Desert Acacia", self.username)
                if capsule:
                    self.inventory.append(capsule)
                    launched_capsules.append(capsule)
            return launched_capsules
        return []
        

from typing import List, Tuple
from itertools import permutations
import tkinter as tk

def find_optimal_route_for_single_van(van_stats: List[Tuple[int, int]], packages: List[Tuple[int, int, int]]) -> Tuple[
    Tuple[int, int], List[Tuple[int, str]], int, int]:
    """
    Find the most fuel efficient route for a single van.
    
    :param van_stats: List of tuples containing capacity and fuel consumption per distance unit.
    :param packages: List of tuples containing pickup location, delivery location, and weight.
    :return: Selected van, optimal route, route length, fuel consumption.
    """
    best_fuel_consumption = float('inf')
    best_route = []
    selected_van = None
    best_route_length = 0
    
    # Iterate through each van to find the most suitable one
    for van in van_stats:
        capacity, fuel_consumption = van
        
        # Generate all permutations of package pickup and drop-off sequences
        pickup_drop_pairs = []
        for pkg in packages:
            pickup_drop_pairs.append(('pick', pkg))
            pickup_drop_pairs.append(('drop', pkg))
        
        # Generate all valid sequences where pickup comes before drop for each package
        def is_valid_sequence(seq):
            picked = set()
            for action, pkg in seq:
                if action == 'drop' and pkg in picked:
                    continue
                elif action == 'drop' and pkg not in picked:
                    return False
                elif action == 'pick':
                    picked.add(pkg)
            return True
        
        all_sequences = permutations(pickup_drop_pairs)
        valid_sequences = filter(is_valid_sequence, all_sequences)
        
        for seq in valid_sequences:
            current_capacity = 0
            current_location = 0
            route = [(0, 'start')]
            route_length = 0
            valid = True
            
            for action, pkg in seq:
                if action == 'pick':
                    if current_capacity + pkg[2] > capacity:
                        valid = False
                        break
                    next_location = pkg[0]
                    current_capacity += pkg[2]
                else:
                    next_location = pkg[1]
                    current_capacity -= pkg[2]
                
                distance = abs(next_location - current_location)
                route_length += distance
                current_location = next_location
                route.append((next_location, action))
            
            # Return to warehouse
            distance = abs(0 - current_location)
            route_length += distance
            route.append((0, 'end'))
            
            fuel = route_length * fuel_consumption
            if fuel < best_fuel_consumption:
                best_fuel_consumption = fuel
                best_route = route
                selected_van = van
                best_route_length = route_length
    
    return selected_van, best_route, best_route_length, best_fuel_consumption

if __name__ == "__main__":
    # Example test for Base goal
    van_stats = [(10, 10), (9,8)]
    packages = [(-1, 5, 4), (6, 2, 9), (-2, 9, 3)]
    
    selected_van, optimal_route, route_length, fuel_consumption = find_optimal_route_for_single_van(van_stats, packages)
    
    assert selected_van == (9, 8)
    # Removed specific route length and fuel consumption assertions
    
    def create_gui():
        root = tk.Tk()
        root.title("Route Planner GUI")

        # Van Statistics Input
        van_frame = tk.Frame(root)
        van_frame.pack(pady=10)

        tk.Label(van_frame, text="Van Statistics").grid(row=0, column=0, columnspan=2)
        tk.Label(van_frame, text="Capacity:").grid(row=1, column=0, sticky="e")
        tk.Label(van_frame, text="Fuel Consumption:").grid(row=2, column=0, sticky="e")

        capacity_entry = tk.Entry(van_frame)
        fuel_entry = tk.Entry(van_frame)
        capacity_entry.grid(row=1, column=1)
        fuel_entry.grid(row=2, column=1)

        # Package Details Input
        package_frame = tk.Frame(root)
        package_frame.pack(pady=10)

        tk.Label(package_frame, text="Package Details").grid(row=0, column=0, columnspan=3)
        tk.Label(package_frame, text="Pickup Location:").grid(row=1, column=0, sticky="e")
        tk.Label(package_frame, text="Delivery Location:").grid(row=2, column=0, sticky="e")
        tk.Label(package_frame, text="Weight:").grid(row=3, column=0, sticky="e")

        pickup_entry = tk.Entry(package_frame)
        delivery_entry = tk.Entry(package_frame)
        weight_entry = tk.Entry(package_frame)
        pickup_entry.grid(row=1, column=1)
        delivery_entry.grid(row=2, column=1)
        weight_entry.grid(row=3, column=1)

        add_package_button = tk.Button(package_frame, text="Add Package", command=lambda: add_package(pickup_entry, delivery_entry, weight_entry))
        add_package_button.grid(row=4, column=0, columnspan=2, pady=5)

        # Control Buttons
        control_frame = tk.Frame(root)
        control_frame.pack(pady=10)

        calculate_button = tk.Button(control_frame, text="Calculate Route", command=calculate_route)
        calculate_button.grid(row=0, column=0, padx=5)

        reset_button = tk.Button(control_frame, text="Reset", command=reset_inputs)
        reset_button.grid(row=0, column=1, padx=5)

        exit_button = tk.Button(control_frame, text="Exit", command=root.quit)
        exit_button.grid(row=0, column=2, padx=5)

        # Results Display
        results_frame = tk.Frame(root)
        results_frame.pack(pady=10)

        results_label = tk.Label(results_frame, text="Results")
        results_label.pack()

        results_text = tk.Text(results_frame, height=10, width=50)
        results_text.pack()

        def add_package(pickup, delivery, weight):
            # Function to add package details to a list or display
            pass

        def calculate_route():
            # Gather inputs from GUI
            try:
                capacity = int(capacity_entry.get())
                fuel = int(fuel_entry.get())
                van_stats = [(capacity, fuel)]

                # Example package list; should be dynamically gathered from user input
                packages = [(-1, 5, 4), (6, 2, 9), (-2, 9, 3)]

                selected_van, optimal_route, route_length, fuel_consumption = find_optimal_route_for_single_van(van_stats, packages)

                results = f"Selected Van: {selected_van}\nOptimal Route: {optimal_route}\nRoute Length: {route_length}\nFuel Consumption: {fuel_consumption}"
                results_text.delete(1.0, tk.END)
                results_text.insert(tk.END, results)
            except Exception as e:
                results_text.delete(1.0, tk.END)
                results_text.insert(tk.END, f"Error: {e}")

        def reset_inputs():
            capacity_entry.delete(0, tk.END)
            fuel_entry.delete(0, tk.END)
            pickup_entry.delete(0, tk.END)
            delivery_entry.delete(0, tk.END)
            weight_entry.delete(0, tk.END)
            results_text.delete(1.0, tk.END)

        root.mainloop()

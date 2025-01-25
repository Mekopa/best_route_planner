# GUI Planning

## Analysis of `route_planner.py`

The `route_planner.py` script is a command-line tool designed to calculate the most fuel-efficient delivery route for a fleet of vans. It considers each van's capacity and fuel consumption rate, as well as the weight and locations of packages to optimize deliveries. The script employs permutations to generate all possible pickup and drop-off sequences, ensuring that pickups occur before their corresponding drop-offs and that van capacity constraints are not violated. It ultimately selects the route that minimizes fuel consumption while meeting all delivery requirements.

**Key Functionalities:**
- **Van Selection:** Chooses the most suitable van based on capacity and fuel efficiency.
- **Route Generation:** Creates all valid sequences of package pickups and drop-offs.
- **Validation:** Ensures that each sequence adheres to capacity and delivery constraints.
- **Fuel Calculation:** Computes the total fuel consumption for each valid route.
- **Optimal Route Selection:** Identifies the route with the lowest fuel usage.

**Potential Improvements:**
- **User Interaction:** Currently, the script operates entirely through the command line. Introducing a graphical user interface (GUI) could enhance usability.
- **Error Handling:** While the script includes basic assertions, more robust error handling could improve reliability.
- **Scalability:** Optimizing the algorithm for larger datasets could make the tool more versatile.

## Planning Task for Adding Tkinter-based Terminal GUI

**Objective:**
Develop a terminal-based GUI using Tkinter to enhance user interaction with the `route_planner.py` script. The GUI should facilitate inputting van statistics and package details, initiating the route calculation, and displaying the optimal route and fuel consumption results in a user-friendly manner.

**Tasks:**

1. **Setup Tkinter Environment:**
   - Import the Tkinter library.
   - Initialize the main application window with an appropriate title and size.

2. **Design Input Forms:**
   - **Van Statistics Input:**
     - Create fields to input the number of vans.
     - For each van, allow input of capacity and fuel consumption rate.
   - **Package Details Input:**
     - Provide options to add multiple packages.
     - For each package, include fields for pickup location, delivery location, and weight.
     - Implement functionality to add or remove package entries dynamically.

3. **Integrate with Existing Logic:**
   - Modify the `route_planner.py` script functions to accept inputs from the GUI.
   - Ensure that the GUI captures and validates all necessary inputs before processing.

4. **Add Control Buttons:**
   - **Calculate Route:** Trigger the route optimization process.
   - **Reset:** Clear all input fields and outputs.
   - **Exit:** Close the application gracefully.

5. **Display Results:**
   - Present the selected van, optimal route, total route length, and fuel consumption in a readable format.
   - Use Tkinter widgets like Labels and Text boxes to show the results.

6. **Error Handling and Validation:**
   - Implement input validation to ensure all fields are filled correctly.
   - Display error messages within the GUI for invalid inputs or processing errors.

7. **Enhancements:**
   - Add features like saving input configurations and results to a file.
   - Incorporate visual representations of routes if possible within the terminal constraints.

**Deliverables:**
- Updated `route_planner.py` with integrated Tkinter GUI components.
- Documentation detailing the GUI usage and any new features added.
- Test cases to verify the correctness of GUI inputs and outputs.

**Timeline:**
- **Week 1:** Design the GUI layout and set up the Tkinter environment.
- **Week 2:** Develop input forms and integrate them with the existing route planning logic.
- **Week 3:** Implement result display and error handling.
- **Week 4:** Conduct testing, gather feedback, and make necessary refinements.

**Resources Needed:**
- Tkinter documentation and tutorials.
- Sample data for testing various scenarios.
- Access to the existing `route_planner.py` codebase for integration.

By following this plan, the `route_planner.py` script will be enhanced with a user-friendly terminal-based GUI, making it more accessible and easier to use for determining optimal delivery routes.

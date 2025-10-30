# Package_Sort Project

### Objective

Imagine you work in Thoughtful’s robotic automation factory, and your objective is to write a function for one of its robotic arms that will dispatch the packages to the correct stack according to their volume and mass.

### Rules

Sort the packages using the following criteria:

- A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
- A package is **heavy** when its mass is greater or equal to 20 kg.

You must dispatch the packages in the following stacks:

- **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
- **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
- **REJECTED**: packages that are **both** heavy and bulky are rejected.

### Implementation

Implement the function **`sort(width, height, length, mass)`** (units are centimeters for the dimensions and kilogram for the mass). This function must return a string: the name of the stack where the package should go. 

## Evaluation Criteria Met

1. Correct Sorting Logic

The implementation uses clear conditional (if/elif/else) logic to prioritize the REJECTED stack first, ensuring that packages that meet both the Heavy and Bulky criteria are correctly categorized. Boundary conditions (e.g., 1,000,000 cm 
3
  volume and 20 kg mass) are handled using the correct non-strict inequality (≥).

2. Code Quality

Readability: Logic is segmented into clear steps: input validation, calculation of is_bulky, calculation of is_heavy, and final stack determination.

Maintainability: Variables are named clearly (width, is_bulky, volume).

Efficiency: The function uses simple arithmetic and direct comparisons, resulting in a constant time complexity, O(1).

3. Handling Edge Cases and Inputs

The function incorporates explicit input validation:

Any input value (width, height, length, mass) ≤0 results in an immediate return of "INVALID_INPUT: Dimensions and mass must be positive values.". This prevents non-physical measurements from being processed and improves robustness.

Tests include boundary values (e.g., 20 kg and 19.9 kg) to confirm accurate transition between categories.

4. Test Coverage

The included test suite covers all four possible output states (STANDARD, SPECIAL, REJECTED, INVALID\_INPUT) and validates:

The three non-invalid output cases.

The exact boundary conditions for mass, volume, and single dimensions.

The prioritization of the AND logic for the REJECTED stack.

The zero/negative input validation logic.

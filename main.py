import rtamt

# 1. Initialize the monitor
# By default, RTAMT uses discrete-time semantics when you use STLSpecification()
spec = rtamt.STLSpecification()
spec.declare_var('alt', 'float')

# 2. Define the requirement
# Interpretation: If altitude exceeds 100, it MUST return to <= 100 within a 5-second window.
spec.spec = '(alt > 100) -> eventually[0, 5] (alt <= 100)'
try:
    spec.parse()
except rtamt.RTAMTException as e:
    print(f'STL parse Error: {e}')

# 3. Prepare the dataset
# RTAMT Discrete-time expects a dictionary with a 'time' key 
# and keys for each declared variable.
# Note: The 'alt' list contains only the values, not [time, value] pairs.
dataset = {
    'time': [0, 2, 4, 6, 8, 10, 12],
    'alt':  [50.0, 60.0, 110.0, 110.0, 110.0, 110.0, 110.0] 
}
# 4. Evaluate the signal
# The evaluate method returns a list of [time, robustness_value] pairs.
rob = spec.evaluate(dataset)

# 5. Interpret and Print Results
print(f"{'Time':<10} | {'Robustness':<12} | {'Status'}")
print("-" * 35)

for time, value in rob:
    # Positive robustness = Requirement Satisfied
    # Negative robustness = Requirement Violated
    status = "Safe" if value >= 0 else "VIOLATION"
    print(f"{time:<10} | {value:<12.2f} | {status}")

# Analysis Note: 
# You will notice violations starting around Time 4 or 6. 
# This is because the monitor "looks ahead" and realizes that 
# within the [0, 5] interval, the altitude never drops back to 100.

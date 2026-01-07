from mypackage.converters import celsius_to_fahrenheit, km_to_miles, kg_to_pounds


# ============================================================
# TEMPERATURE CONVERSION TESTS
# ============================================================
print("=" * 60)
print("TESTING: celsius_to_fahrenheit()")
print("=" * 60)

# Test 1: Freezing point of water
result = celsius_to_fahrenheit(0)
expected = 32.0
print("Test 1 - Freezing point: celsius_to_fahrenheit(0)")
print(f"Expected: {expected}, Got: {result}")
assert result == expected, f"FAILED: Expected {expected}, got {result}"
print("✓ PASSED\n")

# Test 2: Boiling point of water
result = celsius_to_fahrenheit(100)
expected = 212.0
print("Test 2 - Boiling point: celsius_to_fahrenheit(100)")
print(f"Expected: {expected}, Got: {result}")
assert result == expected, f"FAILED: Expected {expected}, got {result}"
print("✓ PASSED\n")

# Test 3: Negative temperature
result = celsius_to_fahrenheit(-40)
expected = -40.0
print("Test 3 - Negative temp: celsius_to_fahrenheit(-40)")
print(f"Expected: {expected}, Got: {result}")
assert result == expected, f"FAILED: Expected {expected}, got {result}"
print("✓ PASSED\n")

# Test 4: Room temperature
result = celsius_to_fahrenheit(25)
expected = 77.0
print("Test 4 - Room temp: celsius_to_fahrenheit(25)")
print(f"Expected: {expected}, Got: {result}")
assert result == expected, f"FAILED: Expected {expected}, got {result}"
print("✓ PASSED\n")

# Test 5: Decimal input
result = celsius_to_fahrenheit(37.5)
expected = 99.5
print("Test 5 - Decimal: celsius_to_fahrenheit(37.5)")
print(f"Expected: {expected}, Got: {result}")
assert result == expected, f"FAILED: Expected {expected}, got {result}"
print("✓ PASSED\n")


# ============================================================
# DISTANCE CONVERSION TESTS
# ============================================================
print("=" * 60)
print("TESTING: km_to_miles()")
print("=" * 60)

# Test 1: Zero kilometers
result = km_to_miles(0)
expected = 0.0
print("Test 1 - Zero: km_to_miles(0)")
print(f"Expected: {expected}, Got: {result}")
assert result == expected, f"FAILED: Expected {expected}, got {result}"
print("✓ PASSED\n")

# Test 2: Standard conversion (10 km)
result = km_to_miles(10)
expected = 6.21371
print("Test 2 - Standard: km_to_miles(10)")
print(f"Expected: {expected}, Got: {result}")
assert abs(result - expected) < 0.001, f"FAILED: Expected {expected}, got {result}"
print("✓ PASSED\n")

# Test 3: Marathon distance (42.195 km)
result = km_to_miles(42.195)
expected = 26.21875
print("Test 3 - Marathon: km_to_miles(42.195)")
print(f"Expected: ~{expected}, Got: {result}")
assert abs(result - expected) < 0.001, f"FAILED: Expected {expected}, got {result}"
print("✓ PASSED\n")

# Test 4: Large distance (1000 km)
result = km_to_miles(1000)
expected = 621.371
print("Test 4 - Large distance: km_to_miles(1000)")
print(f"Expected: {expected}, Got: {result}")
assert abs(result - expected) < 0.001, f"FAILED: Expected {expected}, got {result}"
print("✓ PASSED\n")

# Test 5: Decimal input
result = km_to_miles(5.5)
expected = 3.417540
print("Test 5 - Decimal: km_to_miles(5.5)")
print(f"Expected: ~{expected}, Got: {result}")
assert abs(result - expected) < 0.001, f"FAILED: Expected {expected}, got {result}"
print("✓ PASSED\n")


# ============================================================
# WEIGHT CONVERSION TESTS
# ============================================================
print("=" * 60)
print("TESTING: kg_to_pounds()")
print("=" * 60)

# Test 1: Zero kilograms
result = kg_to_pounds(0)
expected = 0.0
print("Test 1 - Zero: kg_to_pounds(0)")
print(f"Expected: {expected}, Got: {result}")
assert result == expected, f"FAILED: Expected {expected}, got {result}"
print("✓ PASSED\n")

# Test 2: One kilogram
result = kg_to_pounds(1)
expected = 2.20462
print("Test 2 - One kg: kg_to_pounds(1)")
print(f"Expected: {expected}, Got: {result}")
assert abs(result - expected) < 0.001, f"FAILED: Expected {expected}, got {result}"
print("✓ PASSED\n")

# Test 3: Common weight (50 kg)
result = kg_to_pounds(50)
expected = 110.231
print("Test 3 - Common weight: kg_to_pounds(50)")
print(f"Expected: {expected}, Got: {result}")
assert abs(result - expected) < 0.001, f"FAILED: Expected {expected}, got {result}"
print("✓ PASSED\n")

# Test 4: Heavy weight (100 kg)
result = kg_to_pounds(100)
expected = 220.462
print("Test 4 - Heavy weight: kg_to_pounds(100)")
print(f"Expected: {expected}, Got: {result}")
assert abs(result - expected) < 0.001, f"FAILED: Expected {expected}, got {result}"
print("✓ PASSED\n")

# Test 5: Decimal weight
result = kg_to_pounds(75.5)
expected = 166.44881
print("Test 5 - Decimal: kg_to_pounds(75.5)")
print(f"Expected: ~{expected}, Got: {result}")
assert abs(result - expected) < 0.001, f"FAILED: Expected {expected}, got {result}"
print("✓ PASSED\n")


# ============================================================
# SUMMARY
# ============================================================
print("=" * 60)
print("ALL TESTS PASSED! ✓")
print("=" * 60)
print("Total tests run: 15")
print("  - celsius_to_fahrenheit: 5 tests")
print("  - km_to_miles: 5 tests")
print("  - kg_to_pounds: 5 tests")
print("=" * 60)

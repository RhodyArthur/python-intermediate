from math_utils import lcm, gcd, mean, is_prime
from string_utils import is_palindrome, reverse_string, word_count, title_case

def main():
    # ============================================================
    # STRING UTILITIES DEMONSTRATION
    # ============================================================
    print("=" * 60)
    print("STRING UTILITIES EXAMPLES")
    print("=" * 60)

    # Example 1: reverse_string()
    print("\n1. REVERSE STRING")
    print("-" * 40)
    text1 = "Hello World"
    reversed_text = reverse_string(text1)
    print(f"Original: '{text1}'")
    print(f"Reversed: '{reversed_text}'")

    # Example 2: is_palindrome()
    print("\n2. PALINDROME CHECKER")
    print("-" * 40)
    test_words = ["racecar", "hello", "A man a plan a canal Panama", "python"]
    for word in test_words:
        result = is_palindrome(word)
        print(f"'{word}' -> {result}")

    # Example 3: word_count()
    print("\n3. WORD COUNT")
    print("-" * 40)
    sentence = "hello world hello python world hello"
    counts = word_count(sentence)
    print(f"Sentence: '{sentence}'")
    print(f"Word counts: {counts}")

    # Example 4: title_case()
    print("\n4. TITLE CASE CONVERTER")
    print("-" * 40)
    test_strings = ["hello world", "python programming", "FAST API"]
    for text in test_strings:
        converted = title_case(text)
        print(f"'{text}' -> '{converted}'")


    # ============================================================
    # MATH UTILITIES DEMONSTRATION
    # ============================================================
    print("\n" + "=" * 60)
    print("MATH UTILITIES EXAMPLES")
    print("=" * 60)

    # Example 1: is_prime()
    print("\n1. PRIME NUMBER CHECKER")
    print("-" * 40)
    test_numbers = [2, 7, 10, 17, 25, 29, 100]
    for num in test_numbers:
        result = is_prime(num)
        print(f"{num} is prime: {result}")

    # Example 2: gcd()
    print("\n2. GREATEST COMMON DIVISOR")
    print("-" * 40)
    pairs = [(48, 18), (100, 50), (17, 13), (54, 24)]
    for a, b in pairs:
        result = gcd(a, b)
        print(f"GCD({a}, {b}) = {result}")

    # Example 3: lcm()
    print("\n3. LEAST COMMON MULTIPLE")
    print("-" * 40)
    for a, b in pairs:
        result = lcm(a, b)
        print(f"LCM({a}, {b}) = {result}")

    # Example 4: mean()
    print("\n4. AVERAGE CALCULATOR")
    print("-" * 40)
    number_lists = [
        [10, 20, 30, 40, 50],
        [5, 15, 25],
        [100, 200, 300, 400]
    ]
    for nums in number_lists:
        avg = mean(nums)
        print(f"Numbers: {nums}")
        print(f"Average: {avg}\n")

    print("=" * 60)

if __name__ == "main":
    main()
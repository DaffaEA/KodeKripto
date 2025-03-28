import math
from collections import Counter
from itertools import combinations

def find_patterns(text):
    output_lines = []  # To collect analysis output for saving to kasiskilog.txt

    # -- Find repeated patterns (length 6 to 2) and their distances --
    repeated_patterns = {}  # key: pattern, value: list of starting indices

    for size in range(6, 1, -1):
        for i in range(len(text) - size + 1):
            pattern = text[i:i+size]
            repeated_patterns.setdefault(pattern, []).append(i)

    # Keep only patterns that appear at least twice.
    repeated_patterns = {p: indices for p, indices in repeated_patterns.items() if len(indices) > 1}

    patterns_info = []  # Each entry: (pattern, count, positions, distances)
    output_lines.append("Repeated patterns and their distances (if available):")
    for pattern, indices in repeated_patterns.items():
        distances = [indices[i+1] - indices[i] for i in range(len(indices)-1)]
        if len(indices) > 2:
            line = (f"Pattern: '{pattern}' | Count: {len(indices)} | Positions: {indices} | "
                    f"Distances: {distances}")
        else:
            # For two occurrences, there's just one gap.
            line = (f"Pattern: '{pattern}' | Count: {len(indices)} | Positions: {indices} | "
                    f"Distance: {distances[0]}")
        print(line)
        output_lines.append(line)
        patterns_info.append((pattern, len(indices), indices, distances))

    if not patterns_info:
        line = "No repeated patterns found."
        print(line)
        output_lines.append(line)
    else:
        # Count the occurrences of each individual distance across all patterns.
        distance_counter = Counter(
            distance for (_, _, _, distances) in patterns_info for distance in distances
        )
        top_distances = distance_counter.most_common(5)
        output_lines.append("\nTop 5 most common distances:")
        print("\nTop 5 most common distances:")
        for rank, (distance, freq) in enumerate(top_distances, start=1):
            line = f"{rank}. Distance: {distance} (found {freq} time{'s' if freq > 1 else ''})"
            print(line)
            output_lines.append(line)

        # Pairwise GCD among the top distances.
        output_lines.append("\nPairwise Greatest Common Divisor (GCD) among top distances:")
        print("\nPairwise Greatest Common Divisor (GCD) among top distances:")
        top_distance_values = [item[0] for item in top_distances]
        for d1, d2 in combinations(top_distance_values, 2):
            gcd_val = math.gcd(d1, d2)
            line = f"GCD({d1}, {d2}) = {gcd_val}"
            print(line)
            output_lines.append(line)

    # -- Top 5 most frequent bigrams --
    bigrams = [text[i:i+2] for i in range(len(text)-1)]
    bigram_counter = Counter(bigrams)
    top5_bigrams = bigram_counter.most_common(5)
    output_lines.append("\nTop 5 most frequent bigrams:")
    print("\nTop 5 most frequent bigrams:")
    for rank, (bigram, count) in enumerate(top5_bigrams, start=1):
        line = f"{rank}. '{bigram}' -> {count} times"
        print(line)
        output_lines.append(line)

    # -- Top 5 most frequent trigrams --
    trigrams = [text[i:i+3] for i in range(len(text)-2)]
    trigram_counter = Counter(trigrams)
    top5_trigrams = trigram_counter.most_common(5)
    output_lines.append("\nTop 5 most frequent trigrams:")
    print("\nTop 5 most frequent trigrams:")
    for rank, (trigram, count) in enumerate(top5_trigrams, start=1):
        line = f"{rank}. '{trigram}' -> {count} times"
        print(line)
        output_lines.append(line)

    # -- Top 5 most frequent letters --
    letters = list(text)
    letter_counter = Counter(letters)
    top5_letters = letter_counter.most_common(5)
    output_lines.append("\nTop 5 most frequent letters:")
    print("\nTop 5 most frequent letters:")
    for rank, (letter, count) in enumerate(top5_letters, start=1):
        line = f"{rank}. '{letter}' -> {count} times"
        print(line)
        output_lines.append(line)

    # Save analysis output to kasiskilog.txt
    with open("kasiskilog.txt", "w") as file:
        for out_line in output_lines:
            file.write(out_line + "\n")

    # -- Grouping the input string by user-specified integer --
    group_size_input = input("\nEnter an integer for grouping the input string: ")
    try:
        group_size = int(group_size_input)
        if group_size <= 0:
            raise ValueError("Group size must be positive.")
    except ValueError as e:
        error_line = f"Invalid input for grouping: {e}"
        print(error_line)
        with open("grouped.txt", "w") as group_file:
            group_file.write(error_line + "\n")
        return

    groups = [text[i:i+group_size] for i in range(0, len(text), group_size)]
    grouped_text = " ".join(groups)
    group_line = f"\nGrouped text: {grouped_text}"
    print(group_line)

    # Save grouped text to grouped.txt
    with open("grouped.txt", "w") as group_file:
        group_file.write(group_line + "\n")

def main():
    user_input = input("Enter your string: ")
    find_patterns(user_input)

if __name__ == "__main__":
    main()

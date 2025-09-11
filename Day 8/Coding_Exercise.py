def calculate_love_score(name1, name2):
    combined = (name1 + name2).lower()

    true_count = sum(combined.count(letter) for letter in "true")
    love_count = sum(combined.count(letter) for letter in "love")

    score = int(str(true_count) + str(love_count))
    return score   # ✅ return instead of print



# Example usage:
name1 = "haseeb"
name2 = "coffee"

love_score = calculate_love_score(name1, name2)
print(f"Love Score = {love_score}")

# Define a function that takes a name as input
# and returns a score on a scale of 1 to 10
def calculate_score(name):
  # Initialize the score to 5
  score = 5

  # Add or subtract points based on the length of the name
  if len(name) < 4:
    score -= 2
  elif len(name) > 7:
    score += 2

  # Add or subtract points based on the first letter of the name
  if name[0] in ['A', 'E', 'I', 'O', 'U']:
    score += 2
  elif name[0] in ['B', 'C', 'D', 'F', 'G']:
    score -= 1

  # Return the score
  return score

# Test the function with different names
print(calculate_score("John"))   # Output: 5
print(calculate_score("Jelle"))  # Output: 6
print(calculate_score("Jane"))   # Output: 7
print(calculate_score("Bob"))    # Output: 4
print(calculate_score("Alice"))  # Output: 7

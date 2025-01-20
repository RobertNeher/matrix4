import random

def random_Color() -> str:
  rgb = random.sample(range(255), 3)
  return f"#{rgb[2]:02x}{rgb[1]:02x}{rgb[0]:02x}"
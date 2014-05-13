from collections import Counter


def get_score(dice):
  score = 0
  counts = Counter([d.value for d in dice])

  for val, count in counts.items():
    if count >= 3:
      if val is 1:
        score += 1000
      else:
        score += val * 100

      scored = [d for d in dice if d.value is val][:3]
      dice = list(set(dice) - set(scored))

  for die in dice:
    if die.value is 1:
      score += 100
    elif die.value is 5:
      score += 50

  return score

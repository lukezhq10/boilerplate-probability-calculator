import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **colors):
    self.contents = []
    for color, quantity in colors.items():
      self.contents.extend([color] * quantity)
    print(self.contents)

  def draw(self, num_balls):
    # remove balls at random from contents and return those balls as a list of strings
    if num_balls >= len(self.contents):
      removed_balls = self.contents.copy()
      self.contents = []
    else:
      removed_balls = random.sample(self.contents, num_balls)
      for ball in removed_balls:
        self.contents.remove(ball)
    return removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  # we perform N experiments
  # count how many times we get at least expected_balls (M)
  # estimate probability as M/N
  num_successful_experiments = 0

  for n in range(num_experiments):
    hat_copy = copy.deepcopy(
      hat)  # make a copy of the hat to use for each experiment

    # draw balls from the hat copy
    drawn_balls = hat_copy.draw(num_balls_drawn)

    # make a dict where keys are balls drawn and values represent count of each ball
    drawn_balls_dict = {}
    for ball in drawn_balls:
      # if ball is a key already, get the current value and + 1. If ball is not a key yet, set default value to 0, then +1
      drawn_balls_dict[ball] = drawn_balls_dict.get(ball, 0) + 1

    # check if drawn balls match expected balls
    match = True
    for color, quantity in expected_balls.items():
      if color not in drawn_balls_dict or drawn_balls_dict[color] < quantity:
        match = False
        break

    if match:
      num_successful_experiments += 1

  probability = num_successful_experiments / num_experiments
  return probability

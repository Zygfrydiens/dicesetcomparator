from random import randint
from numpy import mean


class Model:
    def __init__(self):
        self.average_outcome_a = 0
        self.average_outcome_b = 0
        self.outcome_optional = []
        return

    def roll(self, num_sides):
        outcome = randint(1, num_sides)
        if outcome == num_sides:
            outcome = outcome + self.roll(num_sides)
        return outcome

    def value_check(self, count, entry_list, entry_modifier0):
        for c in range(count):
            try:
                int(entry_list[c].get())
            except ValueError:
                return 0
        try:
            int(entry_modifier0.get())
        except ValueError:
            return 0
        return 1

    def clear_list(self, list):
        list.clear()

    def roll_set(self, count, entry_list, entry_modifier0, outcomes, combobox_list, combobox_die0):
            self.clear_list(outcomes)
            for roll_num in range(10000):
                outcomes_optional = 0
                for c in range(count):
                    outcomes_optional = self.roll(int(combobox_list[c].get())) + int(
                        entry_list[c].get()) + outcomes_optional
                outcome = self.roll(int(combobox_die0.get())) + int(entry_modifier0.get()) + outcomes_optional
                outcomes.append(outcome)
            average_outcome = mean(outcomes)
            return average_outcome

import collections
import random
from math import floor


class General:
    def __init__(self, name, preferred_value, is_king, is_faulty, number_of_traitors, number_of_all_generals):
        self.name = name
        self.preferred_value = preferred_value
        self.is_king = is_king
        self.is_faulty = is_faulty
        self.preferred_values_of_every_general = []
        for i in range(number_of_all_generals):
            self.preferred_values_of_every_general.append(0)
        self.preferred_values_of_every_general[int(self.name[-1])] = self.preferred_value
        self.majority = 0
        self.multiplicity = 0
        self.is_weak_majority = False
        self.number_of_traitors = number_of_traitors
        self.number_of_all_generals = number_of_all_generals

    def count_majority_and_multiplicity_and_weak_majority(self):
        temp_list = self.preferred_values_of_every_general.copy()
        temp_list.sort()
        occurrences = collections.Counter(temp_list)
        self.majority = max(occurrences, key=occurrences.get)
        self.multiplicity = occurrences[self.majority]
        self.is_weak_majority = True if self.multiplicity < (floor(self.number_of_all_generals / 2) +
                                                             self.number_of_traitors + 1) else False


NUMBER_OF_TRAITORS = 1
# number of all generals must be n >= (4 * NUMBER_OF_TRAITORS + 1)
INPUT_OF_ALL_GENERALS = 6
NUMBER_OF_ALL_GENERALS = INPUT_OF_ALL_GENERALS if INPUT_OF_ALL_GENERALS >= (4 * NUMBER_OF_TRAITORS + 1) \
    else (4 * NUMBER_OF_TRAITORS + 1)
NUMBER_OF_ROUNDS = NUMBER_OF_TRAITORS + 1
MAX_VALUE = 3
MIN_VALUE = 0


def main():
    generals = []
    for i in range(NUMBER_OF_ALL_GENERALS):
        generals.append(General("p"+str(i), random.randint(MIN_VALUE, MAX_VALUE), False, False, NUMBER_OF_TRAITORS,
                                NUMBER_OF_ALL_GENERALS))

    # choosing traitors at random
    traitors = []
    while len(traitors) != NUMBER_OF_TRAITORS:
        faulty = random.randint(0, len(generals)-1)
        if faulty in traitors:
            continue
        else:
            traitors.append(faulty)
            generals[faulty].is_faulty = True
    print("List of traitors: ")
    print(traitors)

    # choosing king for every round at random
    kings_order = []
    while len(kings_order) != NUMBER_OF_ROUNDS:
        king = random.randint(0, len(generals)-1)
        if king in kings_order:
            continue
        else:
            kings_order.append(king)
    print("Kings order: ")
    print(kings_order)

    # start of rounds
    for k in range(NUMBER_OF_ROUNDS):
        generals[kings_order[k]].is_king = True

        # round 1
        # send preferred values to all
        for i in range(len(generals)):
            for j in range(len(generals)):
                if j == i:
                    continue
                else:
                    if generals[j].is_faulty:
                        generals[i].preferred_values_of_every_general[j] = random.randint(MIN_VALUE, MAX_VALUE)
                    else:
                        generals[i].preferred_values_of_every_general[j] = generals[j].preferred_value

        # count majority, multiplicity, weak majority for every general
        for i in range(len(generals)):
            generals[i].count_majority_and_multiplicity_and_weak_majority()
            generals[i].preferred_value = generals[i].majority

        # print generals
        for i in range(len(generals)):
            print(generals[i].name, generals[i].preferred_values_of_every_general,
                  "Majority: ", generals[i].majority, "Multiplicity: ", generals[i].multiplicity,
                  "Weak Majority: ", generals[i].is_weak_majority, "King: ", generals[i].is_king,
                  "Faulty: ", generals[i].is_faulty)

        # round 2
        # king sends his preferred value to everyone
        for i in range(len(generals)):
            if generals[i].is_king:
                for j in range(len(generals)):
                    if j == i:
                        generals[i].preferred_values_of_every_general[i] = generals[i].majority
                    else:
                        if generals[j].is_weak_majority:
                            if generals[i].is_faulty:
                                temp_rand = random.randint(MIN_VALUE, MAX_VALUE)
                                generals[j].preferred_value = temp_rand
                                generals[j].preferred_values_of_every_general[j] = temp_rand
                            else:
                                generals[j].preferred_value = generals[i].majority
                                generals[j].preferred_values_of_every_general[j] = generals[i].majority

        print()

        # make current king no king
        generals[kings_order[k]].is_king = False

    # print all final preferred values
    for i in range(len(generals)):
        print(generals[i].preferred_value)

    # print final decision
    final_decision = 0
    for i in range(len(generals)):
        if not generals[i].is_faulty:
            final_decision = generals[i].preferred_value
            break
    print("Final decision: ", final_decision)


if __name__ == "__main__":
    main()
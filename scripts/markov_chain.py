import numpy as np


class MarkovChain:
    """


    """

    def __init__(self, initial_state, states, transition):
        self.initial_state = initial_state
        self.states = states
        self.transition = transition
        self.num_states = len(states)

    def generate(self, sequence_length):
        """
        Given an an initial state and a 2d matrix of probabilites,
        returns a randomly generated, 1D array of a possible state sequence

        :param int sequence_length:  length of markov sequence to be generates
        :return:

        """

        sequence = []
        current_state = self.initial_state
        for i in range(sequence_length):
            sequence.append(current_state)
            p = self.transition[current_state]
            next_state = np.random.choice(a=self.states, p=p)
            current_state = next_state

        return sequence


def main():
    states = [0, 1, 2, 3]
    t = [[0, 1.0, 0, 0], [0, 0, 1.0, 0], [0, 0, 0, 1.0], [1.0, 0, 0, 0]]
    l = 5
    m = MarkovChain(initial_state=0, states=states, transition=t)
    print(m.generate(sequence_length=l))


if __name__ == main():
    main()

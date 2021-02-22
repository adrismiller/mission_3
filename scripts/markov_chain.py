import numpy as np


class MarkovChain:
    """


    """

    def __init__(self, states, prior, transition):
        self.states = states
        self.prior = prior
        self.transition = transition
        self.num_states = len(states)

    def get_initial_state(self):
        """

        :return:
        """
        return np.random.choice(a=self.states, p=self.prior)

    # TODO: make this higher order ???

    def get_new_state(self, current_state):
        """

        :param State current_state:
        :return: State new_state:
        """
        current_state_id = current_state.id
        p = self.transition[current_state_id]
        next_state = np.random.choice(a=self.states, p=p)
        return next_state

    def run(self, sequence_length):
        """
        Given an an initial state and a 2d matrix of probabilites,
        returns a randomly generated, 1D array of a possible state sequence

        :param int sequence_length:  length of markov sequence to be generates
        :return:

        """

        sequence = []
        current_state = self.get_initial_state()

        for i in range(sequence_length):
            sequence.append(current_state)
            next_state = self.get_new_state(current_state)
            current_state = next_state

        return sequence


def main():
    states = [0, 1, 2, 3]
    t = [[0, 1.0, 0, 0], [0, 0, 1.0, 0], [0, 0, 0, 1.0], [1.0, 0, 0, 0]]
    l = 5
    m = MarkovChain(initial_state=0, states=states, transition=t)
    print(m.generate(sequence_length=l))


if __name__ == '__main__':
    main()

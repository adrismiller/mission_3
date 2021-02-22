import numpy as np


class MarkovChain:
    """

    Class representing a MarkovChain that, given a list of states, a prior probability vector, and a transition matrix,
    is able to run a Markov Chain and return the resulting sequence of states.

    :param State[] states: a list of States
    :param float[] prior: a prior probability vector
    :param float[][] transition: a 2D vector representing the transition matrix


    """

    def __init__(self, states, prior, transition):
        self.states = states
        self.prior = prior
        self.transition = transition

    def get_initial_state(self):
        """
        Helper function for self.run -- randomly selects an initial state based on the prior probability
        vector.

        :return: State
        """
        return np.random.choice(a=self.states, p=self.prior)

    # TODO: make this higher order ???

    def get_new_state(self, current_state):
        """
        Helper function for self.run -- randomly selects a next state based on the current_state and the transition
        matrix.

        :param State current_state: state that Markov Chain is currently in
        :return: State new_state:   state that Markov Chain will enter
        """
        current_state_id = current_state.id
        # probability vector for current state
        p = self.transition[current_state_id]
        # randomly select next state based on probabilities
        next_state = np.random.choice(a=self.states, p=p)
        return next_state

    def run(self, sequence_length):
        """
        Given a sequence_length, runs a Markov Chain from a randomly selected

        :param int sequence_length:  length of markov sequence to be generates
        :return: State[] sequence:  sequence of states created by markov model

        """

        sequence = [] # intialize empty sequence
        current_state = self.get_initial_state() # randomly select initial state

        for i in range(sequence_length):
            sequence.append(current_state)
            next_state = self.get_new_state(current_state) # randomly select next state
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

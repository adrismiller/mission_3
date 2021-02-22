import cv2
import numpy as np
import os
from scripts import state, markov_chain


class ImgGenerator():
    """

    """

    def __init__(self, order, input_dir, output_path, num_rows, num_cols, all_states):
        self.order = order
        self.input_dir = input_dir
        self.output_path = output_path
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.all_states = all_states

    def get_all_imgs(self):
        """
        Helper function for generate_img
        :return:
        """
        all_imgs = []

        for s in self.all_states:
            filename = s.name + ".jpeg"
            img_path = os.path.join(self.input_dir, filename)
            img = cv2.imread(img_path)
            img = cv2.resize(img, (300, 300))
            all_imgs.append(img)

        return all_imgs

    def generate_img(self):
        """

        :return:
        """
        # TODO : add check for dimensions of picture being good

        index = 0
        all_imgs = self.get_all_imgs()
        all_rows = []
        for r in range(self.num_rows):
            current_row = []
            for c in range(self.num_cols):
                current_state_id = self.order[index].id
                current_row.append(all_imgs[current_state_id])
                index += 1
            current_row = np.hstack(current_row)
            all_rows.append(current_row)

        img = np.vstack(all_rows)

        cv2.imwrite(self.output_path, img)

def main():

    cwd = os.getcwd()[:-7]

    dog_names = ["rosie", "callie", "venus", "bear", "jamie", "cooper", "winston", "bruno", "maisy",
                 "speedy", "bella"]

    # probability of the first pixel (upper left corner) is each dog
    prior = [.15, .15, .15, .15, .15, .15, .02, .02, .02, .02, .02]

    # probabilty
    rosie_transition = [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    callie_transition = [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    venus_transition = [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    bear_transition = [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    jamie_transition = [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    cooper_transition = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]
    winston_transition = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
    bruno_transition = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]
    maisy_transition = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]
    speedy_transition = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
    bella_transition = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    transition = [rosie_transition, callie_transition, venus_transition, bear_transition, jamie_transition,
                  cooper_transition, winston_transition, bruno_transition, maisy_transition, speedy_transition,
                  bella_transition]

    all_states = []

    for i, dog in enumerate(dog_names):
        new_state = state.State(id=i, name=dog)
        all_states.append(new_state)

    m = markov_chain.MarkovChain(states=all_states, prior=prior, transition=transition)
    sequence = m.run(sequence_length=400)

    output_path = os.path.join(cwd, "outputs")
    output_path = os.path.join(output_path, "example2.jpeg")

    i = ImgGenerator(order=sequence, input_dir=os.path.join(cwd, "photos"), output_path=output_path, num_rows=20,
                     num_cols=20, all_states=all_states)
    i.generate_img()

if __name__ == '__main__':
    main()

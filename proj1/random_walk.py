import random
import numpy as np

action_map = {
    'left': -1,
    'right': 1
}

MAX_STATES = 7


def char_state(i):
    return chr(ord('A') + i)


def execute_random_action(current_state):
    action = action_map.get(random.choice(['left', 'right']))
    new_state = current_state + action
    return new_state


def random_walk_generator():
    current_state = 3  # state D
    next_state = current_state
    yield next_state
    while next_state not in [0, MAX_STATES - 1]:
        next_state = execute_random_action(current_state)
        current_state = next_state
        yield next_state


def get_numpy_episode_and_reward(episode):
    reward = 0 if episode[-1] == 0 else 1
    episode = episode[:-1]
    np_episode = np.zeros((len(episode), MAX_STATES - 2))

    for i, state in enumerate(episode):
        np_episode[i][state - 1] = 1

    return np_episode, reward


def get_state_vector(current_state):
    pass


def td_lambda(episode_gen, alpha, lambda_val, gamma, iterations,
              max_states=MAX_STATES):
    """
    Args:
        :param episode_gen: generator for mdp
        :param alpha: learning rate
        :param lambda_val: lambda in the td-lambda
        :param gamma: discount to be applied for the next step value func
        :param iterations: number of episodes to be run
        :param max_states number of maximum states [ always 7(0-6)]
    Return:
        :return:
    """
    # full episode
    v = np.zeros((1, max_states))
    v[:] = 0.5
    episode = list(episode_gen())
    np_episode, reward = get_numpy_episode_and_reward(episode)

    # todo: vectorize

    print np_episode, reward



def main():
    td_lambda(random_walk_generator, 0.75, 1, 1, 1000)



if __name__ == '__main__':
    main()
import numpy as np
import gymnasium as gym
import random
import matplotlib.pyplot as plt
import time
from IPython.display import clear_output, display

from IPython.display import HTML
from matplotlib import animation
import matplotlib.pyplot as plt


def play_episode(env, Q=None, random_policy=False, max_steps=100, seed=None):
    """Ejecuta un episodio y devuelve sus frames y recompensa total."""
    state, _ = env.reset(seed=seed)
    frames = [env.render()]
    total_reward = 0.0

    for _ in range(max_steps):
        if random_policy:
            action = env.action_space.sample()
        else:
            q_values = Q[state]
            max_q = np.max(q_values)

            # Desempate aleatorio entre acciones con el mismo Q.
            best_actions = np.flatnonzero(q_values == max_q)
            action = int(np.random.choice(best_actions))

        next_state, reward, terminated, truncated, _ = env.step(action)

        frames.append(env.render())
        total_reward += reward
        state = next_state

        if terminated or truncated:
            break

    return frames, total_reward


def frames_to_video(frames, interval=700):
    """Convierte una lista de frames RGB en una animación reproducible en Jupyter."""
    fig = plt.figure(figsize=(4, 4))
    plt.axis("off")

    image = plt.imshow(frames[0])

    def update(frame):
        image.set_data(frame)
        return [image]

    anim = animation.FuncAnimation(
        fig,update,
        frames=frames,
        interval=interval,
        blit=True,
        repeat=True
    )

    plt.close(fig)
    return HTML(anim.to_jshtml())


def initialize_q_table(state_space, action_space):
    return np.zeros((state_space, action_space))


def greedy_policy(Qtable, state):
    # Si hay empate entre varias acciones con el mismo Q, desempata al azar.
    max_q = np.max(Qtable[state])
    best_actions = np.flatnonzero(Qtable[state] == max_q)
    return int(np.random.choice(best_actions))


def epsilon_greedy_policy(Qtable, state, epsilon, env):
    if random.random() < epsilon:
        return env.action_space.sample()

    return greedy_policy(Qtable, state)


def train_q_learning(
    env,
    Qtable,
    n_episodes=5000,
    learning_rate=0.7,
    gamma=0.95,
    max_epsilon=1.0,
    min_epsilon=0.05,
    decay_rate=0.001,
    max_steps=100,
    start_episode=0,
):
    rewards = []

    for episode in range(n_episodes):
        state, _ = env.reset()
        total_reward = 0

        global_episode = start_episode + episode
        epsilon = min_epsilon + (
            max_epsilon - min_epsilon
        ) * np.exp(-decay_rate * global_episode)

        for _ in range(max_steps):
            action = epsilon_greedy_policy(
                Qtable, state, epsilon, env
            )

            next_state, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated

            best_next_q = 0.0 if done else np.max(Qtable[next_state])

            td_target = reward + gamma * best_next_q
            td_error = td_target - Qtable[state, action]

            Qtable[state, action] += learning_rate * td_error

            state = next_state
            total_reward += reward
            
            if done:
                break

        rewards.append(total_reward)

    return Qtable, rewards


def evaluate_q_policy(env, Qtable, n_episodes=100, max_steps=100):
    episode_rewards = []

    for _ in range(n_episodes):
        state, _ = env.reset()
        total_reward = 0

        for _ in range(max_steps):
            action = greedy_policy(Qtable, state)

            next_state, reward, terminated, truncated, _ = env.step(action)

            state = next_state
            total_reward += reward

            if terminated or truncated:
                break

        episode_rewards.append(total_reward)

    return np.mean(episode_rewards), np.std(episode_rewards)


def show_frame(env, title=''):
    frame = env.render()
    plt.figure(figsize=(4, 4))
    plt.imshow(frame)
    plt.axis('off')
    plt.title(title)
    display(plt.gcf())
    plt.close()

if __name__ == "__main__":
    env = gym.make(
        "FrozenLake-v1",
        map_name="4x4",
        is_slippery=False,
        render_mode="rgb_array"
    )

    state, info = env.reset()

    print("Estado inicial:", state)
    print("Número de estados:", env.observation_space.n)
    print("Número de acciones:", env.action_space.n)
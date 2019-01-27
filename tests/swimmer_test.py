from mjrl.utils.gym_env import GymEnv
from mjrl.policies.gaussian_mlp import MLP
from mjrl.baselines.quadratic_baseline import QuadraticBaseline
from mjrl.baselines.mlp_baseline import MLPBaseline
from mjrl.algos.npg_cg import NPG
from mjrl.utils.train_agent import train_agent
import mjrl.envs
import time as timer
SEED = 500

env_name = 'mjrl_swimmer-v0'
policy = MLP(obs_dim=12, act_dim=4, hidden_sizes=(32,32), seed=SEED)
baseline = MLPBaseline(obs_dim=12, reg_coef=1e-3, batch_size=64, epochs=5, learn_rate=1e-3)
agent = NPG(env_name, policy, baseline, normalized_step_size=0.1, seed=SEED, save_logs=True)

ts = timer.time()
train_agent(job_name='swimmer_exp1',
            agent=agent,
            seed=SEED,
            niter=50,
            gamma=0.995,
            gae_lambda=0.97,
            num_cpu=1,
            sample_mode='trajectories',
            num_traj=10,
            save_freq=5,
            evaluation_rollouts=None)
print("time taken = %f" % (timer.time()-ts))

e = GymEnv(e_name)
e.env.env.visualize_policy_offscreen(policy, num_episodes=5, horizon=e.horizon, mode='evaluation')
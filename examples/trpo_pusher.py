


from rllab.algos.trpo import TRPO
from rllab.baselines.linear_feature_baseline import LinearFeatureBaseline
from rllab.envs.gym_env import GymEnv
from rllab.envs.normalized_env import normalize
from rllab.misc.instrument import stub, run_experiment_lite
from rllab.policies.gaussian_mlp_policy import GaussianMLPPolicy

stub(globals())

#env = normalize(GymEnv("InvertedPendulum-v1"))
env = normalize(GymEnv("Pusher-v1"))

policy = GaussianMLPPolicy(
    env_spec=env.spec,
    # The neural network policy should have two hidden layers, each with 32 hidden units.
    hidden_sizes=(300, 400)
)

baseline = LinearFeatureBaseline(env_spec=env.spec)

algo = TRPO(
    env=env,
    policy=policy,
    baseline=baseline,
    batch_size=20000,
    #max_path_length=env.horizon, #should probably reduce this to 200 or something
    max_path_length=500,
    n_itr=1000,
    discount=1.0, #should probaby make this equal to 1.0
    step_size=0.01,
    # Uncomment both lines (this and the plot parameter below) to enable plotting
    plot=True,
)

run_experiment_lite(
    algo.train(),
    # Number of parallel workers for sampling
    n_parallel=2,
    # Only keep the snapshot parameters for the last iteration
    snapshot_mode="last",
    # Specifies the seed for the experiment. If this is not provided, a random seed
    # will be used
    seed=1,
    plot=True,
)

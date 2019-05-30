from baselines.common import plot_util as pu
import matplotlib.pyplot as plt
import numpy as np
import json
import os

if not os.path.exists('pics/'):
    os.makedirs('pics/')

results = pu.load_results('logs/', verbose=True)

for r in results:
    with open("{}/0.0.monitor.csv".format(r.dirname), "r") as f:
        info = f.readline()
        meta = json.loads(info[1:])
    game = meta['env_id']
    fig = plt.figure()
    plt.plot(np.cumsum(r.monitor.l), pu.smooth(r.monitor.r, radius=10))
    fig.suptitle(game, fontsize=18)
    plt.savefig('pics/{}.png'.format(game))



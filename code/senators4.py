from __future__ import division, print_function

import json
import pandas as pd


with open("followers.json", "r") as f:
    followers = json.load(f)

ids = [sen["id"] for sen in senators["users"]]
M = np.asmatrix(np.zeros([100, 100]))
for i, fol in enumerate(followers):
    print(i)
    for j, idj in enumerate(ids):
        if idj in fol:
            M[i, j] = 1
M_df = pd.DataFrame(M)
M_df.to_csv('followersmatrix.csv', encoding='utf-8', index_label=False)



#   Copyright 2020 The PyMC Developers
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from pymc3 import HalfCauchy, Normal, sample, Model, loo
import numpy as np

"""Original Stan model

data {
  int<lower=0> J; // number of schools
  real y[J]; // estimated treatment effects
  real<lower=0> sigma[J]; // s.e. of effect estimates
}
parameters {
  real mu;
  real<lower=0> tau;
  real eta[J];
}
transformed parameters {
  real theta[J];
  for (j in 1:J)
    theta[j] <- mu + tau * eta[j];
}
model {
  eta ~ normal(0, 1);
  y ~ normal(theta, sigma);
}
"""

J = 8
y = np.array([28, 8, -3, 7, -1, 1, 18, 12])
sigma = np.array([15, 10, 16, 11, 9, 11, 10, 18])

with Model() as schools:

    eta = Normal("eta", 0, 1, shape=J)
    mu = Normal("mu", 0, sigma=1e6)
    tau = HalfCauchy("tau", 25)

    theta = mu + tau * eta

    obs = Normal("obs", theta, sigma=sigma, observed=y)


def run(n=1000):
    if n == "short":
        n = 50
    with schools:
        tr = sample(n)
        loo(tr)


if __name__ == "__main__":
    run()

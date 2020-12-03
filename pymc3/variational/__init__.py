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

# commonly used
from pymc3.variational import updates
from pymc3.variational.updates import (
    sgd,
    apply_momentum,
    momentum,
    apply_nesterov_momentum,
    adagrad_window,
    nesterov_momentum,
    adagrad,
    rmsprop,
    adadelta,
    adam,
    adamax,
    norm_constraint,
    total_norm_constraint,
)

from pymc3.variational import inference
from pymc3.variational.inference import (
    ADVI,
    FullRankADVI,
    SVGD,
    ASVGD,
    NFVI,
    Inference,
    KLqp,
    ImplicitGradient,
    fit,
)

from pymc3.variational import approximations
from pymc3.variational.approximations import (
    MeanField,
    FullRank,
    Empirical,
    NormalizingFlow,
    sample_approx,
)
from pymc3.variational import opvi
from pymc3.variational.opvi import Group, Approximation

# special
from pymc3.variational.stein import Stein
from pymc3.variational import flows
from pymc3.variational import operators
from pymc3.variational import test_functions
from pymc3.variational import callbacks

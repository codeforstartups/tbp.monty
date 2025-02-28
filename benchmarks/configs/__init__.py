# Copyright 2025 Thousand Brains Project
# Copyright 2022-2024 Numenta Inc.
#
# Copyright may exist in Contributors' modifications
# and/or contributions to the work.
#
# Use of this source code is governed by the MIT
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

from .monty_world_experiments import CONFIGS as MONTY_WORLD
from .pretraining_experiments import CONFIGS as PRETRAININGS
from .ycb_experiments import CONFIGS as YCB
from .first_experiment import CONFIGS as FIRST_EXPERIMENT
from .pretraining_tutorial_train import CONFIGS as PRETRAINING_TUTORIAL_TRAIN
from .pretraining_tutorial_eval import CONFIGS as PRETRAINING_TUTORIAL_EVAL

CONFIGS = dict()
CONFIGS.update(PRETRAININGS)
CONFIGS.update(YCB)
CONFIGS.update(MONTY_WORLD)
CONFIGS.update(FIRST_EXPERIMENT)
CONFIGS.update(PRETRAINING_TUTORIAL_TRAIN)
CONFIGS.update(PRETRAINING_TUTORIAL_EVAL)

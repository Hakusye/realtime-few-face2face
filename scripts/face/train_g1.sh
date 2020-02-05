# Copyright (c) 2019, NVIDIA Corporation. All rights reserved.
#
# This work is made available
# under the Nvidia Source Code License (1-way Commercial).
# To view a copy of this license, visit
# https://nvlabs.github.io/few-shot-vid2vid/License.txt

python3 train.py --name face --dataset_mode fewshot_face \
--adaptive_spade --warp_ref --spade_combine --batchSize 1 --continue_train --which_epoch 50 --lr 0.0002

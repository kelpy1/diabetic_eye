#!/bin/bash

REL_PATH_TO_SCRIPT=$(dirname "${BASH_SOURCE[0]}")
cd "${REL_PATH_TO_SCRIPT}"
NAME="intel_cancer"
IMAGENAME="${NAME}"
CONTNAME="--name=${NAME}"
NET="--net=host"

CUDA_DEVICES=$(\ls /dev/nvidia* | xargs -I{} echo '--device {}:{}')
CUDA_SO=$(\ls /usr/lib/x86_64-linux-gnu/libcuda.* | xargs -I{} echo '-v {}:{}')

VOLUMES="-v $(pwd)/..:/workdir"
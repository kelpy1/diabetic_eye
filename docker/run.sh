#!/bin/bash

source params.sh

nvidia-docker run --rm -it ${CUDA_DEVICES} ${CUDA_SO} ${NET} ${VOLUMES} ${CONTNAME} ${IMAGENAME} bash
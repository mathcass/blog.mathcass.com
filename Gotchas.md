# Anaconda + Pyenv

I created a new env within `anaconda3-4.0.0` with `conda create -n tensorflow
--clone root` which I expected to create a new env that I could work with easily. 

There's a check with `pyenv` that ensures that a `conda` executable is in the
directory `anaconda3-4.0.0/envs/tensorflow/bin` that wasn't there. I'm assuming
that the creation of a cloned directory just uses a linked conda bin somehow
that wasn't working as expected here.

As a workaround, I linked conda to the tensorflow env with `ln`.

# OpenCV

From the Trainspotting talk, the speaker suggests installing OpenCV from Anaconda via:

    conda install -c https://conda.binstar.org/menpo opencv3


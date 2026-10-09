#!/usr/bin/env bash
# Build Qwen's optional CUDA kernels with uv-managed CUDA 13.0 tooling.
set -euo pipefail
cd "$(dirname "$0")/.."

# Bootstrap build tools before building the extension against our pinned torch.
uv sync --group notebooks --group cuda-build --no-install-package causal-conv1d
export CUDA_HOME
CUDA_HOME="$(.venv/bin/python -c 'import sysconfig; print(sysconfig.get_path("purelib") + "/nvidia/cu13")')"
# NVIDIA's runtime wheel supplies the versioned library; the linker needs this name.
if [[ ! -e "$CUDA_HOME/lib/libcudart.so" ]]; then
  ln -s libcudart.so.13 "$CUDA_HOME/lib/libcudart.so"
fi
export MAX_JOBS="${MAX_JOBS:-2}"
export CAUSAL_CONV1D_FORCE_BUILD=TRUE
uv sync --group notebooks --group cuda-build --no-build-isolation-package causal-conv1d
uv run --no-sync --group notebooks python -c \
  'from transformers.models.qwen3_5.modeling_qwen3_5 import is_fast_path_available; print("Qwen DeltaNet fast path:", is_fast_path_available); assert is_fast_path_available'

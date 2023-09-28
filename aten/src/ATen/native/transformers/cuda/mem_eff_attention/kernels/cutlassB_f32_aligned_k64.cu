/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
 */
// This file is auto-generated. See "generate_kernels.py"
#define TORCH_ASSERT_NO_OPERATORS
#include <ATen/native/transformers/cuda/mem_eff_attention/kernel_backward.h>
using namespace PyTorchMemEffAttention;
__global__ void __launch_bounds__(
    AttentionBackwardKernel<cutlass::arch::Sm50, float, true, false, false, 64, 64, 64>::kNumThreads,
    AttentionBackwardKernel<cutlass::arch::Sm50, float, true, false, false, 64, 64, 64>::kMinBlocksPerSm)
fmha_cutlassB_f32_aligned_64x64_k64_sm50(typename AttentionBackwardKernel<cutlass::arch::Sm50, float, true, false, false, 64, 64, 64>::Params p) {
#ifdef __CUDA_ARCH__
#if __CUDA_ARCH__ >= 500
#if __CUDA_ARCH__ < 700
  if (!p.advance_to_block()) {
    return;
  }
  AttentionBackwardKernel<cutlass::arch::Sm50, float, true, false, false, 64, 64, 64>::attention_kernel(p);
  return;
#endif
#endif
    printf(
        "FATAL: kernel `fmha_cutlassB_f32_aligned_64x64_k64_sm50` is for sm50-sm70, but was built for sm%d\n",
        int(__CUDA_ARCH__ + 0) / 10);
#endif
}
__global__ void __launch_bounds__(
    AttentionBackwardKernel<cutlass::arch::Sm70, float, true, false, false, 64, 64, 64>::kNumThreads,
    AttentionBackwardKernel<cutlass::arch::Sm70, float, true, false, false, 64, 64, 64>::kMinBlocksPerSm)
fmha_cutlassB_f32_aligned_64x64_k64_sm70(typename AttentionBackwardKernel<cutlass::arch::Sm70, float, true, false, false, 64, 64, 64>::Params p) {
#ifdef __CUDA_ARCH__
#if __CUDA_ARCH__ >= 700
#if __CUDA_ARCH__ < 750
  if (!p.advance_to_block()) {
    return;
  }
  AttentionBackwardKernel<cutlass::arch::Sm70, float, true, false, false, 64, 64, 64>::attention_kernel(p);
  return;
#endif
#endif
    printf(
        "FATAL: kernel `fmha_cutlassB_f32_aligned_64x64_k64_sm70` is for sm70-sm75, but was built for sm%d\n",
        int(__CUDA_ARCH__ + 0) / 10);
#endif
}
__global__ void __launch_bounds__(
    AttentionBackwardKernel<cutlass::arch::Sm75, float, true, false, false, 64, 64, 64>::kNumThreads,
    AttentionBackwardKernel<cutlass::arch::Sm75, float, true, false, false, 64, 64, 64>::kMinBlocksPerSm)
fmha_cutlassB_f32_aligned_64x64_k64_sm75(typename AttentionBackwardKernel<cutlass::arch::Sm75, float, true, false, false, 64, 64, 64>::Params p) {
#ifdef __CUDA_ARCH__
#if __CUDA_ARCH__ >= 750
#if __CUDA_ARCH__ < 800
  if (!p.advance_to_block()) {
    return;
  }
  AttentionBackwardKernel<cutlass::arch::Sm75, float, true, false, false, 64, 64, 64>::attention_kernel(p);
  return;
#endif
#endif
    printf(
        "FATAL: kernel `fmha_cutlassB_f32_aligned_64x64_k64_sm75` is for sm75-sm80, but was built for sm%d\n",
        int(__CUDA_ARCH__ + 0) / 10);
#endif
}
__global__ void __launch_bounds__(
    AttentionBackwardKernel<cutlass::arch::Sm80, float, true, false, false, 64, 64, 64>::kNumThreads,
    AttentionBackwardKernel<cutlass::arch::Sm80, float, true, false, false, 64, 64, 64>::kMinBlocksPerSm)
fmha_cutlassB_f32_aligned_64x64_k64_sm80(typename AttentionBackwardKernel<cutlass::arch::Sm80, float, true, false, false, 64, 64, 64>::Params p) {
#ifdef __CUDA_ARCH__
#if __CUDA_ARCH__ >= 800
#if __CUDA_ARCH__ < 1000
  if (!p.advance_to_block()) {
    return;
  }
  AttentionBackwardKernel<cutlass::arch::Sm80, float, true, false, false, 64, 64, 64>::attention_kernel(p);
  return;
#endif
#endif
    printf(
        "FATAL: kernel `fmha_cutlassB_f32_aligned_64x64_k64_sm80` is for sm80-sm100, but was built for sm%d\n",
        int(__CUDA_ARCH__ + 0) / 10);
#endif
}


// Copyright (c) 2023, Tri Dao.

// Splitting the different head dimensions to different files to speed up compilation.
// This file is auto-generated. See "generate_kernels.py"

#define TORCH_ASSERT_NO_OPERATORS
#include <ATen/native/transformers/cuda/flash_attn/flash_fwd_launch_template.h>
namespace pytorch_flash{

template<>
void run_mha_fwd_<cutlass::bfloat16_t, 32>(Flash_fwd_params &params, cudaStream_t stream) {
    run_mha_fwd_hdim32<cutlass::bfloat16_t>(params, stream);
}
} // namespace pytorch_flash

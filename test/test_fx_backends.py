# Owner(s): ["oncall: fx"]

import os
import pickle
import importlib
import logging
from typing import List, Tuple

import torch
from torch.fx._symbolic_trace import symbolic_trace

from torch.fx.passes.backends.nvfuser import NvFuserBackend

from torch.testing._internal.common_utils import run_tests, instantiate_parametrized_tests
from torch.testing._internal.jit_utils import JitTestCase

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class HF_T5_Partial(torch.nn.Module):

    def inputs_meta(self):
        return [
            (torch.Size([512, 512]), torch.float32),
            (torch.Size([512, 512]), torch.float32),
            (torch.Size([512, 512]), torch.float32),
            (torch.Size([512, 512]), torch.float32),
            (torch.Size([512]), torch.float32),
            (torch.Size([2048, 512]), torch.float32),
            (torch.Size([512, 2048]), torch.float32),
            (torch.Size([512]), torch.float32),
            (torch.Size([8, 1024, 512]), torch.float32),
            (torch.Size([8, 8, 1024, 1024]), torch.float32),
        ]

    def forward(self, primals_1, primals_2, primals_3, primals_4, primals_5, primals_6, primals_7, primals_8, primals_9, primals_10):
        pow_1 = torch.ops.aten.pow(primals_9, 2)
        mean = torch.ops.aten.mean(pow_1, [-1], True);  pow_1 = None
        add = torch.ops.aten.add(mean, 1e-06);  mean = None
        rsqrt = torch.ops.aten.rsqrt(add);  add = None
        mul = torch.ops.aten.mul(primals_9, rsqrt)
        mul_1 = torch.ops.aten.mul(primals_5, mul)
        t = torch.ops.aten.t(primals_3);  primals_3 = None
        view = torch.ops.aten.view(mul_1, [8192, 512])
        mm = torch.ops.aten.mm(view, t)
        _unsafe_view = torch.ops.aten._unsafe_view(mm, [8, 1024, 512]);  mm = None
        view_1 = torch.ops.aten.view(_unsafe_view, [8, -1, 8, 64]);  _unsafe_view = None
        transpose = torch.ops.aten.transpose(view_1, 1, 2);  view_1 = None
        t_1 = torch.ops.aten.t(primals_1);  primals_1 = None
        view_2 = torch.ops.aten.view(mul_1, [8192, 512])
        mm_1 = torch.ops.aten.mm(view_2, t_1)
        _unsafe_view_1 = torch.ops.aten._unsafe_view(mm_1, [8, 1024, 512]);  mm_1 = None
        view_3 = torch.ops.aten.view(_unsafe_view_1, [8, -1, 8, 64]);  _unsafe_view_1 = None
        transpose_1 = torch.ops.aten.transpose(view_3, 1, 2);  view_3 = None
        t_2 = torch.ops.aten.t(primals_4);  primals_4 = None
        view_4 = torch.ops.aten.view(mul_1, [8192, 512]);  mul_1 = None
        mm_2 = torch.ops.aten.mm(view_4, t_2)
        _unsafe_view_2 = torch.ops.aten._unsafe_view(mm_2, [8, 1024, 512]);  mm_2 = None
        view_5 = torch.ops.aten.view(_unsafe_view_2, [8, -1, 8, 64]);  _unsafe_view_2 = None
        transpose_2 = torch.ops.aten.transpose(view_5, 1, 2);  view_5 = None
        transpose_3 = torch.ops.aten.transpose(transpose_1, 3, 2);  transpose_1 = None
        expand = torch.ops.aten.expand(transpose, [8, 8, 1024, 64]);  transpose = None
        clone = torch.ops.aten.clone(expand, memory_format = torch.contiguous_format);  expand = None
        _unsafe_view_3 = torch.ops.aten._unsafe_view(clone, [64, 1024, 64]);  clone = None
        expand_1 = torch.ops.aten.expand(transpose_3, [8, 8, 64, 1024]);  transpose_3 = None
        clone_1 = torch.ops.aten.clone(expand_1, memory_format = torch.contiguous_format);  expand_1 = None
        _unsafe_view_4 = torch.ops.aten._unsafe_view(clone_1, [64, 64, 1024]);  clone_1 = None
        bmm = torch.ops.aten.bmm(_unsafe_view_3, _unsafe_view_4)
        _unsafe_view_5 = torch.ops.aten._unsafe_view(bmm, [8, 8, 1024, 1024]);  bmm = None
        add_ = torch.ops.aten.add_(_unsafe_view_5, primals_10);  _unsafe_view_5 = primals_10 = None
        _softmax = torch.ops.aten._softmax(add_, -1, False);  add_ = None
        expand_2 = torch.ops.aten.expand(_softmax, [8, 8, 1024, 1024])
        view_6 = torch.ops.aten.view(expand_2, [64, 1024, 1024]);  expand_2 = None
        expand_3 = torch.ops.aten.expand(transpose_2, [8, 8, 1024, 64]);  transpose_2 = None
        clone_2 = torch.ops.aten.clone(expand_3, memory_format = torch.contiguous_format);  expand_3 = None
        _unsafe_view_6 = torch.ops.aten._unsafe_view(clone_2, [64, 1024, 64]);  clone_2 = None
        bmm_1 = torch.ops.aten.bmm(view_6, _unsafe_view_6)
        _unsafe_view_7 = torch.ops.aten._unsafe_view(bmm_1, [8, 8, 1024, 64]);  bmm_1 = None
        transpose_4 = torch.ops.aten.transpose(_unsafe_view_7, 1, 2);  _unsafe_view_7 = None
        clone_3 = torch.ops.aten.clone(transpose_4, memory_format = torch.contiguous_format);  transpose_4 = None
        view_7 = torch.ops.aten.view(clone_3, [8, -1, 512]);  clone_3 = None
        t_3 = torch.ops.aten.t(primals_2);  primals_2 = None
        view_8 = torch.ops.aten.view(view_7, [8192, 512]);  view_7 = None
        mm_3 = torch.ops.aten.mm(view_8, t_3)
        _unsafe_view_8 = torch.ops.aten._unsafe_view(mm_3, [8, 1024, 512]);  mm_3 = None
        add_1 = torch.ops.aten.add(primals_9, _unsafe_view_8);  _unsafe_view_8 = None
        pow_2 = torch.ops.aten.pow(add_1, 2)
        mean_1 = torch.ops.aten.mean(pow_2, [-1], True);  pow_2 = None
        add_2 = torch.ops.aten.add(mean_1, 1e-06);  mean_1 = None
        rsqrt_1 = torch.ops.aten.rsqrt(add_2);  add_2 = None
        mul_2 = torch.ops.aten.mul(add_1, rsqrt_1)
        mul_3 = torch.ops.aten.mul(primals_8, mul_2)
        t_4 = torch.ops.aten.t(primals_6);  primals_6 = None
        view_9 = torch.ops.aten.view(mul_3, [8192, 512]);  mul_3 = None
        mm_4 = torch.ops.aten.mm(view_9, t_4)
        _unsafe_view_9 = torch.ops.aten._unsafe_view(mm_4, [8, 1024, 2048]);  mm_4 = None
        relu = torch.ops.aten.relu(_unsafe_view_9);  _unsafe_view_9 = None
        t_5 = torch.ops.aten.t(primals_7);  primals_7 = None
        view_10 = torch.ops.aten.view(relu, [8192, 2048])
        mm_5 = torch.ops.aten.mm(view_10, t_5)
        _unsafe_view_10 = torch.ops.aten._unsafe_view(mm_5, [8, 1024, 512]);  mm_5 = None
        add_3 = torch.ops.aten.add(add_1, _unsafe_view_10);  _unsafe_view_10 = None
        return [add_3, rsqrt, _unsafe_view_3, t_3, _softmax, view_6, mul_2, t, view_9, t_1, primals_5, add_1, _unsafe_view_4, view_2, view_10, t_5, t_2, primals_8, view_4, view_8, rsqrt_1, primals_9, t_4, mul, _unsafe_view_6, relu, view]


class TestFxNvFuserBackend(JitTestCase):

    def _generate_random_inputs(self, device, inputs_meta: List[Tuple[torch.Size, torch.dtype]]):
        inputs = []
        for meta in inputs_meta:
            shape, dtype = meta

            if dtype in {torch.int, torch.int32, torch.int64, torch.bool, torch.int, torch.uint8}:
                input = torch.randint(0, 1, shape, dtype=dtype, device=device)
            else:
                input = torch.rand(shape, dtype=dtype, device=device)

            inputs.append(input)

        return inputs

    def test_nvfuser_backend(self):
        device = 'cuda'

        m = HF_T5_Partial()
        m.to(device)

        traced = symbolic_trace(m)

        nvfuser = NvFuserBackend()
        compiled_module = nvfuser.compile(traced)

        inputs = self._generate_random_inputs(device, m.inputs_meta())

        eager_result = m(*inputs)
        nvfuser_result = compiled_module(*inputs)

        torch.testing.assert_close(eager_result, nvfuser_result, rtol=1e-5, atol=1e-5)

instantiate_parametrized_tests(TestFxNvFuserBackend)

if __name__ == "__main__":
    run_tests()

from setuptools import setup
from torch.utils.cpp_extension import CUDAExtension, BuildExtension
import os
import glob


def get_extensions():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    main_file = glob.glob(os.path.join(this_dir, '*.cpp'))
    source_cuda = glob.glob(os.path.join(this_dir, 'src', '*.cu'))
    os.environ["CC"] = "g++"
    sources = main_file + source_cuda
    extra_compile_args = {"cxx": ['-std=c++14']}
    define_macros = []
    include_dirs = [this_dir]
    define_macros += [("WITH_CUDA", None)]
    extra_compile_args["nvcc"] = [
        "-DCUDA_HAS_FP16=1",
        "-D__CUDA_NO_HALF_OPERATORS__",
        "-D__CUDA_NO_HALF_CONVERSIONS__",
        "-D__CUDA_NO_HALF2_OPERATORS__",
        '-gencode', 'arch=compute_60,code=sm_60',
        '-gencode', 'arch=compute_61,code=sm_61',
        '-gencode', 'arch=compute_70,code=sm_70',
        '-gencode', 'arch=compute_70,code=compute_70',
        '-gencode', 'arch=compute_37,code=sm_37',
        '-gencode', 'arch=compute_50,code=sm_50',
        '-gencode', 'arch=compute_37,code=compute_37',
        '-gencode', 'arch=compute_60,code=compute_60',
        '-gencode', 'arch=compute_61,code=compute_61',
        '-gencode', 'arch=compute_50,code=compute_50',
    ]
    CC = os.environ.get("CC", None)
    if CC is not None:
        extra_compile_args["nvcc"].append("-ccbin={}".format(CC))
    ext_modules = [
        CUDAExtension(
            name='_ext',
            sources=sources,
            include_dirs=include_dirs,
            define_macros=define_macros,
            extra_compile_args=extra_compile_args,
        )
    ]
    return ext_modules


setup(
    ext_modules=get_extensions(),
    cmdclass={'build_ext': BuildExtension}
)

from ipykernel.kernelapp import IPKernelApp
from . import CocalcKernel

IPKernelApp.launch_instance(kernel_class=CocalcKernel)
from ipykernel.kernelbase import Kernel

__version__ = '0.1'

class CocalcKernel(Kernel):
    implementation = 'cocalc_kernel'
    implementation_version = __version__
    language = 'sagemath'
    language_version = '7.6'
    language_info = {
        'name': 'sage',
        'mimetype': 'text/x-python',
        'file_extension': '.sage',
    }
    banner = "CoCalc kernel Hal testing"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            stream_content = {'name': 'stdout', 'text': code}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
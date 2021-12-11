from subprocess import CompletedProcess, run
from settings import DEFAULT_ENCODER, DEFAULT_FONT_FILE_PATH
from loguru import logger


class Processor(object):

    def __init__(self, encoder=DEFAULT_ENCODER, font_file_path=DEFAULT_FONT_FILE_PATH):
        self.encoder = encoder
        self.font_file_path = font_file_path

    def process(self,
                input_file_path: str,
                output_file_path: str,
                mark_text: str = '',
                cycle: int = 5):
        cmd = f"ffmpeg -y -i {input_file_path} -vf " \
            + f'''"drawtext=fontfile={self.font_file_path}:fontsize=20:fontcolor=white@1:text='{mark_text}':''' \
            + f"x=if(eq(mod(t\,{cycle})\,0)\,rand(0\,(W-tw))\,x):" \
            + f'y=if(eq(mod(t\,{cycle})\,0)\,rand(0\,(H-th))\,y)"' \
            + f" -c:v {self.encoder} -crf 23 -c:a copy {output_file_path}"
        logger.info(f'processor command {cmd}')
        result: CompletedProcess = run(cmd, shell=True)
        return result.returncode == 0

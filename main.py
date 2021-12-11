from posixpath import join
from subprocess import Popen
from processor import Processor
from processor import Processor
from settings import VIDEO_DIR

processor = Processor()
input_file_path = join(VIDEO_DIR, 'input.mp4')
output_file_path = join(VIDEO_DIR, 'output.mp4')
processor.process(input_file_path=input_file_path,
                  output_file_path=output_file_path,
                  mark_text='崔庆才')

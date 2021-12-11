from environs import Env
import platform
from os.path import dirname, abspath, join


env = Env()
env.read_env()

# definition of flags
IS_WINDOWS = platform.system().lower() == 'windows'

# definition of dirs
ROOT_DIR = dirname(abspath(__file__))
LOG_DIR = join(ROOT_DIR, env.str('LOG_DIR', 'logs'))
VIDEO_DIR = join(ROOT_DIR, env.str('VIDEO_DIR', 'videos'))
FONT_DIR = join(ROOT_DIR, env.str('FONT_DIR', 'fonts'))

# definition of environments
DEV_MODE, TEST_MODE, PROD_MODE = 'dev', 'test', 'prod'
APP_ENV = env.str('APP_ENV', DEV_MODE).lower()
APP_DEBUG = env.bool('APP_DEBUG', True if APP_ENV == DEV_MODE else False)
APP_DEV = IS_DEV = APP_ENV == DEV_MODE
APP_PROD = IS_PROD = APP_ENV == PROD_MODE
APP_TEST = IS_TEST = APP_ENV == TEST_MODE


DEFAULT_ENCODER = 'libx264'
DEFAULT_FONT_FILE_PATH = join(FONT_DIR, 'msyh.ttf')

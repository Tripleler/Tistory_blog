import os
from pathlib import Path
import platform
dir = Path('test')
print(os.access(dir, os.X_OK))

# def is_writeable(dir, test=False):  # utils.general
#     # Return True if directory has write permissions, test opening a file with write permissions if test=True
#     if test:  # method 1
#         file = Path(dir) / 'tmp.txt'
#         try:
#             with open(file, 'w'):  # open file with write permissions
#                 pass
#             file.unlink()  # remove file
#             return True
#         except OSError:
#             return False
#     else:  # method 2
#         print('here')
#         return os.access(dir, os.R_OK)  # possible issues on Windows
#
#
# def user_config_dir(dir='test', env_var='test2'):  # utils.general
#     # Return path of user configuration directory. Prefer environment variable if exists. Make dir if required.
#     env = os.getenv(env_var)
#     if env:
#         path = Path(env)  # use environment variable
#     else:
#         cfg = {'Windows': 'AppData/Roaming', 'Linux': '.config', 'Darwin': 'Library/Application Support'}  # 3 OS dirs
#         path = Path.home() / cfg.get(platform.system(), '')  # OS-specific config dir
#         path = (path if is_writeable(path) else Path('/tmp')) / dir  # GCP and AWS lambda fix, only /tmp is writeable
#     path.mkdir(exist_ok=True)  # make if required
#     return path
#
#
# CONFIG_DIR = user_config_dir()
# print(CONFIG_DIR)

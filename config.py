import sys
import os
lib_path = os.path.join(os.path.dirname(__file__), 'libs')
if lib_path not in sys.path:
    sys.path.append(lib_path)

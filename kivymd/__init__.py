# -*- coding: utf-8 -*-

import os

from kivy import Logger

__version_info__ = (0, 4, 1)
__version__ = '0.4.1'

path = os.path.dirname(__file__)
fonts_path = os.path.join(path, "fonts/")
images_path = os.path.join(path, 'images/')

Logger.info("KivyMD: KivyMD version: {}".format(__version__))

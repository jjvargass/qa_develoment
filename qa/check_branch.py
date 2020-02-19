#!/usr/bin/python
# -*- coding: utf8 -*-

import os
from git import Repo
import logging


logging.basicConfig()
_logger = logging.getLogger('CHECK_BRANCH')
_logger.setLevel(logging.DEBUG)

max_branche = 15
path = os.getcwd()
repo = Repo(path)

all_branches = []
for ref in repo.git.branch('-r').split('\n'):
    name = ref.split('/')[1]
    if ('HEAD' in name) or ('dev' in name) or ('tes' in name) or ('maste' in name): 
        pass
    else:
        all_branches.append(name)

_logger.info("=================================")
_logger.info("RESULTADO CHECK BRANCH:")
_logger.info("====")
if len(all_branches) >= max_branche:
    for i in all_branches:
        _logger.info(i)
    _logger.error('A superado el numero maximo de branch')
    raise Exception('A superado el numero maximo de branch')
else:
    _logger.info('A cumplido con el lineamiento de limpieza de brachs\n')


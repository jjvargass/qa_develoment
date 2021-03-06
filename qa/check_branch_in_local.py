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

_logger.info("=================================")
_logger.info("         VALIDAR BRANCH          ")
_logger.info("=================================")
_logger.info("TODOS LOS BRANCH")
_logger.info("====")
for branch in repo.git.branch('-r').split('\n'):
    _logger.info(branch.lstrip())
_logger.info("=================================")
_logger.info("BRANCH INNECESARIO")
_logger.info("====")
for ref in repo.git.branch('-r').split('\n'):
    name = ref.split('/')[1]   # output is origin/develop for this reason it is [1]
    if ('HEAD' in name) or ('develop' in name) or ('release' in name) or ('maste' in name):
        pass
    else:
        _logger.info(ref.lstrip())
        all_branches.append(name)
_logger.info("=================================")
_logger.info(" RESULTADO VALIDAR BRANCH:")
_logger.info("====")
_logger.info('Branches innecesarios: ' + str(len(all_branches)))
_logger.info('Limite branches innecesarios: ' + str(max_branche))
if len(all_branches) >= max_branche:
    for i in all_branches:
        _logger.info(i)
    _logger.error('Ha superado el numero maximo de branch')
    raise Exception('Ha superado el numero maximo de branch')
else:
    _logger.info('Ha cumplido con el lineamiento de limpieza de brachs')
    _logger.info("=================================")


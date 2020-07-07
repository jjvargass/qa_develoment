#!/usr/bin/python
# -*- coding: utf8 -*-

import os, subprocess
from git import Repo, Git
import logging
from optparse import OptionParser

logging.basicConfig()
_logger = logging.getLogger('CHECK_BRANCH')
_logger.setLevel(logging.DEBUG)

def check_branch():

    usage = "Revisa los Branch del Repositorio Conforme GitFlow: %prog [options]"
    parser = OptionParser(usage)

    parser.add_option("-H", "--git_url", dest="git_url", help="Git URL")
    (options, args) = parser.parse_args()

    if not options.git_url:
        parser.error('Parametro git_url no especificado')

    max_branche = 15
    all_branches = []
    branches_innecesarios = []

    _logger.info("=================================")
    _logger.info("         VALIDAR BRANCH          ")
    _logger.info("=================================")
    _logger.info("REPO")
    _logger.info("====")
    _logger.info(str(options.git_url))
    _logger.info("=================================")
    _logger.info("TODOS LOS BRANCH")
    _logger.info("====")

    cmd = 'git ls-remote -h ' + str(options.git_url)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    output_branches = [ x.split('\t')[-1] for x in output.split('\n') ]

    # get name repo
    for i in output_branches:
        name_branch = i.split('refs/heads/')[-1]   # ejemplo 'refs/heads/feature/error_list_branch'
        if len(name_branch) > 1:
            _logger.info(name_branch.lstrip())
            all_branches.append(name_branch.lstrip())

    _logger.info("=================================")
    _logger.info("BRANCH INNECESARIO")
    _logger.info("====")
    for name in all_branches:
        if ('HEAD' in name) or ('develop' in name) or ('release' in name) or ('maste' in name):
            pass
        else:
            _logger.info(name)
            branches_innecesarios.append(name)
    _logger.info("=================================")
    _logger.info(" RESULTADO VALIDAR BRANCH:")
    _logger.info("====")
    _logger.info('Branches innecesarios: ' + str(len(branches_innecesarios)))
    _logger.info('Limite branches innecesarios: ' + str(max_branche))
    if len(branches_innecesarios) >= max_branche:
        _logger.info('Ha superado el numero maximo de branch')
        _logger.info("=================================")
        raise Exception('Ha superado el numero maximo de branch')
    else:
        _logger.info('Ha cumplido con el lineamiento de limpieza de brachs')
        _logger.info("=================================")

if __name__ == '__main__':
    check_branch()
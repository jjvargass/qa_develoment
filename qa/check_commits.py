#!/usr/bin/python
# -*- coding: utf8 -*-

import os
from git import Repo
import logging
import datetime
import calendar

logging.basicConfig()
_logger = logging.getLogger('CHECK_COMMITS')
_logger.setLevel(logging.DEBUG)

max_commits_no_lineamiento = 30
date  = datetime.datetime.now()
fecha_inicio = date.replace(day = 1)
fecha_fin = date.replace(day = calendar.monthrange(date.year, date.month)[1])

# formato
form_fecha_inicio = fecha_inicio.strftime("%Y-%m-%d")
form_fecha_fin = fecha_fin.strftime("%Y-%m-%d")

# filtros
# --after=2020-02-11 00:00
after = '--after=' + str(form_fecha_inicio) +' 00:00'
# --before=2020-02-12 23:59
before = '--before=' + str(form_fecha_fin) + ' 23:59'

path = os.getcwd()
repo = Repo(path)

_logger.info("=================================")
_logger.info("        VALIDAR COMMITS          ")
_logger.info("=================================")
_logger.info("INTERVALO DE {} HASTA {}".format(form_fecha_inicio, form_fecha_fin))
_logger.info("BRANCH DE VALIDACIÓN: {} ".format(repo.active_branch.name))


commits_list = repo.git.log('--oneline', after, before, '--format=%B').split('\n')
#commits_list = repo.git.log('--oneline', '--after=2020-02-17 00:00', '--before=2020-02-17 23:59', '--format=%B').split('\n')

_logger.info("=================================")
_logger.info("COMMITS SIN LINEAMIENTO")
_logger.info("====")

# limpiar lista
while("" in commits_list):
    commits_list.remove("")

total_commits = len(commits_list)
commits_sin_lineamiento = []

for i in commits_list:
    comentrario = i.split(':')
    if (len(comentrario) > 1) and ( ('feat' in comentrario[0]) or ('fix' in comentrario[0]) or ('docs' in comentrario[0]) or ('test' in comentrario[0]) or ('refactor' in comentrario[0]) or ('devops' in comentrario[0]) or ('management' in comentrario[0]) ):
        pass
    elif ( ('Merge' in comentrario[0]) or ('See' in comentrario[0]) ):
        pass
    else:
        _logger.info(i)
        commits_sin_lineamiento.append(comentrario[0])

_logger.info("=================================")
_logger.info(" RESULTADO VALIDAR COMMITS:")
_logger.info("====")
_logger.info('Commits sin lineamiento: ' + str(len(commits_sin_lineamiento)))
_logger.info('Limite de commits sin lineamiento: ' + str(max_commits_no_lineamiento))
if len(commits_sin_lineamiento) >= max_commits_no_lineamiento:
    _logger.error("Ha Supperado el Limite de Commits Sin lineamiento")
    _logger.error("De {} Commits, {} No Cumplen con Lineamientos".format(total_commits, len(commits_sin_lineamiento) ))
    raise Exception('Ha Supperado el Limite de Commits Sin lineamiento')
else:
    _logger.info('Ha Cumplido con el Lineamiento de Definición de Commits')
    _logger.info("=================================")
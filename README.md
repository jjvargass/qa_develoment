# qa_develoment

Este repositorio tiene como propósito consolidar una serie de script que validen buenas prácticas en el Sistema Control de Versionamiento Git para ser implementado en un pipeline y reducir la deuda técnica.

### Script check_readme.py
Este script valida que el archivo README  contenga los siguientes capítulos:
- Especificaciones Técnicas
- Tecnologías Implementadas y Versiones
- Variables de Entorno
- Ejecución del Proyecto
- Estado CI
- Licencia

### Script check_commits.py
Este script valida que los commits deban contener un tag previos para proporcionar información valiosa y mantenibilidad al código.

**feat**: Describe si trabajaste en un nuevo feature.

**fix**: Describe si solucionaste un bug.

**docs**: Dice si hiciste algún cambio en la documentación.

**test**: Indica si añadiste un test

**refactor**: Nos muestra que se ejecutó algún refactor en el código.

**devops**: En este se engloban las tareas de DevOps ya sea, Monitoreo, Automatización, etc.

**management**: En esta categoría se agrupan todas las tareas de merge de los commits en las ramas, creación de ramas hotfix, release, etc. Este tag es para el uso exclusivo de las personas que tienen el rol de Master/Maintainer del proyecto.

Como Comentar los commits:
```bash
git commit -m "devops: ajustes formato ...."
git commit -m "fix: se realiza ....."
```
De esta forma se aporta una mejor organización a todo el control de cambios e intuitivo.

### Script check_branch.py

Este script valida la limpieza y el nombramiento de branch que nos aconseja la metodologia [gitflow](https://danielkummer.github.io/git-flow-cheatsheet/)


## Especificaciones Técnicas

### Tecnologías Implementadas y Versiones
* [Docker](https://www.docker.com/)
* [python 2.7](https://www.python.org/download/releases/2.7/)
* [GitPython](https://gitpython.readthedocs.io/en/stable/)

### Variables de Entorno
```shell
# Integración Continua
DOCKER_USERNAME: Usuario Docker Hup
DOCKER_PASSWORD: Password Docker Hup
TELEGRAM_TOKEN: Token del Bot de Telegran
TELEGRAM_TO: Grupo o conversación Id donde el Bot Reportará
```

### Instalación
```shell
# Opción 1
git clone https://github.com/jjvargass/qa_develoment.git
```

### Ejecución desde archivos fuentes dentro de un en Repositorio
```bash
kind: pipeline
name: qa_devops

steps:
- name: check_readme
  image: python:2.7
  commands:
  - python qa/check_readme.py
  when:
    branch:
    - dev
    - test
    - master

- name: check_branch
  image: python:2.7
  commands:
  - pip install gitpython
  - python qa/check_branch.py -H ${DRONE_GIT_HTTP_URL}
  when:
    branch:
    - dev
    - test
    - master

- name: check_commits
  image: python:2.7
  commands:
  - pip install gitpython
  - python qa/check_commits.py
  when:
    branch:
    - dev
    - test
    - master
```

### Ejecución desde Imagen Docker Consolidada
```shell
kind: pipeline
name: qa_devops

steps:
- name: check_readme
  image: jjvargass/qa_develoment:0.1
  commands:
  - python /app/check_readme.py
  when:
    branch:
    - dev
    - test
    - master

- name: check_branch
  image: jjvargass/qa_develoment:0.1
  commands:
  - python /app/check_branch.py -H ${DRONE_GIT_HTTP_URL}
  when:
    branch:
    - dev
    - test
    - master

- name: check_commits
  image: jjvargass/qa_develoment:0.1
  commands:
  - python /app/check_commits.py
  when:
    branch:
    - dev
    - test
    - master
```

## Licencia

This file is part of qa_develoment.

qa_develoment is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Foobar is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Foobar. If not, see https://www.gnu.org/licenses/.

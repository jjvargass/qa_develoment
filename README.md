# qa_develoment

Este repositorio tiene como propósito almacenar una serie de script que validen buenas prácticas en el Sistema Control de Versionamiento Git para ser implementado en un pipeline.

## Especificaciones Técnicas

### Tecnologías Implementadas y Versiones
* [Docker](https://www.docker.com/)
* [python 2.7](https://www.python.org/download/releases/2.7/)
* [GitPython](https://gitpython.readthedocs.io/en/stable/)

### Variables de Entorno
```shell
# En Pipeline
AWS_ACCESS_KEY_ID: llave de acceso ID Usuario AWS
AWS_SECRET_ACCESS_KEY: Secreto de Usuario AWS
REGISTRY_URI: URI repositorio Registry con account ID
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
  - python qa/check_branch.py
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
  - python /app/check_branch.py
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

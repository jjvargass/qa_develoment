#!/usr/bin/python
# -*- coding: utf8 -*-

import logging


logging.basicConfig(level=logging.CRITICAL)
_logger = logging.getLogger('CHECK_README')
_logger.setLevel(logging.DEBUG)

def check_readme():
    words = ['Especificaciones Técnicas',
                'Requerimientos de Software',
                'Tecnologías Implementadas y Versiones',
                'Ejecución del Proyecto',
            'Licencia'
            ]
    control = 0.0
    words_encontradas = []
    total_encontradas = 0.0
    control = len(words)/2.0

    _logger.info("=================================")
    _logger.info("        VALIDAR README           ")
    _logger.info("=================================")

    try:
        with open('README.md') as f:
            all_line = f.readlines()
            _logger.info("DEFINICIONES ENCONTRADAS:")
            _logger.info("====")
        for line in all_line:
            if  words[0] in line:
                _logger.info(words[0])
                total_encontradas +=1
                words_encontradas.append(words[0])
            if  words[1] in line:
                _logger.info(words[1])
                total_encontradas +=1
                words_encontradas.append(words[1])
            if  words[2] in line:
                _logger.info(words[2])
                total_encontradas +=1
                words_encontradas.append(words[2])
            if  words[3] in line:
                _logger.info(words[3])
                total_encontradas +=1
                words_encontradas.append(words[3])
            if  words[4] in line:
                _logger.info(words[4])
                total_encontradas +=1
                words_encontradas.append(words[4])

        # Validar Definiciones
        if (len(words_encontradas) == len(words)):
            _logger.info("=================================")
            _logger.info("Se Encontraron Todas las Definiciones en el README")
        elif (len(words_encontradas) == 0):
            _logger.info("=================================")
            _logger.info("No Se Encontró Ninguna Definiciones en el README")
        else:
            _logger.info("=================================")
            _logger.info("DEFINICIONES NO ENCONTRADAS:")
            _logger.info("====")
            words_no_encontradas =  list(set(words).difference(words_encontradas))
            for pp in words_no_encontradas:
                _logger.info(pp)

        # Resultado del Check
        _logger.info("=================================")
        _logger.info("RESULTADO VALIDAR README:")
        _logger.info("====")
        if (total_encontradas > control):
            _logger.info("Cumple con los lineamientos")
            _logger.info("=================================")

        else:
            _logger.error("No Cumple con los Lineamientos")
            raise Exception('No Cumple con los Lineamientos')

    except IOError:
            _logger.error("=================================")
            _logger.error("No Existe Arvhivo README.md - No Cumple con los Lineamientos")
            raise Exception('No Existe Arvhivo README.md - No Cumple con los Lineamientos')

if __name__ == '__main__':
    check_readme()
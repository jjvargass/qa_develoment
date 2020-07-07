#!/usr/bin/python
# -*- coding: utf8 -*-

import logging


logging.basicConfig(level=logging.CRITICAL)
_logger = logging.getLogger('CHECK_README')
_logger.setLevel(logging.DEBUG)

def check_words_in_line(line, words, contador, words_encontradas):
    new_words = words[:]
    for i in words:
        if i in line:
            _logger.info(i)
            contador +=1
            words_encontradas.append(i)
            new_words.remove(i)
    return contador, words_encontradas, new_words

def check_readme():
    words = ['Especificaciones Técnicas',
             'Tecnologías Implementadas y Versiones',
             'Variables de Entorno',
             'Ejecución del Proyecto',
             'Estado CI',
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
            total_encontradas, words_encontradas, words  = check_words_in_line(line, words, total_encontradas, words_encontradas)

        # Validar Definiciones
        if (len(words) == 0):
            _logger.info("=================================")
            _logger.info("Se Encontraron Todas las Definiciones en el README")
        elif (len(words_encontradas) == 0):
            _logger.info("=================================")
            _logger.info("No Se Encontró Ninguna Definiciones en el README")
        else:
            _logger.info("=================================")
            _logger.info("DEFINICIONES NO ENCONTRADAS:")
            _logger.info("====")
            for pp in words:
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
            _logger.info("No Existe Arvhivo README.md - No Cumple con los Lineamientos")
            _logger.info("=================================")
            raise Exception('No Existe Arvhivo README.md - No Cumple con los Lineamientos')

if __name__ == '__main__':
    check_readme()
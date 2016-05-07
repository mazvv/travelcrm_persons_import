#-*-coding:utf-8-*-

from pyramid.config import Configurator


def includeme(config):
    config.add_translation_dirs('travelcrm_persons_import:locale')
    config.scan()

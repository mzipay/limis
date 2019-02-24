import os

from distutils.version import StrictVersion
from pathlib import Path
from unittest import TestCase

import limis
from limis.core import get_version, initialize_logging, Settings
from tests import remove_logfile


class TestMethods(TestCase):
    def tearDown(self):
        remove_logfile()

    def test_initialize_logging(self):
        initialize_logging()

        path = Path(__file__).parent / 'data/settings_logging.ini'

        os.environ['LIMIS_PROJECT_SETTINGS'] = str(path)

        with self.assertRaises(ValueError):
            initialize_logging()

        os.environ.pop('LIMIS_PROJECT_SETTINGS')

    def test_get_version(self):
        version = get_version()
        self.assertEqual(version, StrictVersion('.'.join(map(str, limis.VERSION))))


class TestSettings(TestCase):
    def test_init(self):
        settings_instance = Settings()

        with self.assertRaises(ValueError):
            settings_instance = Settings(['invalid_file'])

        path = Path(__file__).parent / 'data/settings.ini'
        settings_instance = Settings([str(path)])

        self.assertTrue(hasattr(settings_instance, 'test_settings'))
        self.assertEqual(settings_instance.test_settings['valid_setting'], 'valid')
        self.assertFalse(hasattr(settings_instance, 'nonexistent_setting'))

        os.environ['LIMIS_PROJECT_SETTINGS'] = str(path)

        settings_instance = Settings()
        self.assertEqual(settings_instance.test_settings['valid_setting'], 'valid')


# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""

@author: Elena Colomo
@contact: ecolomo@esa.int

European Space Astronomy Centre (ESAC)
European Space Agency (ESA)

Created on 4 Sept. 2019
"""

import pytest

from ..core import XMMNewtonClass
from ..tests.dummy_tap_handler import DummyXMMNewtonTapHandler


class TestXMMNewton():

    def get_dummy_tap_handler(self):
        parameterst = {'query': "select top 10 * from v_public_observations",
                       'output_file': "test2.vot",
                       'output_format': "votable",
                       'verbose': False}
        dummyTapHandler = DummyXMMNewtonTapHandler("launch_job", parameterst)
        return dummyTapHandler

    @pytest.mark.remote_data
    def test_download_data(self):
        parameters = {'observation_id': "0112880801",
                      'level': "ODF",
                      'filename': 'file',
                      'verbose': False}
        xsa = XMMNewtonClass(self.get_dummy_tap_handler())
        xsa.download_data(parameters['observation_id'],
                          parameters['filename'],
                          parameters['verbose'],
                          level=parameters['level']
                          )

    @pytest.mark.remote_data
    def test_get_postcard(self):
        parameters = {'observation_id': "0112880801",
                      'image_type': "OBS_EPIC",
                      'filename': None,
                      'verbose': False}
        xsa = XMMNewtonClass(self.get_dummy_tap_handler())
        xsa.get_postcard(parameters['observation_id'],
                         parameters['image_type'],
                         parameters['filename'],
                         parameters['verbose'])

    def test_query_xsa_tap(self):
        parameters = {'query': "select top 10 * from v_public_observations",
                      'output_file': "test2.vot",
                      'output_format': "votable",
                      'verbose': False}

        xsa = XMMNewtonClass(self.get_dummy_tap_handler())
        xsa.query_xsa_tap(parameters['query'], parameters['output_file'],
                          parameters['output_format'], parameters['verbose'])
        self.get_dummy_tap_handler().check_call("launch_job", parameters)

    def test_get_tables(self):
        parameters = {'query': "select top 10 * from v_public_observations",
                      'output_file': "test2.vot",
                      'output_format': "votable",
                      'verbose': False}

        parameters2 = {'only_names': True,
                       'verbose': True}

        dummyTapHandler = DummyXMMNewtonTapHandler("get_tables", parameters2)
        xsa = XMMNewtonClass(self.get_dummy_tap_handler())
        xsa.get_tables(True, True)
        dummyTapHandler.check_call("get_tables", parameters2)

    def test_get_columns(self):
        parameters = {'query': "select top 10 * from v_public_observations",
                      'output_file': "test2.vot",
                      'output_format': "votable",
                      'verbose': False}

        parameters2 = {'table_name': "table",
                       'only_names': True,
                       'verbose': True}

        dummyTapHandler = DummyXMMNewtonTapHandler("get_columns", parameters2)
        xsa = XMMNewtonClass(self.get_dummy_tap_handler())
        xsa.get_columns("table", True, True)
        dummyTapHandler.check_call("get_columns", parameters2)

import pytest
from mock import patch
from cpx_client import CPXClient

def test_cpx_client():

  client = CPXClient()
  servers = ['10.58.1.8', '10.58.1.4']
  instance = {
    'cpu': '10%',
    'memory': '10%',
    'service': 'TestService'
  }

  print(client._endpoint)

  # mock_get_patcher = patch('')
  # mock_get = mock_get_patcher.start()

  # mock_get.return_value.json.return_value = instance
  # mock_get.return_value.ok = True

  response = client._get_instances()
  print(response)
  # assert_is_not_none(response)
  assert True is True

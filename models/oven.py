from typing import Dict, List

class Oven:
    """ """

    def __init__(self):
        self._endpoint = "http://localhost:8080"
        self.refresh()

    def refresh(self):
        self.instances = self._get_instances()
        self.services = self._get_services()
        self.instances_by_service = self._get_instances_by_service()

    def _get_instance(self, ip: str) -> Dict[str, str]:
        return instance


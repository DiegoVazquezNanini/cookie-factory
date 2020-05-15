import json
import requests
from typing import Dict, List


class CPXClient:
    """Cloud Provider X Api Client"""

    def __init__(self):
        self._endpoint = "http://localhost:8080"
        self.refresh()

    def refresh(self):
        self.instances = self._get_instances()
        self.services = self._get_services()
        self.instances_by_service = self._get_instances_by_service()

    def _get_instances_by_service(self) -> Dict[str, List[Dict[str, str]]]:
        services_by_type = {}
        for service_type in self.services:
            services_by_type[service_type] = self._get_instances_by(service_type)
        return services_by_type

    def _get_instances(self) -> Dict[str, str]:
        instances = {}
        response = requests.get(f"{self._endpoint}/servers")
        instance_ip = response.json()
        for ip in instance_ip:
            instances[ip] = self._get_instance(ip)
        return instances

    def _get_instance(self, ip: str) -> Dict[str, str]:
        response = requests.get(f"{self._endpoint}/{ip}")
        instance = response.json()
        instance["ip"] = ip
        instance["status"] = self._get_status(instance)
        return instance

    def _get_instances_by(self, service: str) -> List[Dict[str, str]]:
        return [
            self.instances[i]
            for i in self.instances.keys()
            if self.instances[i]["service"] == service
        ]

    def _get_services(self) -> List[str]:
        return list(set(self.instances[i]["service"] for i in self.instances.keys()))

    def _get_status(self, service: Dict[str, str]) -> str:
        return (
            "Healthy"
            if int(service["cpu"][:-1]) > 75 or int(service["memory"][:-1]) > 75
            else "Unhealthy"
        )

    def healthy_by(self, service: str) -> int:
        healthy = 0
        for service in self.instances_by_service[service]:
            if service["status"] == "Healthy":
                healthy += 1
        return healthy

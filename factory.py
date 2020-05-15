#!/usr/bin/env python3
import argparse
import time
from typing import Dict, List, Tuple
from cpx_client import CPXClient


def main(client: CPXClient, args: argparse.Namespace) -> None:
    """Jarvis Main"""
    if args.cmd == "instances":
        instances_cmd(client, args)
    elif args.cmd == "stats":
        stats_cmd(client, args)
    elif args.cmd == "alert":
        alert_cmd(client, args)
    else:
        print("Try running jarvis.py -h")


def instances_cmd(client: CPXClient, args: argparse.Namespace):

    services = [args.service] if args.service else client.services

    header = ["IP", "Service", "Status", "CPU", "Memory"]
    print("\t\t".join(header))

    for service in services:
        for instance in client.instances_by_service[service]:
            instance_info = [
                instance["ip"],
                instance["service"],
                instance["status"],
                instance["cpu"],
                instance["memory"],
            ]
            line = "\t".join(instance_info)
            print(line)


def stats_cmd(client: CPXClient, args: argparse.Namespace):

    services = [args.service] if args.service else client.services
    while True:
        for service in services:
            if args.avg:
                cpu, memory = avg_cpu_memory_by(client, service)
                print(f"{service}:\t avg_cpu: {cpu}\t avg_memory: {memory}")
            else:
                header = ["IP", "CPU", "Memory"]
                print("\t\t".join(header))

                for instance in client.instances_by_service[service]:
                    instance_info = [
                        instance["ip"],
                        instance["cpu"],
                        instance["memory"],
                    ]
                    line = "\t".join(instance_info)
                    print(line)
        if args.watch:
            time.sleep(args.watch)
            client.refresh()
        else:
            break


def alert_cmd(client: CPXClient, args: argparse.Namespace):
    nominal = True
    for service in client.services:
        healthy_count = client.healthy_by(service)
        if healthy_count < args.threshold:
            nominal = False
            print(
                f"Fewer than {args.threshold} healthy instances running for service {service}"
            )

    if nominal:
        print("All system nominal! Go grab a cup of tea")


def avg_cpu_memory_by(client: CPXClient, service: str) -> Tuple[str, str]:
    cpu, memory = [], []
    for service in client.instances_by_service[service]:
        cpu.append(int(service["cpu"][:-1]))
        memory.append(int(service["memory"][:-1]))
    return (
        "%.2f" % round(sum(cpu) / len(cpu), 2),
        "%.2f" % round(sum(memory) / len(memory), 2),
    )


if __name__ == "__main__":

    client = CPXClient()

    parser = argparse.ArgumentParser(description="")
    subparsers = parser.add_subparsers(
        title="commands",
        description="Try COMMAND -h for help on that command",
    )

    instances_parser = subparsers.add_parser(
        "instances", help="Print information about instances"
    )
    instances_parser.add_argument("-s", "--service", choices=client.services)
    instances_parser.set_defaults(cmd="instances")

    stats_parser = subparsers.add_parser("stats", help="Print instances or services stats")
    stats_parser.add_argument(
        "-s", "--service", choices=client.services, dest="service"
    )
    stats_parser.add_argument(
        "-w", "--watch", type=int, dest="watch", help="Continues monitoring"
    )
    stats_parser.add_argument("--avg", dest="avg", action="store_true")
    stats_parser.set_defaults(cmd="stats")

    alert_parser = subparsers.add_parser(
        "alert", help="Alert about services in a critical state based on your threshold"
    )
    alert_parser.add_argument(
        "-t",
        "--threshold",
        type=int,
        dest="threshold",
        help="Instances threshold to alert on a service",
        default=2,
    )
    alert_parser.set_defaults(cmd="alert")

    args = parser.parse_args()
    if hasattr(args, "cmd"):
        main(client, args)
    else:
        parser.print_help()

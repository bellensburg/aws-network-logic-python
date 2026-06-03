
# routing.py

import ipaddress

def match_route(routes, destination_ip):
    """
    Simulates AWS longest prefix match behavior
    """
    best_match = None
    best_prefix = -1

    for route in routes:
        network = ipaddress.ip_network(route.destination)

        if ipaddress.ip_address(destination_ip) in network:
            if network.prefixlen > best_prefix:
                best_match = route
                best_prefix = network.prefixlen

    return best_match

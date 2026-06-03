
# reachability.py

from routing import match_route

def can_reach(source_subnet, dest_ip, route_tables):
    """
    Determines if traffic can leave source subnet
    """

    rt = route_tables.get(source_subnet.route_table_id)

    route = match_route(rt.routes, dest_ip)

    if not route:
        return False, "No route found"

    if route.target == "local":
        return True, "Local VPC routing"

    if route.target == "tgw":
        return True, "Forwarded to Transit Gateway"

    if route.target == "igw":
        return True, "Internet Gateway route"

    return False, f"Unsupported target {route.target}"

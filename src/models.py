
# models.py

class Subnet:
    def __init__(self, id, cidr, route_table_id, vpc_id):
        self.id = id
        self.cidr = cidr
        self.route_table_id = route_table_id
        self.vpc_id = vpc_id


class Route:
    def __init__(self, destination, target):
        self.destination = destination
        self.target = target  # igw, nat, tgw, local


class RouteTable:
    def __init__(self, id, routes):
        self.id = id
        self.routes = routes


class TransitGatewayAttachment:
    def __init__(self, vpc_id, tgw_id):
        self.vpc_id = vpc_id
        self.tgw_id = tgw_id
``

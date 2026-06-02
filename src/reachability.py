import json
from find_by_id import find_by
from tgw_logic import same_tgw

def can_reach(data, subnet_a, subnet_b):
    """
    Determine if two subnets can reach each other.
    Rules:
    - Same VPC = reachable
    - Different VPCs but share same TGW = reachable
    """
    sub_a = find_by(data["subnets"], "id", subnet_a)
    sub_b = find_by(data["subnets"], "id", subnet_b)

    if not sub_a or not sub_b:
        return False

    # Same VPC
    if sub_a["vpc_id"] == sub_b["vpc_id"]:
        return True

    # Same TGW
    if same_tgw(data["tgw_attachments"], sub_a["vpc_id"], sub_b["vpc_id"]):
        return True

    return False


if __name__ == "__main__":
    with open("data/sample_topology.json") as f:
        topo = json.load(f)

    print(can_reach(topo, "subnet-a1", "subnet-b1"))

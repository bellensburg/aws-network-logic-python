# tgw.py

def evaluate_tgw_connectivity(source_vpc, dest_vpc, attachments):
    """
    Simulates TGW attachment connectivity
    """

    src_attached = any(a.vpc_id == source_vpc for a in attachments)
    dst_attached = any(a.vpc_id == dest_vpc for a in attachments)

    if not src_attached:
        return False, "Source VPC not attached to TGW"

    if not dst_attached:
        return False, "Destination VPC not attached to TGW"

    return True, "Both VPCs connected via TGW"

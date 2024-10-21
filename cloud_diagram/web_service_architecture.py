from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.network import ElasticLoadBalancing
from diagrams.aws.database import RDS

with Diagram("Cloud Web Service Architecture", show=False):
    with Cluster("VPC"):
        lb = ElasticLoadBalancing("lb")
        with Cluster("Services"):
            svc_group = [EC2("web1"),
                         EC2("web2"),
                         EC2("web3")]

        with Cluster("DB Cluster"):
            rds_master = RDS("master")
            rds_replica = [RDS("replica1"),
                           RDS("replica2")]

        lb >> svc_group
        svc_group >> rds_master
        rds_master - Edge(color="brown", style="dashed") - rds_replica
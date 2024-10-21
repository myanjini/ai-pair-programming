from diagrams import Diagram, Cluster
from diagrams.aws.network import VPC, InternetGateway, PublicSubnet, PrivateSubnet, RouteTable

with Diagram("VPC Diagram", show=False):
    with Cluster("VPC"):
        vpc = VPC("MyVPC\nCIDR: 10.0.0.0/16")
        
        igw = InternetGateway("MyIGW")
        
        with Cluster("Public Subnet"):
            public_subnet = PublicSubnet("MyPublicSubnetA\nCIDR: 10.0.10.0/24")
            public_rt = RouteTable("MyPublicRT\nRoute: 0.0.0.0/0 -> IGW")
        
        with Cluster("Private Subnet"):
            private_subnet = PrivateSubnet("MyPrivateSubnetA\nCIDR: 10.0.20.0/24")
            private_rt = RouteTable("MyPrivateRT")
        
        vpc - igw
        vpc - public_subnet
        vpc - private_subnet
        public_subnet - public_rt
        private_subnet - private_rt
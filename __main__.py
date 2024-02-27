import pulumi
from pulumi import Output
from pulumi_cloud import Server

size = "t2.micro"

user_data = """
#!/bin/bash
echo "Hello, World!" > index.html
git clone https://github.com/TeamUltroid/Ultroid /ok
cd /ok
pip3 install -r requirements.txt
nohup python3 -m pyUltroid 80 &
"""

server = Server(
    'web-server-www',
    opts=pulumi.ResourceOptions(depends_on=[]),
    size=size,
    user_data=user_data,
)

pulumi.export("public_ip", server.public_ip)
pulumi.export("public_dns", server.public_dns)

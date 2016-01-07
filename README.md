# aliyun-whitelist-service
阿里云的IP白名单服务

$pip install -r requirements.txt

$python whitelist.py

在settings.py中配置阿里云 SDK的账号，以及ECS服务器所在区域。

IP白名单服务：
http://127.0.0.1:5001/list

返回值说明：
得到白名单列表，白名单包含：

1.阿里云账号下面的所有主机的内网IP，外网IP

2.配置的IP列表，以及以 white_ip_prefix（如值设置为192.168)开头的前缀的IP地址


注意事项：
当调用白名单服务的机器的IP地址在白名单内时，/list才会返回正确的IP列表，否则errorcode会返回-1。

centos上需要安装libxslt-devel:
$sudo yum install libxslt-devel

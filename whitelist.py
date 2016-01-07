from flask import Flask, request
import flask

app = Flask(__name__, static_url_path='')

from settings import appKey,appSecret,zone,white_list,white_ip_prefix

@app.route('/')
def root():
	return "aliyun whitelist service";


def allow(ip):
	return ip in white_list or (white_ip_prefix and ip.startswith(white_ip_prefix))

@app.route('/list')
def list():
	#print(request.remote_addr)
	if not allow(request.remote_addr):
		return flask.jsonify(errorcode='-1', errormessage='', whitelist={})
	list_str = white_list + ' ' +  aliyun_ecs_list()
	return flask.jsonify(errorcode='0', errormessage='', whitelist=list_str.split())

def aliyun_ecs_list():
	from aliyunsdkcore import client
	from aliyunsdkcore import request
	from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
	clt = client.AcsClient(appKey,appSecret, zone)
	request = DescribeInstancesRequest.DescribeInstancesRequest()
	result = clt.do_action(request)

	from pyquery import PyQuery as pq
	d = pq(result,parser='xml')
	ip_list = d('PublicIpAddress').text()
	internal_ip_list = d('InnerIpAddress').text()
	return ip_list + ' ' + internal_ip_list

if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0",port=5001)

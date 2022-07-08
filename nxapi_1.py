import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

host = '192.168.47.102'
username = 'admin'
password = 'admin'

postdata = '''{
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show int mgmt 0",
    "output_format": "json"
  }
}'''

response = requests.post(f'https://{host}/ins',
                        auth=(username, password),
                        data=postdata,
                        headers={'Content-Type': 'application/json'},
                        verify=False)

if response.status_code == 200:
    print(response.json()['ins_api']['outputs']['output']['body'])
    #mgmt0 = response.json()['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']
    #print(mgmt0['eth_ip_addr'])

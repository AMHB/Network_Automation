import requests
import urllib3
import json

def nxapi_command(command_type, commands, rollback='stop-on-error'):

    command_type_valid_values = ['cli_show', 'cli_show_array', 'cli_show_ascii', 'cli_conf', 'bash']
    rollback_valid_values = ['stop-on-error', 'continue-on-error', 'rollback-on-error']

    if command_type not in command_type_valid_values:
        raise ValueError(f'Invalid command_type. Must be one of {command_type_valid_values}')

    if rollback not in rollback_valid_values:
        raise ValueError(f'Invalid rollback. Must be one of {rollback_valid_values}')


    request_body = {'ins_api': {'version': '1.0',
                                'type': command_type,
                                'chunk': '0',
                                'sid': '1',
                                'input': ' ;'.join(commands),
                                'output_format': 'json'}}

    if command_type == 'cli_conf':
        request_body['ins_api']['rollback'] = rollback

    return json.dumps(request_body, indent=4)


def nxapi_request(host, username, password, commands, command_type='cli_show_array', rollback='stop-on-error'):

    command_type_valid_values = ['cli_show', 'cli_show_array', 'cli_show_ascii', 'cli_conf',  'bash']

    if command_type not in command_type_valid_values:
        raise ValueError(f'Invalid command_type. Must be one of {command_type_valid_values}')

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    return requests.post(f'https://{host}/ins',
                        auth=(username, password),
                        data=nxapi_command(command_type, commands, rollback=rollback),
                        headers={'content-type': 'application/json'},
                        verify=False)


def nxapi_verify_response(response):

    output = response.json()['ins_api']['outputs']['output']

    if type(output) == list:
        if len(set([x['code'] for x in output])) == 1 and output[0]['code'] == '200':
            return True
    else:
        if output['code'] == '200':
            return True

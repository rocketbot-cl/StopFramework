__version__ = '1.0.0'
__author__ = 'Rocketbot'

import configparser
import json
import platform
import requests
import os
import traceback

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'StopFramework' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

from configurationObject import ConfigObject
from orchestator import OrchestatorCommon

global configFormObject
global path_ini_assetnoc_

module = GetParams('module')
try:
    if module == 'Login':
        server_ = GetParams("server_url")
        var_ = GetParams('var_')
        iframe = GetParams("iframe")
        iframe = eval(iframe) if iframe is not None else {}
        username = iframe.get("user", "")
        password = iframe.get("password", "")
        api_key = iframe.get("apikey", "")
        path = iframe.get("path_ini", GetParams("ruta_"))
        path_ini_assetnoc_ = path
        proxies = GetParams("proxies")

        if password and username:
            try:
                orchestrator_service = OrchestatorCommon(server=server_, user=username, password=password, ini_path=path, apikey=api_key)
                if server_ is None:
                        server_ = orchestrator_service.server
                token = orchestrator_service.get_authorization_token()
                headers = {'content-type': 'application/x-www-form-urlencoded','Authorization': 'Bearer {token}'.format(token=token)}
                res = requests.post(server_ + '/api/assets/list',
                                    headers=headers)
                configFormObject = ConfigObject(token, orchestrator_service.server, orchestrator_service.user, orchestrator_service.password, api_key, None)
                conx = True
                SetVar(var_, conx) #type: ignore

            except:
                if res.status_code != 200:
                    exc = res.json()['message'] if res.json()['message'] else "Password o E-mail incorrectos"
                    raise Exception(exc)
                raise Exception("Password o E-mail incorrectos")

        elif api_key:
                        
            orchestrator_service = OrchestatorCommon(server=server_, user=username, password=password, ini_path=path, apikey=api_key)
            if server_ is None:
                server_ = orchestrator_service.server
            token = orchestrator_service.get_authorization_token()
            headers = {'content-type': 'application/x-www-form-urlencoded','Authorization': 'Bearer {token}'.format(token=token)}
            res = requests.post(server_ + '/api/assets/list',
                                headers=headers)
            configFormObject = ConfigObject(token, orchestrator_service.server, orchestrator_service.user, orchestrator_service.password, api_key, None)
            print(res.status_code)
            print(res.text)
            if res.status_code != 200:
                
                exc = res.json()['message'] if res.json()['message'] else "El API Key es incorrecto"
                raise Exception(exc)
            else:
                conx = True
            SetVar(var_, conx)

        elif path:
            try:
                orchestrator_service = OrchestatorCommon(server=server_, user=username, password=password, ini_path=path, apikey=api_key)
                if server_ is None:
                    server_ = orchestrator_service.server
                token = orchestrator_service.get_authorization_token()
                headers = {'content-type': 'application/x-www-form-urlencoded','Authorization': 'Bearer {token}'.format(token=token)}
                res = requests.post(server_ + '/api/assets/list',
                                    headers=headers)
                configFormObject = ConfigObject(token, orchestrator_service.server, orchestrator_service.user, orchestrator_service.password, api_key, None)
                conx = True
                SetVar(var_, conx)
            except:
                if res.status_code != 200:
                    exc = res.json()['message'] if res.json()['message'] else "Password o E-mail incorrectos"
                    raise Exception(exc)
                raise Exception("Password o E-mail incorrectos")

    if module == "ShouldStop":
        var_ = GetParams('var_')
        process_instance = GetParams('process_instance')
        process_id = GetParams('process_id')


        if configFormObject is None:
            raise Exception("No se ha iniciado sesión en Orchestrator")

        token = configFormObject.token
        headers = {'content-type': 'application/x-www-form-urlencoded','Authorization': 'Bearer {token}'.format(token=token)}
        data = {
            "instance": process_instance,
            "process": process_id
        }
        res = requests.post(configFormObject.server_ + '/api/robots/getFrameworkStatus', data=data, headers=headers)
        
        try:
            result = res.json()
            if res.status_code != 200:
                raise Exception(result['message'])
            else:
                SetVar(var_, True if result['data']==1 else False)
        except:
            raise Exception("Error al obtener el estado del framework")

except Exception as e:
    traceback.print_exc()
    PrintException()
    raise e
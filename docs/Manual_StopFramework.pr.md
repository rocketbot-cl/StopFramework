# Rocketbot Stop Framework
  
Módulo para Rocketbot Stop Framework  

*Read this in other languages: [English](Manual_StopFramework.md), [Português](Manual_StopFramework.pr.md), [Español](Manual_StopFramework.es.md)*
  
![banner](imgs/Banner_StopFramework.png o jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Login NOC
  
Faça login no NOC usando uma das opções, arquivo noc.ini, API Key ou credenciais.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL Servidor|URL do servidor para se conectar|https://roc.myrb.io/|
|Selecione um método para se conectar ao orquestrador|Opções para fazer login no R.O.C, você pode usar credenciais de usuário, chave de API ou selecionar o arquivo noc.ini|API Key|
|Atribuir resultado à variável|Variável onde será armazenado o estado da conexão, retorna True se for bem sucedida ou False caso contrário|Variable|

### Deve parar?
  
Verifique se o framework deve parar
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do processo a verificar|Variável onde o id do processo a ser verificado se deve parar ou não deve ser inserido|J1H8K5DQ4XEW3M9R|
|Instância do processo|Variável onde a instância do processo deve ser inserida|a2f64d5d9988c|
|Atribuir resultado à variável|Variável onde True ou False será armazenado dependendo se deve parar ou não|Variable|

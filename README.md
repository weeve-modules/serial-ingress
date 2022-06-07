# Serial Ingress


|              |                                                                                     |
| ------------ |-------------------------------------------------------------------------------------|
| name         | Serial Ingress                                                                      |
| version      | v0.1.0                                                                              |
| docker image | [weevenetwork/serial-ingress](https://hub.docker.com/r/weevenetwork/serial-ingress) |
| tags         | Python, Flask, Docker, Weeve                                                        |
| authors      | Ghassen barbocuhi                                                                   |

***
## Table of Content
- [Serial Ingress](#serial-ingress)
  - [Table of Content](#table-of-content)
  - [Description](#description)
    - [Features](#features)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Directory Structure](#directory-structure)
    - [File Tree](#file-tree)
  - [As a module developer](#as-a-module-developer)
    - [Configuration](#configuration)
    - [Business Logic](#business-logic)
  - [Dependencies](#dependencies)
  - [Output/Egress](#outputegress)
- [VSCode Support for devcontainer](#vscode-support-for-devcontainer)

***

## Description

This module read data from serial of a host machine.

### Features
1. Open serial of a host machine 
2. Read received serial data
3. Progress received serial data in a data service

## Environment Variables

### Module Specific
The following module configurations can be provided in a data service designer section on weeve platform:

| Name                | Environment Variables | Type    | Description                |
|---------------------|-----------------------|---------|----------------------------|
| Serial Port         | PORT                  | string  | eg: /dev/ttyUSB0           |
| Serial Baud_Rate    | BAUD_RATE             | integer | The data baud rate         | ws`                |
| Number of data bits | DATA_BITS             | string  | Port number for tbe broker |
| Parity              | PARITY                | string  | Enable parity checking     |
| Stop bits           | STOP_BITS             | string  | Number of stop bits        |

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

### Set by the weeve Agent on the edge-node

| Environment Variables | type   | Description                            |
|-----------------------| ------ | -------------------------------------- |
| EGRESS_URL            | string | HTTP ReST endpoint for the next module |
| MODULE_NAME           | string | Name of the module                     |


## Dependencies
```
requests
python-dotenv
pyserial==3.3 
```
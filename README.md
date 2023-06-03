# DoS_attack

## About

This project provides a simulation of a Denial of Service (DoS) attack for educational purposes in information security classes. It demonstrates how such attacks can disrupt the availability of a target system by overwhelming its resources.

You can access the slides in the following [link](https://docs.google.com/presentation/d/1O_LsmGRh4DroH3Tq830xtmxml6-76d7YTPXxOUDyXX4/edit?usp=sharing).

## Installation

[Optional] Create a virtual environment to isolate project dependencies. Skip this step if you prefer to install the project dependencies globally.

```bash
python3 -m venv .venv
```

[Optional] Active the virtual environment, running:

```bash
source ./.venv/bin/activate
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

## Run project

Start the server by running the following command:

```bash
python3 server/main.py
```

Run the DoS attack by executing the following command:

```bash
python3 attack/main.py
```

## API Reference

### Get fibonacci

#### Request

```http
GET /fib/${number}
```

| Parameter | Type     | Description                                                             |
| :-------- | :------- | :---------------------------------------------------------------------- |
| `number`  | `number` | **Required**. The input number to calculate the Fibonacci sequence for. |

#### Response

| Property | Type     | Description                                                         |
| :------- | :------- | :------------------------------------------------------------------ |
| `number` | `number` | The input number for which Fibonacci sequence was calculated.       |
| `fib`    | `number` | The calculated Fibonacci sequence value.                            |
| `time`   | `number` | The time taken to calculate the Fibonacci sequence in milliseconds. |

## Hands-On

You should choose between the **Blue (defense)** or **Red (attack)** team and perform the specific activity according to your choice:

**Blue Team**

The objective is to defend the server against a DoS attack. To do so, implement improvements to prevent the attack.

**Red Team**

The objective is to attack the server by converting the DoS attack into a Distributed Denial of Service (DDoS) attack:

- Create an SSH botnet.
- Upon connecting to the target, [download the file](https://raw.githubusercontent.com/eoisaac/DoS_attack/main/attack/main.py) and execute it.

## Exercício Prático

Você deverá escolher entre o time **Azul(defesa)** ou **Vermelho(ataque)** e desenvolver a atividade específica de acordo com a escolha:

**Azul Team**

O objetivo é defender o servidor do ataque DoS, para isso implemente melhorias para prevenir o ataque.

**Vermelho Team**

O objetivo é atacar o servidor, para isso converta o DoS em um ataque DDoS:

- Crie uma simples botnet SSH
- Ao conectar ao alvo, faça [download do arquivo](https://raw.githubusercontent.com/eoisaac/DoS_attack/main/attack/main.py) e o execute.

## Author

[@eoisaac](https://www.github.com/eoisaac)

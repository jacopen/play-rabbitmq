# Play RabbitMQ

This repository contains notes to play the [RabbitMQ][1].

## Getting started

### Preparation

1. Setup docker
1. Boot RabbitMQ
```bash
$ docker run -d -p 5672:5672 rabbitmq:3
```
1. Install pika (pika is rabbitmq client for Python)
```bash
pip install pika
```

### [Hello World!][2]
1. move to helloworld directory.
1. Run the send program.
```bash
$ python send.py
```
1. Run the recive program.
```bash
$ python recive.py
```

### [Work Queues][3]
1. move to work-queue directory.
1. Boot worker.
```bash
shell-1 $ python worker.py
```
1. Boot worker on another shell.
```bash
shell-2 $ python worker.py
```
1. Send messages
```bash
$ python new_task.py one message.
$ python new_task.py two message..
$ python new_task.py three message...
$ python new_task.py fourth message....
$ python new_task.py fifth message.....
```

### [Publisher & Subscriber][4]

1. Move to directory
```bash
$ cd publish-subscribe
```
1. Boot subscriber and save log file
```bash
$ python recive_logs.py > rabbit.log
```
1. Boot second subscriber
```
$ python recive_logs.py
```
1. Emit logs
```bash
$ python emit_log.py
```

## Links
* [RabbitMQ][1]
* [Tutorial - HelloWorld][2]
* [Tutorial - Work Queues][3]
* [Tutorial - Publisher/Subscriber][4]

[1]: https://www.rabbitmq.com/
[2]: https://www.rabbitmq.com/tutorials/tutorial-one-python.html
[3]: https://www.rabbitmq.com/tutorials/tutorial-two-python.html
[4]: https://www.rabbitmq.com/tutorials/tutorial-three-python.html

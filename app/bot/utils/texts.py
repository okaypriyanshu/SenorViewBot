Last login: Thu Jul 11 14:06:37 on ttys000
senor@Mac ~ % ssh senor@65.20.77.250
senor@65.20.77.250's password: 
Welcome to Ubuntu 22.04.4 LTS (GNU/Linux 5.15.0-113-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Thu Jul 11 09:01:26 AM UTC 2024

  System load:  0.2                Processes:               156
  Usage of /:   41.6% of 22.88GB   Users logged in:         1
  Memory usage: 40%                IPv4 address for enp1s0: 65.20.77.250
  Swap usage:   6%

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

3 additional security updates can be applied with ESM Apps.
Learn more about enabling ESM Apps service at https://ubuntu.com/esm


Last login: Thu Jul 11 08:46:47 2024 from 223.228.226.215
senor@vultr:~$ cd SenorViewBot
senor@vultr:~/SenorViewBot$ ls
Dockerfile  README.md  docker-compose.yml  requirements.txt
LICENSE     app        redis
senor@vultr:~/SenorViewBot$ docker-compose restart
[+] Restarting 2/2
 ✔ Container support-redis  Started                                        1.0s 
 ✔ Container support-bot    Started                                        0.7s 
senor@vultr:~/SenorViewBot$ cd app/bot/utils
senor@vultr:~/SenorViewBot/app/bot/utils$ ls
__init__.py  create_forum_topic.py  exceptions.py  redis  texts.py
senor@vultr:~/SenorViewBot/app/bot/utils$ nano texts.py
senor@vultr:~/SenorViewBot/app/bot/utils$ docker-compose restart
[+] Restarting 2/2
 ✔ Container support-redis  Started                                        0.9s 
 ✔ Container support-bot    Started                                        0.8s 
senor@vultr:~/SenorViewBot/app/bot/utils$ nano texts.py
senor@vultr:~/SenorViewBot/app/bot/utils$ docker-compose restart
[+] Restarting 2/2
 ✔ Container support-redis  Started                                        0.6s 
 ✔ Container support-bot    Started                                       10.5s 
senor@vultr:~/SenorViewBot/app/bot/utils$ nano texts.py
senor@vultr:~/SenorViewBot/app/bot/utils$ docker-compose restart
[+] Restarting 2/2
 ✔ Container support-redis  Started                                        1.0s 
 ✔ Container support-bot    Started                                        0.8s 
senor@vultr:~/SenorViewBot/app/bot/utils$ nano texts.py
senor@vultr:~/SenorViewBot/app/bot/utils$ docker-compose restart
[+] Restarting 2/2
 ✔ Container support-bot    Started                                       10.5s 
 ✔ Container support-redis  Started                                        0.5s 
senor@vultr:~/SenorViewBot/app/bot/utils$ client_loop: send disconnect: Broken pipe
senor@Mac ~ % ssh senor@65.20.77.250
senor@65.20.77.250's password: 
Welcome to Ubuntu 22.04.4 LTS (GNU/Linux 5.15.0-113-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Thu Jul 11 10:01:09 AM UTC 2024

  System load:  0.0                Processes:               161
  Usage of /:   41.6% of 22.88GB   Users logged in:         1
  Memory usage: 54%                IPv4 address for enp1s0: 65.20.77.250
  Swap usage:   6%

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

3 additional security updates can be applied with ESM Apps.
Learn more about enabling ESM Apps service at https://ubuntu.com/esm


Last login: Thu Jul 11 09:01:27 2024 from 223.228.226.215
senor@vultr:~$ cd SenorViewBot app/bot/utils
-bash: cd: too many arguments
senor@vultr:~$ cd SenorViewBot/app/bot/utils
senor@vultr:~/SenorViewBot/app/bot/utils$ ls
__init__.py  create_forum_topic.py  exceptions.py  redis  texts.py
senor@vultr:~/SenorViewBot/app/bot/utils$ nano texts.py

  GNU nano 6.2                        texts.py                            M     
                    "<b>Status:</b>\n"
                    "- {state}\n"
                    "<b>Username:</b>\n"
                    "- {username}\n"
                    "<b>Blocked:</b>\n"
                    "- {is_banned}\n"
                    "<b>Registration date:</b>\n"
                    "- {created_at}"
                ),
                "message_not_sent": "<b>Message not sent!</b> An unexpected err>
                "message_sent_to_user": "<b>Message sent to user!</b>",
                "silent_mode_enabled": (
                    "<b>Silent mode activated!</b> Messages will not be deliver>
                ),
                "silent_mode_disabled": (
                    "<b>Silent mode deactivated!</b> The user will receive all >
                ),
            }
        }

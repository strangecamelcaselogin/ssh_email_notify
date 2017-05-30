### Simplest email notify script.

1. make dir, let it be '/opt/ssh_email_notify'
>    cd /opt
>    sudo mkdir ssh_email_notify

2. in /opt/ssh_email_notify 
    2.1 create ssh_email_notify.sh and give premmision to execute (chmod +x ssh_email_notify.sh)
>       sudo touch ssh_email_notify.sh
>       sudo chmod +x ssh_email_notify.sh

    2.2 edit ssh_email_notify.sh like:
>       #!/bin/bash
>       python3 /opt/ssh_email_notify/ssh_email_notify.py

    2.3 and put ssh_email_notify.py (this file) in '/opt/ssh_email_notify'

3. create and/or edit '/etc/ssh/sshrc' file like:
>       /opt/ssh_email_notify/ssh_email_notify.sh

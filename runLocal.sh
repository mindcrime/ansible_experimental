#!/bin/bash

rm ansible.log

ANSIBLE_CONFIG="ansible_local.cfg" time -p ansible-playbook $@
rm *.retry
rm *.*~
echo "finished at $(date)"

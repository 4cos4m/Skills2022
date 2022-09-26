#!/bin/sh

docker pull cturra/ntp

docker run --name=task_4            \
              --restart=always      \
              --detach              \
              --publish=145:145/udp \
              cturra/ntp

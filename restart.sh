#!/bin/bash

SUPERVISORD_PID_FILE=supervisord.pid
kill -HUP $(cat ${SUPERVISORD_PID_FILE})


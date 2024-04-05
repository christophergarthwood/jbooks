#Title:     Logger for Python frameworks.
#Objective: Invocation is intended as function calls within another program.
#Assumptions:
#           1. Should be stored in standardized location such as:
#                      /p/home/{user_name}/usr/PYTHONLIB
#           2. Developer invokes this library as per proper Python module calls.
#           3. Invocation of msg_emerg is sufficient to cease operations.
#Pre-Requisites:
#           1. Python v3.*
#           2. RedHat Linux
#Usage:
#       Ensure module is exposed to python environment, see test_msg.py.
#       import debug
#       debug.msg_info("This is a test.")
#
#TODO: Add defenses for missing input (null values).
#TODO: More robust documentation.
#
#Version History:
# ---------------------------------------------------------------------
# Version   Date      Modification                              Author
# ---------------------------------------------------------------------
# 1.0       Unknown   Inception                                 Radiance
# 1.1       20190714  Updates to msg_vars to handle more data   CWood
#                     data types and options.
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#LIBRARIES
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import logging
import time
import getpass
import traceback
import os
import sys

logging.EMERG = 60
## Constant defined to support `emergency` class log events.

logging.TRACE = 70
## Constant defined to support `trace`, deeper than debug, class log events

logging.addLevelName(logging.EMERG, "EMERG")
## Level added for `emergency` to logging structure.

logging.addLevelName(logging.TRACE, "TRACE")
## Level added for `trace` to logging structure.


## Emergency class log output, these are events that warrant direct inspection and could cause system failure.
#
#  @param (debug)  self
#  @param (string) message - Actual message to display in the log
#  @param (list)   args - Additional, variable number, arguments passed to the function.
#  @param (list)   kws - Additional, variable number, optional keywords passed to the function.
#
def emergencyLog(self, message, *args, **kws):
    self.log(logging.EMERG, message, *args, **kws)

## Trace class log output, these are events are highly detailed output to the level of variable inspection.
#
#  @param (debug)  self
#  @param (string) message - Actual message to display in the log
#  @param (list)   args - Additional, variable number, arguments passed to the function.
#  @param (list)   kws - Additional, variable number, optional keywords passed to the function.
#
def traceLog(self, message, *args, **kws):
    self.log(logging.TRACE, message, *args, **kws)


"""Adding new log level to logging module"""
logging.Logger.emergencyLog = emergencyLog
logging.Logger.traceLog = traceLog

"""Create logger and configure format of logger"""
logger = logging.getLogger("msg_logs")

#logging.Formatter.converter = time.gmttime
logging.Formatter.converter = time.localtime

ch = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('[%(asctime)s]%(levelname) 8s: %(message)s ',"%Y-%m-%d %H:%M:%S %Z")
ch.setFormatter(formatter)
logger.addHandler(ch)
logStatement = ''

## Debug statement, wrapper method to the logger's actual debug routine.
#
#  @param (string) logStatement - Actual message to display in the log
#
def msg_debug(logStatement):
    # Debug level msg
    logger.setLevel(logging.DEBUG)
    logger.debug(logStatement)


"""Info Logging Statement"""


def msg_info(logStatement):
    # Debug level msg
    logger.setLevel(logging.INFO)
    logger.info(logStatement)


"""Warning Logging Statement"""


def msg_warning(logStatement):
    # Debug level msg
    logger.setLevel(logging.WARN)
    logger.warning(logStatement)


"""Error Logging Statement"""


def msg_error(logStatement):
    # Debug level msg
    logger.setLevel(logging.ERROR)
    logger.error(logStatement)


"""Emergency Logging Statement"""


def msg_emerg(logStatement):
    # Debug level msg
    logger.setLevel(logging.EMERG)
    emergencyLog(logger, message=logStatement)


"""Vars Logging Statement"""
def msg_vars(logStatementArr):
    logger.setLevel(logging.DEBUG)
    logger.debug("===========================")
    count = 0
    if (type(logStatementArr) is int):
        logger.debug(str(logStatementArr));
    elif (type(logStatementArr) is float):
        logger.debug(str(logStatementArr));
    elif (type(logStatementArr) is str):
        logger.debug(str(logStatementArr));
    else:
        try: 
            for i in logStatementArr:
                logger.debug("[" + str(count) + "]" + str(i))
                count = count + 1
        except TypeError:
            logger.debug(str(logStatementArr))
    logger.debug("===========================")
        
"""Trace Logging Statement"""
def msg_trace(logStatementArr):
    traceLog(logger,message=traceback.format_stack())

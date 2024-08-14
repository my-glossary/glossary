include .env

ifeq (${ENVIRONMENT}, DEVELOPMENT)
	DISPLAY := DEV
else ifeq (${ENVIRONMENT}, PRODUCTION)
	DISPLAY := PROD
endif

display:
	echo ${DISPLAY}

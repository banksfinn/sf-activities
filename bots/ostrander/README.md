# Summary
Bot for fetching ostrander permits

Requires an env variable "FLYBOOK_API_KEY", which can be found by going to the reservation site and grabbing it from the headers

# Cron
Running from a cronjob on my local linux box
*/1 * * * * /sf-activities/bots/ostrander/run.sh
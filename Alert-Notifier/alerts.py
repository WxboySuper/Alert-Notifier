# alerts.py
from datetime import datetime

MAX_MESSAGE_LENGTH = 256


def process_alert(properties, area_desc):
    """
    Process an alert notification based on the provided properties and area description.

    Parameters:
        properties (dict): A dictionary containing the alert properties, including headline, event, and parameters.
        area_desc (str): A string describing the affected area.

    Returns:
        tuple: A tuple containing the event, notification message, area description, and expiration datetime.
    """
    headline = properties["headline"]
    description = ''
    event = properties["event"]

    thunderstorm_damage_threat = properties.get("parameters", {}).get("thunderstormDamageThreat")
    tornado_damage_threat = properties.get("parameters", {}).get("tornadoDamageThreat")
    tornado_detection = properties.get("parameters", {}).get("tornadoDetection")
    flash_flood_damage_threat = properties.get("parameters", {}).get("flashFloodDamageThreat")

    if properties['messageType'] == 'Update':
        description += 'UPDATE'

    # Check if the "thunderstormDamageThreat" tag is present
    if thunderstorm_damage_threat:
        description += f", Thunderstorm Damage Threat: {(thunderstorm_damage_threat)}"

    if tornado_damage_threat:
        description += f", Tornado Damage Threat: {(tornado_damage_threat)}"

    if tornado_detection:
        description += f", Tornado Detection: {(tornado_detection)}"

    if flash_flood_damage_threat:
        description += f", Flash Flood Damage Threat: {(flash_flood_damage_threat)}"

    if description != '':
        notification_message = f"{headline}, {description}"
    else:
        notification_message = f"{headline}"

    if len(notification_message) > MAX_MESSAGE_LENGTH:
        notification_message = notification_message[:MAX_MESSAGE_LENGTH - 3] + "..."

    # Get the expiration time from the properties
    expires_datetime = datetime.strptime(properties["expires"], "%Y-%m-%dT%H:%M:%S%z")

    return event, notification_message, area_desc, expires_datetime

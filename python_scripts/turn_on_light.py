# turn_on_light.py
entity_id = data.get("entity_id")
#rgb_color = data.get("rgb_color", [255, 255, 255])
if entity_id is not None:
    service_data = {"entity_id": entity_id}
    hass.services.call("switch", "turn_on", service_data, False)
    
    
# turn_on_light.py
#entity_id = data.get("entity_id")
#rgb_color = data.get("rgb_color", [255, 255, 255])
#if entity_id is not None:
#    service_data = {"entity_id": entity_id, "rgb_color": rgb_color, "brightness": 255}
#    hass.services.call("light", "turn_on", service_data, False)
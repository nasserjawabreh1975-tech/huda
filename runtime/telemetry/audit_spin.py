EVENTS = []

def record_event(event):

    EVENTS.append(event)

    return {
        "recorded": True,
        "event_count": len(EVENTS)
    }

def get_events():

    return EVENTS

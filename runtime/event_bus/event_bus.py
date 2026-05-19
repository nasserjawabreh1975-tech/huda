EVENTS = []

def emit(event):

    EVENTS.append(event)

def get_events():

    return EVENTS[-100:]

def clear_events():

    EVENTS.clear()

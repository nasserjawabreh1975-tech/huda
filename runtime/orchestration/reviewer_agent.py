def reviewer_agent(execution):

    success = execution["results"][0]["success"]

    return {
        "agent": "reviewer",
        "approved": success
    }


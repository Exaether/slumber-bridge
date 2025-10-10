skillsToken = {}


def parse_blackboard(blackboard):
    blackboard_data = {}
    for e in blackboard:
        blackboard_data[e["key"]] = e["value"]
    return blackboard_data

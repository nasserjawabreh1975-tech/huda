class AgentBus:

    def __init__(self):

        self.queue = []

    def submit(self, task):

        self.queue.append(task)

    def execute(self):

        for task in self.queue:

            print("[EXEC]", task)

bus = AgentBus()

bus.submit("optimize runtime")
bus.submit("validate governance")

bus.execute()

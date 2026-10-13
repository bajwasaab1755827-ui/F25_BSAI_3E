class ClassroomAgent:

    def __init__(self):
        self.previous_mode = None

    def act(self, temp, occupied):

        if not occupied:
            target_mode = "ECO"
        elif temp > 26:
            target_mode = "COOL"
        elif temp < 20:
            target_mode = "WARM"
        else:
            target_mode = "IDLE"

        send_command = target_mode != self.previous_mode

        if send_command:
            self.previous_mode = target_mode

        return target_mode, send_command


if __name__ == "__main__":

    agent = ClassroomAgent()

    percepts = [
        (29, True),
        (29, True),
        (20, True),
        (26, True),
        (19, True),
        (29, False)
    ]

    previous_mode = None

    print("Step | Previous | Percept       | Target | Command")
    print("-" * 62)

    for step, (temp, occupied) in enumerate(percepts, 1):

        old_mode = previous_mode
        target, send = agent.act(temp, occupied)

        print(
            f"{step:>4} | {str(old_mode):<8} | "
            f"{(temp, occupied)!s:<13} | "
            f"{target:<6} | "
            f"{'SEND' if send else 'NO SEND'}"
        )

        previous_mode = target
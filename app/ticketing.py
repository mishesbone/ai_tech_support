from datetime import datetime

class Ticket:
    def __init__(self, issue):
        self.id = str(int(datetime.timestamp(datetime.now())))
        self.issue = issue
        self.created_at = datetime.now()
        self.status = "open"

    def __repr__(self):
        return f"Ticket(id={self.id}, status={self.status})"

tickets_db = []

def create_ticket(issue):
    ticket = Ticket(issue)
    tickets_db.append(ticket)
    return ticket

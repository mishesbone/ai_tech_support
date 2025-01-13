knowledge_base = {
    "cloud_storage": "To solve cloud storage issues, try clearing cache or check your cloud service provider's status page.",
    "on_prem_server": "For on-prem server issues, ensure the server is powered on and check for hardware issues.",
}

def fetch_solution(query):
    query_lower = query.lower()
    for key, solution in knowledge_base.items():
        if key in query_lower:
            return solution
    return "Solution not found. Please contact support."

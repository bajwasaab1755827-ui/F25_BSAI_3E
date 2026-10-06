def scholarship_decision(score, documents_complete, attendance, interview_score):

    if score < 70:
        return "HOLD", "Score is below 70"

    if not documents_complete:
        return "HOLD", "Documents are incomplete"

    if attendance < 75:
        return "HOLD", "Attendance is below 75%"

    if interview_score < 60:
        return "HOLD", "Interview score is below 60"

    return "REVIEW", "All conditions are satisfied"

test_cases = [
    ("Pass", 85, True, 80, 75),
    ("Attendance failure", 85, True, 70, 75),
    ("Interview failure", 85, True, 80, 55),
    ("Threshold boundary", 70, True, 75, 60)
]


for name, score, documents, attendance, interview in test_cases:

    actual, reason = scholarship_decision(
        score,
        documents,
        attendance,
        interview
    )

    if name in ["Pass", "Threshold boundary"]:
        expected = "REVIEW"
    else:
        expected = "HOLD"

    print("--------------------------------")
    print("Test Case:", name)
    print("Input:")
    print("Score:", score)
    print("Documents Complete:", documents)
    print("Attendance:", attendance)
    print("Interview Score:", interview)

    print("Expected Result:", expected)
    print("Actual Result:", actual)
    print("Reason:", reason)
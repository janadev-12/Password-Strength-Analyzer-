import math
import re

COMMON_PASSWORDS = [
    "123456",
    "password",
    "123456789",
    "qwerty",
    "abc123",
    "password123",
    "admin",
    "welcome"
]


def calculate_entropy(password):
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[^a-zA-Z0-9]", password):
        charset += 32

    if charset == 0:
        return 0

    return round(len(password) * math.log2(charset), 2)


def analyze_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 20
    else:
        feedback.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 10

    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[0-9]", password):
        score += 15
    else:
        feedback.append("Include numbers.")

    if re.search(r"[^a-zA-Z0-9]", password):
        score += 15
    else:
        feedback.append("Use special characters.")

    if password.lower() not in COMMON_PASSWORDS:
        score += 10
    else:
        feedback.append("Avoid common passwords.")

    entropy = calculate_entropy(password)

    if score >= 80:
        strength = "Very Strong"
        color = "#22c55e"
    elif score >= 60:
        strength = "Strong"
        color = "#84cc16"
    elif score >= 40:
        strength = "Moderate"
        color = "#facc15"
    elif score >= 20:
        strength = "Weak"
        color = "#f97316"
    else:
        strength = "Very Weak"
        color = "#ef4444"

    return {
        "score": score,
        "strength": strength,
        "color": color,
        "entropy": entropy,
        "feedback": feedback
    }
"""Pure resolution rules for the Mirael route.

The Ren'Py script collects the values while the player plays.  This module is
kept free of Ren'Py imports so the same resolver can be exhaustively tested
without the SDK.
"""

ENDING_HUMAN = "human"
ENDING_GUARDIAN = "guardian"

# These are the only values that decide E01/E02.  The names intentionally use
# the store variable names so the rule can be checked against the script.
MIRAEL_ENDING_REQUIREMENTS = {
    "mirael_autonomy": 3,
    "alex_responsibility": 2,
    # Closeness is not a hidden romance score.  The route must have completed
    # both of its linear mutual-contact beats: hand-holding in M03 and the
    # kiss in M06.  It is a completion guard, not a branching advantage.
    "mirael_closeness": 2,
}


# The test script imports this table to enumerate every reachable score
# profile. Values are (false branch, true branch). C03-S02 is deliberately
# included: deleting the photos is an autonomy point, not an evidence-only
# value.
MIRAEL_DECISION_SPEC = (
    ("C00-S01", "alex_responsibility", (0, 1)),
    ("C00-S04 / manifest", "alex_responsibility", (0, 1)),
    ("C01-S02", "alex_responsibility", (0, 1)),
    ("C04-S03", "alex_responsibility", (0, 1)),
    ("C03-S02", "mirael_autonomy", (0, 1)),
    ("C04-S01", "mirael_autonomy", (-1, 1)),
    ("C05-S03", "mirael_autonomy", (-1, 1)),
    ("M01-S03", "mirael_autonomy", (-1, 1)),
    ("M03-S03", "mirael_autonomy", (-1, 1)),
    # M05 is one choice with two effects, so the test treats it specially.
    ("M05-S04", "linked", ("control", "stop")),
)


def ending_checks(autonomy, responsibility, closeness):
    """Return named pass/fail checks for the final resolver."""
    return {
        "mirael_autonomy": autonomy >= MIRAEL_ENDING_REQUIREMENTS["mirael_autonomy"],
        "alex_responsibility": responsibility >= MIRAEL_ENDING_REQUIREMENTS["alex_responsibility"],
        "mirael_closeness": closeness >= MIRAEL_ENDING_REQUIREMENTS["mirael_closeness"],
    }


def resolve_mirael_ending(autonomy, responsibility, closeness):
    """Return the internal endpoint id for the accumulated route state."""
    checks = ending_checks(autonomy, responsibility, closeness)
    if all(checks.values()):
        return ENDING_HUMAN
    return ENDING_GUARDIAN


def ending_report(autonomy, responsibility, closeness):
    """Return a serialisable explanation of why the endpoint was selected."""
    checks = ending_checks(autonomy, responsibility, closeness)
    failed = tuple(name for name, passed in checks.items() if not passed)
    return {
        "ending": resolve_mirael_ending(autonomy, responsibility, closeness),
        "mirael_autonomy": autonomy,
        "alex_responsibility": responsibility,
        "mirael_closeness": closeness,
        "requirements": dict(MIRAEL_ENDING_REQUIREMENTS),
        "checks": checks,
        "failed_checks": failed,
    }

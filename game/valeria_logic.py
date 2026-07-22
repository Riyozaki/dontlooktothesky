"""Pure ending resolver for the Valeria route."""

ENDING_EQUAL = "equal"
ENDING_STANDARD = "standard"
ENDING_FAILURE = "failure"

VALERIA_EQUAL_REQUIREMENTS = {
    "transparency": 3,
    "reciprocity": 1,
    "third_party_autonomy": 2,
}


def equal_contract_failures(transparency: int, reciprocity: int, third_party_autonomy: int) -> tuple[str, ...]:
    failures: list[str] = []
    if transparency < VALERIA_EQUAL_REQUIREMENTS["transparency"]:
        failures.append("transparency")
    if reciprocity < VALERIA_EQUAL_REQUIREMENTS["reciprocity"]:
        failures.append("reciprocity")
    if third_party_autonomy < VALERIA_EQUAL_REQUIREMENTS["third_party_autonomy"]:
        failures.append("third_party_autonomy")
    return tuple(failures)


def equal_contract_is_admissible(transparency: int, reciprocity: int, third_party_autonomy: int) -> bool:
    return not equal_contract_failures(transparency, reciprocity, third_party_autonomy)


def resolve_valeria_ending(transparency: int, reciprocity: int, third_party_autonomy: int) -> str:
    """Resolve the route without a final menu.

    A fully admissible reciprocal contract produces E03. If transparency never
    reached the reciprocal threshold, Alexander chooses the known safety of the
    standard contract (E04). If he became transparent enough to reject ownership
    but damaged reciprocity or third-party autonomy, the reciprocal form is
    removed and he refuses the standard one, producing E05.
    """
    if equal_contract_is_admissible(transparency, reciprocity, third_party_autonomy):
        return ENDING_EQUAL
    if transparency < VALERIA_EQUAL_REQUIREMENTS["transparency"]:
        return ENDING_STANDARD
    return ENDING_FAILURE


def valeria_ending_report(transparency: int, reciprocity: int, third_party_autonomy: int) -> str:
    result = resolve_valeria_ending(transparency, reciprocity, third_party_autonomy)
    failures = equal_contract_failures(transparency, reciprocity, third_party_autonomy)
    return (
        f"result={result}; transparency={transparency}; reciprocity={reciprocity}; "
        f"third_party_autonomy={third_party_autonomy}; failures={','.join(failures) or 'none'}"
    )

def max_daily_paracetamol_child(weight_kg, mg_per_kg_per_dose=15, max_doses_per_day=4):
    """
    Estimate the maximum safe daily dose of paracetamol for a child.

    Parameters
    ----------
    weight_kg : float
        Child's weight in kilograms.
    mg_per_kg_per_dose : float, optional
        Recommended milligrams per kilogram per dose (typical range 10‑15 mg/kg).
    max_doses_per_day : int, optional
        Maximum number of doses allowed in 24 hours (usually 4).

    Returns
    -------
    max_daily_mg : float
        Estimated maximum daily dose in milligrams.
    """
    # Calculate dose per administration, then multiply by number of doses
    dose_per_administration = weight_kg * mg_per_kg_per_dose
    max_daily_mg = dose_per_administration * max_doses_per_day
    return max_daily_mg

# Example usage:
# child_weight = 12   # kg (≈ 26 lb)
# print(f"Estimated max daily dose for a {child_weight}‑kg child: {max_daily_paracetamol_child(child_weight):.0f} mg")
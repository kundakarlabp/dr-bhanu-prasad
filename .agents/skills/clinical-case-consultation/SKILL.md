---
name: clinical-case-consultation
description: Analyze complex individual clinical cases, especially infectious diseases, transplant, ICU, immunocompromised-host infections, antimicrobial dosing, toxicity, and diagnostic uncertainty.
---

# Clinical Case Consultation

## Purpose

Convert incomplete case information into a structured, patient-specific assessment and actionable plan without hiding uncertainty.

## Workflow

1. Extract confirmed data only:
   - age, weight, immune status, comorbidities
   - syndrome, timeline, severity, organ dysfunction
   - microbiology, susceptibility method, imaging, pathology
   - source control and devices
   - current and prior antimicrobials
   - renal/hepatic function, drug levels, interactions, allergies
2. Identify immediate threats and management priorities before expanding the differential.
3. Build a ranked differential using positive and negative evidence. Separate likely diagnosis, dangerous alternatives, and mimics.
4. Assess whether available microbiology represents infection, colonization, contamination, or uncertain significance.
5. Define the minimum investigations needed to resolve decisions; avoid indiscriminate testing.
6. Recommend treatment with exact dose, route, interval, duration range, adjustment rules, source control, and monitoring when evidence permits.
7. Reassess treatment adequacy by spectrum, penetration, susceptibility, PK/PD target, interaction, toxicity, and feasibility.
8. Specify response criteria, failure criteria, and when to escalate, de-escalate, or stop.

## Required output

- **Working assessment**
- **Ranked differential**
- **Immediate actions**
- **Investigations that change management**
- **Treatment plan**
- **Monitoring and reassessment**
- **Uncertainty / missing data**

For urgent bedside questions, lead with the actionable plan and then justify it.

## Safety checks

- Recalculate weight-based doses independently.
- Use current renal replacement, dialysis, ECMO, obesity, pediatric, or transplant dosing evidence when relevant.
- Check major CYP, P-gp, QT, marrow, renal, hepatic, and immunosuppressant interactions.
- Do not infer susceptibility from species alone when resistance is variable.
- Do not recommend monotherapy for deep-seated infection when resistance emergence or poor penetration makes it unsafe.
- Do not treat a laboratory result without clinical correlation.

## Failure and uncertainty handling

State what is unknown and what decision depends on it. When evidence is weak, present the preferred option, acceptable alternatives, and the reason one is favored. Escalate emergency or specialist review when delay could cause harm.

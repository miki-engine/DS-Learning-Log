"""Manually check A/B test reports and expected errors."""

import pandas as pd

from ab_test_analysis.main import (
    add_purchase_rate,
    perform_purchase_rate_test,
    print_analysis_report,
)

test_cases = {
    "significant_improvement": {
        "group": ["Control", "Test"],
        "users_count": [500, 500],
        "purchased_count": [30, 80],
    },
    "inconclusive_improvement": {
        "group": ["Control", "Test"],
        "users_count": [503, 497],
        "purchased_count": [37, 43],
    },
    "observed_decrease": {
        "group": ["Control", "Test"],
        "users_count": [500, 500],
        "purchased_count": [60, 20],
    },
    "same_rate": {
        "group": ["Control", "Test"],
        "users_count": [500, 500],
        "purchased_count": [40, 40],
    },
    "zero_control": {
        "group": ["Control", "Test"],
        "users_count": [500, 500],
        "purchased_count": [0, 25],
    },
    "all_zero": {
        "group": ["Control", "Test"],
        "users_count": [500, 500],
        "purchased_count": [0, 0],
    },
    "all_purchased": {
        "group": ["Control", "Test"],
        "users_count": [500, 500],
        "purchased_count": [500, 500],
    },
}

expected_error_cases = {
    "all_zero",
    "all_purchased",
}

for case_name, case in test_cases.items():
    df = pd.DataFrame(case)
    summary = add_purchase_rate(df)
    print(f"\n=== {case_name} ===")

    try:
        test_result = perform_purchase_rate_test(summary)

    except ValueError as e:
        if case_name in expected_error_cases:
            print(f"Expected error: {e}")
        else:
            raise
    else:
        if case_name in expected_error_cases:
            raise AssertionError(
                f"Expected ValueError was not raised: {case_name}"
            )

        print_analysis_report(summary, test_result)
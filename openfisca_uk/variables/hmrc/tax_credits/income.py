from openfisca_uk.model_api import *


class tax_credits_applicable_income(Variable):
    label = "Income for Tax Credits"
    entity = BenUnit
    definition_period = YEAR
    value_type = float
    unit = "currency-GBP"
    reference = "https://www.legislation.gov.uk/uksi/2002/2006/regulation/3"

    def formula(benunit, period, parameters):
        tc = parameters(period).hmrc.tax_credits.means_test
        unearned_income = max_(
            0,
            aggr(benunit, period, tc.income.unearned.components)
            - tc.income.unearned.disregard,
        )
        earned_income = aggr(benunit, period, tc.income.earned)
        return unearned_income + earned_income
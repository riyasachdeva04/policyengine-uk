from openfisca_uk.model_api import *


class wtc_basic_element(Variable):
    label = "WTC basic element"
    entity = BenUnit
    definition_period = YEAR
    value_type = float
    unit = "currency-GBP"
    reference = "https://www.legislation.gov.uk/uksi/2002/2005/part/2/crossheading/basic-element"

    def formula(benunit, period, parameters):
        # This is a parameter-only variable in order to ensure the
        # WTC allowed elements parameter list functions.
        wtc = parameters(period).hmrc.tax_credits.working_tax_credit
        return wtc.elements.basic

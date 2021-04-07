from openfisca_core.model_api import *
from openfisca_uk.entities import *
from openfisca_uk.tools.general import *

class weekly_employee_NI_class_1(Variable):
    value_type = float
    entity = Person
    label = u'Employee Class 1 Contributions for National Insurance'
    definition_period = WEEK
    reference = "Social Security Contributions and Benefits Act 1992 s. 8"

    def formula(person, period, parameters):
        class_1 = parameters(period).tax.national_insurance.class_1
        weekly_earnings = person("employment_income", period, options=[DIVIDE])
        main_earnings = amount_between(weekly_earnings, class_1.thresholds.primary_threshold, class_1.thresholds.upper_earnings_limit)
        charge = class_1.rates.employee.main * main_earnings
        return charge

class employee_NI_class_1(Variable):
    value_type = float
    entity = Person
    label = u'Employee Class 1 Contributions for National Insurance'
    definition_period = YEAR

    def formula(person, period, parameters):
        return person("weekly_employee_NI_class_1", period, options=[ADD])

class weekly_employer_NI_class_1(Variable):
    value_type = float
    entity = Person
    label = u'Employer Class 1 Contributions for National Insurance'
    definition_period = WEEK
    reference = "Social Security Contributions and Benefits Act 1992 s. 8"

    def formula(person, period, parameters):
        class_1 = parameters(period).tax.national_insurance.class_1
        weekly_earnings = person("employment_income", period, options=[DIVIDE])
        main_earnings = amount_between(weekly_earnings, class_1.thresholds.primary_threshold, class_1.thresholds.upper_earnings_limit)
        charge = class_1.rates.employer * main_earnings
        return charge

class employer_NI_class_1(Variable):
    value_type = float
    entity = Person
    label = u'Employer Class 1 Contributions for National Insurance'
    definition_period = YEAR

    def formula(person, period, parameters):
        return person("weekly_employer_NI_class_1", period, options=[ADD])

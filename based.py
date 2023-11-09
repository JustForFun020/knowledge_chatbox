from constance import *
from skfuzzy import control
import numpy as np
import matplotlib.pyplot as plt

# Input
field_specialized = control.Antecedent(np.arange(0, 6, 1), "Specialized Field")
field_salary = control.Antecedent(np.arange(0, 5, 1), "Salary Field")
field_code_knowledge = control.Antecedent(np.arange(0, 2, 1), "Code Knowledge Field")
field_skills = control.Antecedent(np.arange(0, 8, 1), "Skills Field")
field_lang = control.Antecedent(np.arange(0, 11, 1), "Language Field")
field_ide = control.Antecedent(np.arange(0, 13, 1), "Ide Field")
field_tools = control.Antecedent(np.arange(0, 9, 1), "Tools Field")
field_db = control.Antecedent(np.arange(0, 7, 1), "Database Field")
field_sql = control.Antecedent(np.arange(0, 2, 1), "SQL Field")
field_cloud = control.Antecedent(np.arange(0, 2, 1), "Cloud Field")
field_oi = control.Antecedent(np.arange(0, 2, 1), "Office Information Field")
field_owasp = control.Antecedent(np.arange(0, 2, 1), "OWASP Top 10 Field")
field_ci_cd = control.Antecedent(np.arange(0, 2, 1), "CI/CD Field")
field_uiux = control.Antecedent(np.arange(0, 2, 1), "UI/UX Field")
field_math = control.Antecedent(np.arange(0, 2, 1), "Math Field")
field_network = control.Antecedent(np.arange(0, 2, 1), "Network Field")
field_security = control.Antecedent(np.arange(0, 2, 1), "Security Field")

# Output
field_jobs = control.Consequent(np.arange(0, 21, 1), "Jobs Field")

# Membership
field_specialized.automf(6, names=specialized)
field_salary.automf(5, names=salary)
field_code_knowledge.automf(2, names=booleanAns)
field_lang.automf(11, names=lang)
field_ide.automf(13, names=ide)
field_tools.automf(9, names=tools)
field_skills.automf(8, names=skills)
field_db.automf(7, names=db)
field_cloud.automf(2, names=booleanAns)
field_oi.automf(2, names=booleanAns)
field_owasp.automf(2, names=booleanAns)
field_sql.automf(2, names=booleanAns)
field_ci_cd.automf(2, names=booleanAns)
field_uiux.automf(2, names=booleanAns)
field_math.automf(2, names=booleanAns)
field_network.automf(2, names=booleanAns)
field_security.automf(2, names=booleanAns)

field_jobs.automf(21, names=jobs)

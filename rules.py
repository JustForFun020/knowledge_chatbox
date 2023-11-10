from skfuzzy import control
from constance import *
from based import *


# Tập quy tắc lĩnh vực công nghệ phần mềm
class RuleOfCNPM:
    rule_fe = control.Rule(
        field_specialized["Công nghệ phần mềm"]
        & field_ci_cd["No"]
        & field_uiux["Yes"]
        & field_cloud["No"]
        & field_sql["No"]
        & field_code_knowledge["Yes"]
        & field_lang["Javascript"]
        & (field_salary["13 - 20"] | field_salary["20 - 30"])
        & field_ide["VSCode"]
        & field_db["UnKnown"],
        field_jobs["FE"],
    )

    rule_be = control.Rule(
        field_specialized["Công nghệ phần mềm"]
        & field_ci_cd["No"]
        & field_uiux["No"]
        & field_cloud["No"]
        & field_sql["Yes"]
        & field_code_knowledge["Yes"]
        & (
            field_lang["Javascript"]
            | field_lang["Java"]
            | field_lang["Python"]
            | field_lang["PHP"]
        )
        & (field_ide["VSCode"] | field_ide["Eclipse"])
        & (field_salary["over 30"] | field_salary["13 - 20"] | field_salary["20 - 30"])
        & (
            field_db["MongoDB"]
            | field_db["SQL Server"]
            | field_db["MySQL"]
            | field_db["PostgreSQL"]
        ),
        field_jobs["BE"],
    )

    rule_android = control.Rule(
        field_specialized["Công nghệ phần mềm"]
        & field_ci_cd["No"]
        & field_uiux["No"]
        & field_cloud["No"]
        & field_sql["Yes"]
        & field_code_knowledge["Yes"]
        & (field_lang["Java"] | field_lang["Kotlin"])
        & (field_ide["Android Studio"] | field_ide["IntelliJ IDEA"])
        & (
            field_db["MongoDB"]
            | field_db["SQL Server"]
            | field_db["MySQL"]
            | field_db["PostgreSQL"]
        )
        & (field_salary["20 - 30"] | field_salary["over 30"] | field_salary["13 - 20"]),
        field_jobs["Android Dev"],
    )

    rule_ios = control.Rule(
        field_specialized["Công nghệ phần mềm"]
        & field_ci_cd["No"]
        & field_sql["Yes"]
        & field_uiux["No"]
        & field_cloud["No"]
        & field_code_knowledge["Yes"]
        & (field_lang["Swift"] | field_lang["C/C++"])
        & field_ide["XCode"]
        & (
            field_db["MongoDB"]
            | field_db["SQL Server"]
            | field_db["MySQL"]
            | field_db["PostgreSQL"]
        )
        & (field_salary["20 - 30"] | field_salary["over 30"] | field_salary["13 - 20"]),
        field_jobs["iOS Dev"],
    )

    rule_iot = control.Rule(
        field_specialized["Công nghệ phần mềm"]
        & field_ci_cd["No"]
        & field_uiux["No"]
        & field_cloud["Yes"]
        & field_sql["Yes"]
        & field_code_knowledge["Yes"]
        & (field_lang["Python"] | field_lang["C/C++"] | field_lang["Javascript"])
        & field_ide["Arduino"]
        & (
            field_db["MongoDB"]
            | field_db["SQL Server"]
            | field_db["MySQL"]
            | field_db["PostgreSQL"]
        )
        & (field_salary["20 - 30"] | field_salary["over 30"] | field_salary["13 - 20"]),
        field_jobs["Iot Developer"],
    )

    rule_devOps = control.Rule(
        field_specialized["Công nghệ phần mềm"]
        & field_ci_cd["Yes"]
        & field_uiux["No"]
        & field_ide["UnKnown"]
        & field_lang["UnKnown"]
        & field_cloud["Yes"]
        & field_sql["Yes"]
        & (field_code_knowledge["No"])
        & field_skills["Ops"]
        & (
            field_db["MongoDB"]
            | field_db["SQL Server"]
            | field_db["MySQL"]
            | field_db["PostgreSQL"]
        )
        & (field_salary["20 - 30"] | field_salary["over 30"] | field_salary["13 - 20"]),
        field_jobs["DevOps Engineer"],
    )

    rule_ba = control.Rule(
        field_specialized["Công nghệ phần mềm"]
        & (field_uiux["Yes"] | field_uiux["No"])
        & (field_sql["Yes"] | field_sql["No"])
        & field_oi["Yes"]
        & (field_salary["13 - 20"] | field_salary["20 - 30"])
        & field_code_knowledge["No"]
        & field_tools["Microsoft Visio"]
        & (field_skills["Economy"]),
        field_jobs["BA"],
    )

    rule_uiux = control.Rule(
        field_specialized["Công nghệ phần mềm"]
        & (field_tools["Figma"] | field_tools["Adobe Photoshop"])
        & field_code_knowledge["No"]
        & field_uiux["Yes"]
        & field_oi["No"]
        & field_lang["UnKnown"]
        & field_ide["UnKnown"]
        & field_skills["UnKnown"]
        & (field_salary["13 - 20"] | field_salary["20 - 30"]),
        field_jobs["UI/UX Designer"],
    )

    rule_tester = control.Rule(
        field_specialized["Công nghệ phần mềm"]
        & field_uiux["Yes"]
        & field_oi["Yes"]
        & field_code_knowledge["No"]
        & (
            field_tools["Selenium"]
            | field_tools["Test complete"]
            | field_tools["TestingWhiz"]
        )
        & field_skills["UnKnown"]
        & (field_salary["13 - 20"] | field_salary["20 - 30"]),
        field_jobs["Tester"],
    )


# Tập quy tắc lĩnh vực khoa học dữ liệu
class RuleOfKHDL:
    rule_ds = control.Rule(
        field_specialized["Khoa học dữ liệu"]
        & field_math["Yes"]
        & (field_cloud["Yes"] | field_cloud["No"])
        & field_sql["Yes"]
        & field_oi["No"]
        & (field_operate["Yes"] | field_operate["No"])
        & field_code_knowledge["Yes"]
        & (field_ide["Jupyter Notebook"] | field_ide["RStudio"] | field_ide["VSCode"])
        & (field_skills["ML"])
        & (field_lang["Python"] | field_lang["Rust"])
        & (
            field_db["MongoDB"]
            | field_db["SQL Server"]
            | field_db["MySQL"]
            | field_db["PostgreSQL"]
            | field_db["Redis"]
        )
        & (field_salary["20 - 30"] | field_salary["over 30"]),
        field_jobs["DS"],
    )

    rule_de = control.Rule(
        field_specialized["Khoa học dữ liệu"]
        & field_cloud["Yes"]
        & field_math["Yes"]
        & (field_operate["Yes"] | field_operate["No"])
        & field_sql["Yes"]
        & field_oi["No"]
        & (field_code_knowledge["Yes"] | field_code_knowledge["No"])
        & field_ide["UnKnown"]
        & field_skills["ML"]
        & field_lang["UnKnown"]
        & (field_lang["Python"] | field_lang["Rust"] | field_lang["Java"])
        & (
            field_db["MongoDB"]
            | field_db["SQL Server"]
            | field_db["MySQL"]
            | field_db["PostgreSQL"]
            | field_db["Redis"]
        )
        & (field_salary["20 - 30"] | field_salary["over 30"]),
        field_jobs["DE"],
    )

    rule_dba = control.Rule(
        field_specialized["Khoa học dữ liệu"]
        & field_cloud["No"]
        & (field_math["Yes"] | field_math["No"])
        & field_sql["Yes"]
        & (field_oi["Yes"] | field_oi["No"])
        & (field_code_knowledge["No"])
        & field_operate["Yes"]
        & (field_skills["ML"] | field_skills["UnKnown"])
        & (field_lang["UnKnown"])
        & field_ide["UnKnown"]
        & (
            field_db["MongoDB"]
            | field_db["SQL Server"]
            | field_db["MySQL"]
            | field_db["PostgreSQL"]
            | field_db["Redis"]
            | field_db["Oracle Database"]
        )
        & (field_salary["20 - 30"] | field_salary["over 30"]),
        field_jobs["DBA"],
    )

    rule_da = control.Rule(
        field_specialized["Khoa học dữ liệu"]
        & field_cloud["No"]
        & (field_operate["Yes"] | field_operate["No"])
        & field_math["Yes"]
        & field_sql["Yes"]
        & field_oi["Yes"]
        & (field_code_knowledge["No"] | field_code_knowledge["Yes"])
        & (field_lang["Python"] | field_lang["Rust"])
        & (field_skills["ML"])
        & field_ide["UnKnown"]
        & (
            field_db["MongoDB"]
            | field_db["SQL Server"]
            | field_db["MySQL"]
            | field_db["PostgreSQL"]
            | field_db["Redis"]
        )
        & (field_salary["20 - 30"] | field_salary["over 30"]),
        field_jobs["DA"],
    )


# Tập quy tắc lĩnh vực game
class RuleOfGame:
    rule_game = control.Rule(
        field_specialized["Game"]
        & field_uiux["Yes"]
        & (field_sql["Yes"] | field_sql["No"])
        & field_code_knowledge["Yes"]
        & (field_db["MySQL"] | field_db["MongoDB"] | field_db["SQL Server"])
        & (field_lang["Unity"] | field_lang["C#"] | field_lang["C/C++"])
        & (field_ide["VSCode"] | field_ide["Unity"] | field_ide["Unreal Engine"])
        & (field_salary["13 - 20"] | field_salary["20 - 30"] | field_salary["over 30"]),
        field_jobs["Game Dev"],
    )


# Tập quy tắc lĩnh vực an toàn thông tin
class RuleOfATTT:
    rule_isa = control.Rule(
        field_specialized["An toàn thông tin"]
        & (field_code_knowledge["No"] | field_code_knowledge["Yes"])
        & field_security["Yes"]
        & field_network["No"]
        & field_cloud["No"]
        & (field_oi["Yes"] | field_oi["No"])
        & field_tools["SIEM"]
        & field_skills["UnKnown"]
        & field_owasp["No"]
        & (field_salary["6 - 12"] | field_salary["13 - 20"] | field_salary["20 - 30"]),
        field_jobs["ISA"],
    )

    rule_itse = control.Rule(
        field_specialized["An toàn thông tin"]
        & (field_code_knowledge["No"] | field_code_knowledge["Yes"])
        & field_security["No"]
        & field_network["Yes"]
        & field_cloud["No"]
        & (field_oi["Yes"] | field_oi["No"])
        & field_tools["UnKnown"]
        & (field_skills["Protocol"])
        & field_owasp["No"]
        & (field_salary["20 - 30"] | field_salary["13 - 20"]),
        field_jobs["ITSE"],
    )

    rule_nss = control.Rule(
        field_specialized["An toàn thông tin"]
        & (field_code_knowledge["No"] | field_code_knowledge["Yes"])
        & field_security["No"]
        & field_network["Yes"]
        & field_cloud["No"]
        & (field_oi["Yes"] | field_oi["No"])
        & field_tools["UnKnown"]
        & field_skills["Protocol"]
        & field_owasp["Yes"]
        & (field_salary["20 - 30"]),
        field_jobs["NSS"],
    )


# Tập quy tắc lĩnh it-  phần cứng
class RuleOfHardware:
    rule_hepdesk = control.Rule(
        field_specialized["IT - Hardware"]
        & (field_code_knowledge["No"] | field_code_knowledge["Yes"])
        & (field_security["No"] | field_security["Yes"])
        & field_network["Yes"]
        & (field_oi["Yes"] | field_oi["No"])
        & (field_skills["Protocol"])
        & (field_salary["0 - 5"] | field_salary["6 - 12"] | field_salary["13 - 20"]),
        field_jobs["IT - Helpdesk"],
    )


# Tập quy tắc lĩnh vực trí tuệ nhân tạo
class RuleOfAI:
    rule_ae = control.Rule(
        field_specialized["Trí tuệ nhân tạo"]
        & (field_cloud["No"] | field_cloud["Yes"])
        & field_math["Yes"]
        & field_sql["Yes"]
        & field_oi["No"]
        & field_code_knowledge["Yes"]
        & (
            field_db["MongoDB"]
            | field_db["SQL Server"]
            | field_db["MySQL"]
            | field_db["PostgreSQL"]
            | field_db["Redis"]
            | field_db["Oracle Database"]
        )
        & (field_lang["Python"] | field_lang["Rust"] | field_lang["C/C++"])
        & (field_ide["Jupyter Notebook"] | field_ide["VSCode"])
        & (field_skills["ML"])
        & (field_salary["20 - 30"] | field_salary["over 30"]),
        field_jobs["AI Engineer"],
    )

    rule_ar = control.Rule(
        field_specialized["Trí tuệ nhân tạo"]
        & field_cloud["No"]
        & field_math["Yes"]
        & field_sql["Yes"]
        & field_oi["Yes"]
        & (field_code_knowledge["No"] | field_code_knowledge["Yes"])
        & (
            field_lang["Python"]
            | field_lang["Rust"]
            | field_lang["C/C++"]
            | field_lang["UnKnown"]
        )
        & field_ide["UnKnown"]
        & (
            field_db["MongoDB"]
            | field_db["SQL Server"]
            | field_db["MySQL"]
            | field_db["PostgreSQL"]
            | field_db["Redis"]
            | field_db["Oracle Database"]
        )
        & (field_skills["ML"])
        & (field_salary["over 30"]),
        field_jobs["AI Researcher"],
    )


class SystemRule:
    job_control = control.ControlSystem(
        [
            RuleOfCNPM.rule_fe,
            RuleOfCNPM.rule_be,
            RuleOfCNPM.rule_android,
            RuleOfCNPM.rule_ios,
            RuleOfCNPM.rule_iot,
            RuleOfCNPM.rule_devOps,
            RuleOfCNPM.rule_ba,
            RuleOfCNPM.rule_uiux,
            RuleOfCNPM.rule_tester,
            RuleOfAI.rule_ae,
            RuleOfAI.rule_ar,
            RuleOfKHDL.rule_da,
            RuleOfKHDL.rule_dba,
            RuleOfKHDL.rule_de,
            RuleOfKHDL.rule_ds,
            RuleOfATTT.rule_isa,
            RuleOfATTT.rule_nss,
            RuleOfATTT.rule_itse,
            RuleOfGame.rule_game,
            RuleOfHardware.rule_hepdesk,
        ]
    )
    job_prediction = control.ControlSystemSimulation(job_control)

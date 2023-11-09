import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Khởi tạo các biến đầu vào
field_of_study = ctrl.Antecedent(np.arange(0, 3, 1), "field_of_study")
salary = ctrl.Antecedent(np.arange(0, 5, 1), "salary")
programming_knowledge = ctrl.Antecedent(np.arange(0, 2, 1), "programming_knowledge")
programming_language = ctrl.Antecedent(np.arange(0, 6, 1), "programming_language")
ide_used = ctrl.Antecedent(np.arange(0, 5, 1), "ide_used")
database_used = ctrl.Antecedent(np.arange(0, 7, 1), "database_used")
ui_ux_knowledge = ctrl.Antecedent(np.arange(0, 2, 1), "ui_ux_knowledge")
job = ctrl.Consequent(np.arange(0, 3, 1), "job")

# Định nghĩa các hàm thành viên cho mỗi biến
field_of_study.automf(
    3, names=["software_technology", "information_security", "data_science"]
)
salary.automf(5, names=["0-5", "6-12", "13-20", "20-30", "over_30"])
programming_knowledge.automf(2, names=["no", "yes"])
programming_language.automf(
    6, names=["java", "python", "javascript", "c_cpp", "swift", "php"]
)
ide_used.automf(5, names=["eclipse", "pycharm", "vscode", "unity", "android_studio"])
database_used.automf(
    7,
    names=[
        "not_used",
        "sql_server",
        "mysql",
        "mongodb",
        "oracle",
        "postgresql",
        "redis",
    ],
)
ui_ux_knowledge.automf(2, names=["no", "yes"])
job.automf(3, names=["back_end_developer", "front_end_developer", "data_scientist"])

# Tạo các quy tắc
rule1 = ctrl.Rule(
    field_of_study["software_technology"]
    & salary["20-30"]
    & programming_knowledge["yes"]
    & programming_language["javascript"]
    & ide_used["vscode"]
    & database_used["not_used"]
    & ui_ux_knowledge["yes"],
    job["front_end_developer"],
)

# Tạo một bộ quy tắc
job_ctrl = ctrl.ControlSystem([rule1])

# Tạo mô hình dự đoán
job_prediction = ctrl.ControlSystemSimulation(job_ctrl)

# Giao tiếp với người dùng
print("Chatbox: Bạn muốn làm việc trong lĩnh vực nào?")
print("0: Công nghệ phần mềm")
print("1: An toàn thông tin")
print("2: Khoa học dữ liệu")

field_choice = int(input("Lựa chọn của bạn: "))
salary_choice = int(input("Lựa chọn của bạn: "))
programming_knowledge_c = int(input("Lựa chọn của bạn: "))
programming_language_c = int(input("Lựa chọn của bạn: "))
ide_used_c = int(input("Lựa chọn của bạn: "))
database_used_c = int(input("Lựa chọn của bạn: "))
ui_ux_knowledge_c = int(input("Lựa chọn của bạn: "))
# Tiếp tục với các câu hỏi khác tương tự

# Gán giá trị cho biến đầu vào trong mô hình
job_prediction.input["field_of_study"] = field_choice
job_prediction.input["salary"] = salary_choice
job_prediction.input["programming_knowledge"] = programming_knowledge_c
job_prediction.input["programming_language"] = programming_language_c
job_prediction.input["ide_used"] = ide_used_c
job_prediction.input["database_used"] = database_used_c
job_prediction.input["ui_ux_knowledge"] = ui_ux_knowledge_c
# Tiếp tục với việc gán giá trị cho các biến đầu vào khác

# Tính toán kết quả
job_prediction.compute()

# In kết quả
print("Công việc phù hợp với bạn là: ", job_prediction.output["job"])

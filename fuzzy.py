import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
import numpy as np


# Đầu vào
experience = ctrl.Antecedent(np.arange(0, 11, 1), "experience")
skill = ctrl.Antecedent(np.arange(0, 11, 1), "skill")

# Đầu ra
job = ctrl.Consequent(np.arange(0, 11, 1), "job")

# Sử dụng hàm automf để tự động tạo các hàm thành viên
experience.automf(3, names=["low", "medium", "high"])
skill.automf(3, names=["low", "medium", "high"])
job.automf(3, names=["low", "medium", "high"])

# Tạo các quy tắc
low_rule = ctrl.Rule(experience["low"] | skill["low"], job["low"])
medium_rule = ctrl.Rule(experience["medium"] | skill["medium"], job["medium"])
high_rule = ctrl.Rule(experience["high"] | skill["high"], job["high"])

# Định nghĩa và xây dựng hệ thống giải mờ. Hệ thống giải mờ này chứa các biến đầu vào, biến xuất, các quy tắc giải mờ và một số thông tin khác
# để mô tả cách một hệ thống hoạt động theo logic giải mờ.
job_ctrl = ctrl.ControlSystem([low_rule, medium_rule, high_rule])
# Thực hiện mô phỏng hệ thống giải mờ. Nó giúp bạn nhập giá trị cho các biến đầu vào,
# thực hiện quy tắc giải mờ và tính toán giá trị của biến xuất.
job_sim = ctrl.ControlSystemSimulation(job_ctrl)

# Gán giá trị cho biến đầu vào
job_sim.input["experience"] = 3
job_sim.input["skill"] = 9

# Thực hiện quy tắc giải mờ và tính toán giá trị của biến đầu ra
job_sim.compute()
print(job_sim.output["job"])

# Vẽ đồ thị
job.view(sim=job_sim)
plt.show()

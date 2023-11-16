from rules import *
from question import *
import matplotlib.pyplot as plt
import time

system_question = ChatBoxQuestion()
system_rule = SystemRule()


def welcome_message():
    print(
        "------------------------------ Welcome to ChatBox ------------------------------\n"
    )
    time.sleep(1)
    print("-------> Chào bạn, tôi là ChatBox tư vấn việc làm Công nghệ thông tin\n")
    time.sleep(1)
    print(
        "Để biết được bạn phù hợp với vị trí nào trong lĩnh vực công nghệ thông tin, hay cung cấp thông tin của bạn bằng cách trả lời các câu hỏi sau đây để tôi có thể gợi ý việc làm phù hợp nhập với bạn \n"
    )


welcome_message()

time.sleep(1)
while True:
    # Lập trình
    system_question.first_question()
    # Lương
    system_question.second_question()
    # Lĩnh vực
    system_question.third_question()
    if "Biết lập trình" in user_choice and "Công nghệ phần mềm" in user_choice:
        job_prediction.input["Tools Field"] = 0
        # Languages
        system_question.fourth_question()
        # IDE
        system_question.fifth_question()
        # SQL
        system_question.eighth_question()
        # Database
        system_question.sixteen_question()
        # CI/CD
        system_question.eleventeen_question()
        # Ops
        system_question.eightteen_question()
        # UI/UX
        system_question.ninth_question()
        # Cloud
        system_question.thirdteen_question()
        break
    elif "Không biết lập trình" in user_choice and "Công nghệ phần mềm" in user_choice:
        job_prediction.input["CI/CD Field"] = 0
        job_prediction.input["Math Field"] = 0
        job_prediction.input["Database Field"] = 0
        job_prediction.input["Cloud Field"] = 0
        # Tin học văn phòng
        system_question.seventh_question()
        # Tools
        system_question.sixth_question()
        # SQL
        system_question.eighth_question()
        # UI/UX
        system_question.ninth_question()
        # Kinh tế
        system_question.ninteen_question()
        break
    elif "An toàn thông tin" in user_choice:
        # Tin học văn phòng
        system_question.seventh_question()
        # Protocol
        system_question.twelfth_question()
        # Network
        system_question.fourthteen_question()
        # Security
        system_question.fifteen_question()
        # SIEM
        system_question.twenty_question()
        # OWASP
        system_question.twenty_one_question()
        # Operate
        system_question.twenty_two_question()
        break
    elif "Không biết lập trình" in user_choice and "Khoa học dữ liệu" in user_choice:
        # SQL
        system_question.eighth_question()
        # Database
        system_question.sixteen_question()
        # Math
        system_question.tenth_question()
        # Machine Learning
        system_question.eleventh_question()
        # Cloud
        system_question.thirdteen_question()
        # Operate
        system_question.twenty_two_question()
        break
    elif "Biết lập trình" in user_choice and "Khoa học dữ liệu" in user_choice:
        job_prediction.input["Office Information Field"] = 0
        # Languages
        system_question.fourth_question()
        # IDE
        system_question.fifth_question()
        # SQL
        system_question.eighth_question()
        # Database
        system_question.sixteen_question()
        # Math
        system_question.tenth_question()
        # Machine Learning
        system_question.eleventh_question()
        # Cloud
        system_question.thirdteen_question()
        # Operate
        system_question.twenty_two_question()
        break
    elif "IT - Phần cứng" in user_choice:
        # Network
        system_question.fourthteen_question()
        # Protocol
        system_question.twelfth_question()
        # Tin học văn phòng
        system_question.seventh_question()
        # Security
        system_question.fifteen_question()
        break
    elif "Không biết lập trình" in user_choice and "Trí tuệ nhân tạo" in user_choice:
        job_prediction.input["Ide Field"] = 12
        # Kinh tế
        system_question.ninteen_question()
        # Tools
        system_question.sixth_question()
        # Database
        system_question.sixteen_question()
        # Math
        system_question.tenth_question()
        # Machine Learning
        system_question.eleventh_question()
        # SQL
        system_question.eighth_question()
        # Cloud
        system_question.thirdteen_question()
        break
    elif "Biết lập trình" in user_choice and "Trí tuệ nhân tạo" in user_choice:
        # Languages
        system_question.fourth_question()
        # IDE
        system_question.fifth_question()
        # Database
        system_question.sixteen_question()
        # Math
        system_question.tenth_question()
        # Machine Learning
        system_question.eleventh_question()
        # SQL
        system_question.eighth_question()
        # Cloud
        system_question.thirdteen_question()
        break
    elif "Game" in user_choice:
        # Languages
        system_question.fourth_question()
        # IDE
        system_question.fifth_question()
        # SQL
        system_question.eighth_question()
        # Database
        system_question.sixteen_question()
        # UI/UX
        system_question.ninth_question()
        break
    else:
        print("no")
        break

try:
    jobs = {
        (0, 0.533): "Front-End Developer",
        (0.533, 1.533): "Back-End Developer",
        (1.533, 2.56): "Android Developer",
        (2.56, 3.57): "iOS Developer",
        (3.57, 4.61): "IoT Developer",
        (4.61, 5.63): "DepOps Engineer",
        (5.63, 6.69): "Business Analyst",
        (6.69, 7.76): "UI/UX Designer",
        (7.76, 8.85): "Tester",
        (8.85, 10): "AI Engineer",
        (10, 11.13): "AI Researcher",
        (11.13, 12.25): "Data Analysis",
        (12.25, 13.30): "Database Administrator",
        (13.30, 14.30): "Data Engineer",
        (14.30, 15.30): "Data Scientist",
        (15.30, 16.40): "Information security analyst",
        (16.40, 17.45): "Network Security Specialist",
        (17.45, 18.45): "IT Security Engineer",
        (18.45, 19.45): "Game Developer",
        (19.45, float("inf")): "IT - Helpdesk",
    }
    job_prediction.compute()
    value = job_prediction.output["Jobs Field"]
    for (low, high), job in jobs.items():
        if low <= value < high:
            time.sleep(1)
            print("Các lựa chọn của bạn là")
            for i in user_choice:
                print(f"+++++  {i}")
            time.sleep(2)
            print("Hệ thống đang tính toán số liệu, bạn vui lòng chờ trong giây lát...")
            time.sleep(3)
            print(f"Công việc phù hợp với bạn là: {job}")
            break
    else:
        print("Không tìm thấy việc phù hợp")
except Exception as e:
    print(e)
    print("Không tìm thấy việc phù hợp")

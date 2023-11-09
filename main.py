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
    print("-------> Chào bạn, tôi là ChatBox tư vấn việc làm Công nghệ thông tin\n")
    print(
        "Để biết được bạn phù hợp với vị trí nào trong lĩnh vực công nghệ thông tin, hay cung cấp thông tin của bạn bằng cách trả lời các câu hỏi sau đây để tôi có thể gợi ý việc làm phù hợp nhập với bạn \n"
    )


welcome_message()


while True:
    # Lập trình
    system_question.first_question()
    # Lương
    system_question.second_question()
    # Lĩnh vực
    system_question.third_question()
    # --> các trường đã có: Specialized Field, Code Knowledge Field, Salary Field
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
    job_prediction.compute()
    value = job_prediction.output["Jobs Field"]
    print("\n")
    time.sleep(1.5)
    print("Đây là những lựa chọn của bạn:")
    for x in user_choice:
        print(f"+++++++++++++ {x} \n")

    time.sleep(1.5)
    print("Hệ thống đang tính toán kết quả, bạn vui lòng chờ một vài giây......")
    time.sleep(3)
    if 0 <= value < 0.533:
        print("Công việc phù hợp với bạn là: Front-End Developer")
    elif 0.533 <= value < 1.533:
        print("Công việc phù hợp với bạn là: Back-End Developer")
    elif 1.533 <= value < 2.56:
        print("Công việc phù hợp với bạn là: Android Developer")
    elif 2.56 <= value < 3.57:
        print("Công việc phù hợp với bạn là: iOS Developer")
    elif 3.57 <= value < 4.61:
        print("Công việc phù hợp với bạn là: IoT Developer")
    elif 4.61 <= value < 5.63:
        print("Công việc phù hợp với bạn là: DepOps Engineer")
    elif 5.63 <= value < 6.69:
        print("Công việc phù hợp với bạn là: Business Analyst")
    elif 6.69 <= value < 7.76:
        print("Công việc phù hợp với bạn là: UI/UX Designer")
    elif 7.76 <= value < 8.85:
        print("Công việc phù hợp với bạn là: Tester")
    elif 8.85 <= value < 10:
        print("Công việc phù hợp với bạn là: AI Engineer")
    elif 10 <= value < 11.13:
        print("Công việc phù hợp với bạn là: AI Researcher")
    elif 11.13 <= value < 12.25:
        print("Công việc phù hợp với bạn là: Data Analysis")
    elif 12.25 <= value < 13.30:
        print("Công việc phù hợp với bạn là: Database Administrator")
    elif 13.30 <= value < 14.30:
        print("Công việc phù hợp với bạn là: Data Engineer")
    elif 14.30 <= value < 15.30:
        print("Công việc phù hợp với bạn là: Data Scientist")
    elif 15.30 <= value < 16.40:
        print("Công việc phù hợp với bạn là: Information security analyst")
    elif 16.40 <= value < 17.45:
        print("Công việc phù hợp với bạn là: Network Security Specialist")
    elif 17.45 <= value < 18.45:
        print("Công việc phù hợp với bạn là: IT Security Engineer")
    elif 18.45 <= value < 19.45:
        print("Công việc phù hợp với bạn là: Game Developer")
    elif value >= 19.45:
        print("Công việc phù hợp với bạn là: IT - Helpdesk")
    else:
        print("Không tìm thấy việc phù hợp")
except Exception as e:
    print("Không tìm thấy việc phù hợp")

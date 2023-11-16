from rules import *

system_rule = SystemRule()
job_prediction = system_rule.job_prediction
user_choice = []


class ChatBoxQuestion:
    # Câu 1: Hỏi về lập trình
    def first_question(self):
        print("---> Bạn có biết lập trình không?")
        print("0: Không")
        print("1: Có")
        while True:
            user_input = int(input("Nhập số từ 0 - 1 để trả lời:\n"))
            if user_input == 0:
                user_choice.append("Không biết lập trình")
                job_prediction.input["Code Knowledge Field"] = 0
                job_prediction.input["Language Field"] = 10
                job_prediction.input["Ide Field"] = 12
                break
            elif user_input == 1:
                user_choice.append("Biết lập trình")
                job_prediction.input["Code Knowledge Field"] = 1
                break
            else:
                print("Vui lòng nhập lại từ 0 - 1:\n")

    # Câu 2: Mức lương mong muốn
    def second_question(self):
        print("---> Bạn mong muốn nhận mức lương bao nhiêu?")
        print("0: 0 - 5 (triệu VNĐ/ tháng)")
        print("1: 6 - 12 (triệu VNĐ/ tháng)")
        print("2: 13 - 20(triệu VNĐ/ tháng)")
        print("3: 20 - 30 (triệu VNĐ/ tháng)")
        print("4: Hơn 30 (triệu VNĐ/ tháng)")
        while True:
            user_input = int(input("Nhập số từ 0 - 4 để trả lời:\n"))

            if user_input == 0:
                user_choice.append("0 - 5 (triệu VNĐ/ tháng)")
                job_prediction.input["Salary Field"] = 0
                break
            elif user_input == 1:
                user_choice.append("6 - 12 (triệu VNĐ/ tháng)")
                job_prediction.input["Salary Field"] = 1
                break
            elif user_input == 2:
                user_choice.append("13 - 20 (triệu VNĐ/ tháng)")
                job_prediction.input["Salary Field"] = 2
                break
            elif user_input == 3:
                user_choice.append("20 - 30 (triệu VNĐ/ tháng)")
                job_prediction.input["Salary Field"] = 3
                break
            elif user_input == 4:
                user_choice.append("Hơn 30 (triệu VNĐ/ tháng)")
                job_prediction.input["Salary Field"] = 4
                break
            else:
                print("Vui lòng nhập lại từ 0 - 4:\n")

    # Câu 3: Lĩnh vực làm việc
    def third_question(self):
        print("---> Bạn mong muốn làm việc trong lĩnh vực nào?")
        print("0: Công nghệ phần mềm")
        print("1: An toàn thông tin")
        print("2: Khoa học dữ liệu")
        print("3: Trí tuệ nhân tạo")
        print("4: IT - Phần cứng")
        print("5: Game")
        while True:
            user_input = int(input("Nhập số từ 0 - 5 để trả lời:\n"))
            if user_input == 0:
                user_choice.append("Công nghệ phần mềm")
                job_prediction.input["Specialized Field"] = 0
                job_prediction.input["Network Field"] = 0
                job_prediction.input["Security Field"] = 0
                job_prediction.input["Math Field"] = 0
                job_prediction.input["Office Information Field"] = 0
                job_prediction.input["OWASP Top 10 Field"] = 0
                job_prediction.input["Operate Field"] = 7
                break
            elif user_input == 1:
                user_choice.append("An toàn thông tin")
                job_prediction.input["Specialized Field"] = 1
                job_prediction.input["Cloud Field"] = 0
                job_prediction.input["CI/CD Field"] = 0
                job_prediction.input["Math Field"] = 0
                job_prediction.input["Database Field"] = 0
                job_prediction.input["UI/UX Field"] = 0
                job_prediction.input["Ide Field"] = 12
                job_prediction.input["Tools Field"] = 8
                job_prediction.input["Language Field"] = 0
                job_prediction.input["SQL Field"] = 0
                break
            elif user_input == 2:
                user_choice.append("Khoa học dữ liệu")
                job_prediction.input["Specialized Field"] = 2
                job_prediction.input["Network Field"] = 0
                job_prediction.input["CI/CD Field"] = 0
                job_prediction.input["Security Field"] = 0
                job_prediction.input["OWASP Top 10 Field"] = 0
                job_prediction.input["Tools Field"] = 8
                job_prediction.input["UI/UX Field"] = 0
                break
            elif user_input == 3:
                user_choice.append("Trí tuệ nhân tạo")
                job_prediction.input["Specialized Field"] = 3
                job_prediction.input["Network Field"] = 0
                job_prediction.input["Security Field"] = 0
                job_prediction.input["UI/UX Field"] = 0
                job_prediction.input["CI/CD Field"] = 0
                job_prediction.input["Tools Field"] = 8
                job_prediction.input["Office Information Field"] = 0
                job_prediction.input["OWASP Top 10 Field"] = 0
                job_prediction.input["Operate Field"] = 7
                break
            elif user_input == 4:
                user_choice.append("IT - Phần cứng")
                job_prediction.input["Specialized Field"] = 4
                job_prediction.input["CI/CD Field"] = 0
                job_prediction.input["UI/UX Field"] = 0
                job_prediction.input["Cloud Field"] = 0
                job_prediction.input["Language Field"] = 0
                job_prediction.input["Ide Field"] = 0
                job_prediction.input["Database Field"] = 0
                job_prediction.input["Tools Field"] = 0
                job_prediction.input["Math Field"] = 0
                job_prediction.input["OWASP Top 10 Field"] = 0
                job_prediction.input["SQL Field"] = 0
                break
            elif user_input == 5:
                user_choice.append("Game")
                job_prediction.input["Specialized Field"] = 5
                job_prediction.input["Network Field"] = 0
                job_prediction.input["CI/CD Field"] = 0
                job_prediction.input["Office Information Field"] = 0
                job_prediction.input["Security Field"] = 0
                job_prediction.input["OWASP Top 10 Field"] = 0
                job_prediction.input["Tools Field"] = 8
                job_prediction.input["Math Field"] = 0
                job_prediction.input["Skills Field"] = 7
                job_prediction.input["Cloud Field"] = 0
                break
            else:
                print("Vui lòng nhập lại từ 0 - 5:\n")

    # Câu 4: Ngôn ngữ lập trình
    def fourth_question(self):
        print(
            "---> Bạn đã từng sử dụng dụng những ngôn ngữ lập trình nào(chọn ngôn ngữ bạn thành thạo nhất hoặc ngôn ngữ bạn dự định học)?"
        )
        print("0: Java")
        print("1: Python")
        print("2: Javascript")
        print("3: C/C++")
        print("4: Swift")
        print("5: Rust")
        print("6: Kotlin")
        print("7: C#")
        print("8: PHP")
        print("9: Unity")
        while True:
            user_input = int(input("Nhập số từ 0 - 9 để trả lời:\n"))

            if user_input == 0:
                user_choice.append("Ngôn ngữ lập trình: Java")
                job_prediction.input["Language Field"] = 0
                break
            elif user_input == 1:
                user_choice.append("Ngôn ngữ lập trình: Python")
                job_prediction.input["Language Field"] = 1
                break
            elif user_input == 2:
                user_choice.append("Ngôn ngữ lập trình: Javascript")
                job_prediction.input["Language Field"] = 2
                break
            elif user_input == 3:
                user_choice.append("Ngôn ngữ lập trình: C/C++")
                job_prediction.input["Language Field"] = 3
                break
            elif user_input == 4:
                user_choice.append("Ngôn ngữ lập trình: Swift")
                job_prediction.input["Language Field"] = 4
                break
            elif user_input == 5:
                user_choice.append("Ngôn ngữ lập trình: Rust")
                job_prediction.input["Language Field"] = 5
                break
            elif user_input == 6:
                user_choice.append("Ngôn ngữ lập trình: Kotlin")
                job_prediction.input["Language Field"] = 6
                break
            elif user_input == 7:
                user_choice.append("Ngôn ngữ lập trình: C#")
                job_prediction.input["Language Field"] = 7
                break
            elif user_input == 8:
                user_choice.append("Ngôn ngữ lập trình: PHP")
                job_prediction.input["Language Field"] = 8
                break
            elif user_input == 9:
                user_choice.append("Ngôn ngữ lập trình: Unity")
                job_prediction.input["Language Field"] = 9
                break
            else:
                print("Vui lòng nhập lại từ 0 - 9:\n")

    # Câu 5: IDE
    def fifth_question(self):
        print(
            "---> Bạn hay dùng IDE nào để code(nếu không có hãy chọn các IDE có chức năng tương tự như IDE bạn đang dùng hoặc IDe bạn dự định sẽ dùng)?"
        )
        print("0: Eclipse")
        print("1: PyCharm")
        print("2: Vscode")
        print("3: Unity")
        print("4: Android Studio")
        print("5: XCode")
        print("6: IntelliJ IDEA")
        print("7: Arduino")
        print("8: IAR Embedded Workbench")
        print("9: RStudio")
        print("10: Jupyter Notebook")
        print("11: Unreal Engine")
        while True:
            user_input = int(input("Nhập số từ 0 - 11 để trả lời:\n"))

            if user_input == 0:
                user_choice.append("IDE: Eclipse")
                job_prediction.input["Ide Field"] = 0
                break
            elif user_input == 1:
                user_choice.append("IDE: PyCharm")
                job_prediction.input["Ide Field"] = 1
                break
            elif user_input == 2:
                user_choice.append("IDE: Vscode")
                job_prediction.input["Ide Field"] = 2
                break
            elif user_input == 3:
                user_choice.append("IDE: Unity")
                job_prediction.input["Ide Field"] = 3
                break
            elif user_input == 4:
                user_choice.append("IDE: Android Studio")
                job_prediction.input["Ide Field"] = 4
                break
            elif user_input == 5:
                user_choice.append("IDE: XCode")
                job_prediction.input["Ide Field"] = 5
                break
            elif user_input == 6:
                user_choice.append("IDE: IntelliJ IDEA")
                job_prediction.input["Ide Field"] = 6
                break
            elif user_input == 7:
                user_choice.append("IDE: Arduino")
                job_prediction.input["Ide Field"] = 7
                break
            elif user_input == 8:
                user_choice.append("IDE: IAR Embedded Workbench")
                job_prediction.input["Ide Field"] = 8
                break
            elif user_input == 9:
                user_choice.append("IDE: RStudio")
                job_prediction.input["Ide Field"] = 9
                break
            elif user_input == 10:
                user_choice.append("IDE: Jupyter Notebook")
                job_prediction.input["Ide Field"] = 10
                break
            elif user_input == 11:
                user_choice.append("IDE: Unreal Engine")
                job_prediction.input["Ide Field"] = 11
                break
            else:
                print("Vui lòng nhập lại từ 0 - 11:\n")

    # Caau 6: Tools
    def sixth_question(self):
        print(
            "---> Bạn biết sử dụng công cụ nào sau đây(nếu không có hãy chọn các tools có chức năng tương tự như IDE bạn đang dùng)?"
        )
        print("0: Microsoft Visio")
        print("1: Selenium")
        print("2: Test complete")
        print("3: TestingWhiz")
        print("4: Figma")
        print("5: Adobe Photoshop")
        print("6: Power PI")
        print("7: SIEM")
        print("8: Tôi không dùng")
        while True:
            user_input = int(input("Nhập số từ 0 - 8 để trả lời:\n"))

            if user_input == 0:
                user_choice.append("Tools: Microsoft Visio")
                job_prediction.input["Tools Field"] = 0
                break
            elif user_input == 1:
                user_choice.append("Tools: Selenium")
                job_prediction.input["Tools Field"] = 1
                break
            elif user_input == 2:
                user_choice.append("Tools: Test complete")
                job_prediction.input["Tools Field"] = 2
                break
            elif user_input == 3:
                user_choice.append("Tools: TestingWhiz")
                job_prediction.input["Tools Field"] = 3
                break
            elif user_input == 4:
                user_choice.append("Tools: Figma")
                job_prediction.input["Tools Field"] = 4
                break
            elif user_input == 5:
                user_choice.append("Tools: Adobe Photoshop")
                job_prediction.input["Tools Field"] = 5
                break
            elif user_input == 6:
                user_choice.append("Tools: Power PI")
                job_prediction.input["Tools Field"] = 6
                break
            elif user_input == 7:
                user_choice.append("Tools: SIEM")
                job_prediction.input["Tools Field"] = 7
                break
            elif user_input == 8:
                user_choice.append("Tools: UnKnown")
                job_prediction.input["Tools Field"] = 8
                break
            else:
                print("Vui lòng nhập lại từ 0 - 8:\n")

    # Câu 7: Tin học văn phòng
    def seventh_question(self):
        print("---> Bạn biết sử dụng các công cụ như: Word, Excel, PP không?")
        print("0: Không")
        print("1: Có")
        while True:
            user_input = int(input("Nhập số từ 0 - 1 để trả lời:\n"))

            if user_input == 0:
                user_choice.append("Office Information: No")
                job_prediction.input["Office Information Field"] = 0
                break
            elif user_input == 1:
                user_choice.append("Office Information: Yes")
                job_prediction.input["Office Information Field"] = 1
                break
            else:
                print("Vui lòng nhập lại từ 0 - 1:\n")

    # Câu 8: SQL
    def eighth_question(self):
        print("---> Bạn có các kiến thức về SQL không?")
        print("0: Không")
        print("1: Có")
        while True:
            user_input = int(input("Nhập số từ 0 - 1 để trả lời:\n"))

            if user_input == 0:
                user_choice.append("SQL: No")
                job_prediction.input["SQL Field"] = 0
                break
            elif user_input == 1:
                user_choice.append("SQL: Yes")
                job_prediction.input["SQL Field"] = 1
                break
            else:
                print("Vui lòng nhập lại từ 0 - 1:\n")

    # Câu 9: UI/UX
    def ninth_question(self):
        print("---> Bạn có hiểu biết về UI/UX không?")
        print("0: Không")
        print("1: Có")
        while True:
            user_input = int(input("Nhập số từ 0 - 1 để trả lời:\n"))

            if user_input == 0:
                user_choice.append("UI/UX : No")
                job_prediction.input["UI/UX Field"] = 0
                break
            elif user_input == 1:
                user_choice.append("UI/UX : Yes")
                job_prediction.input["UI/UX Field"] = 1
                break
            else:
                print("Vui lòng nhập lại từ 0 - 1:\n")

    # Câu 10: Toán
    def tenth_question(self):
        print(
            "---> Bạn nắm chắc các kiến thức về xác suất thống kê, ma trận, đại số,... không?"
        )
        print("0: Không")
        print("1: Có")
        while True:
            user_input = int(input("Nhập số từ 0 - 1 để trả lời:\n"))

            if user_input == 0:
                user_choice.append("Math Field : No")
                job_prediction.input["Math Field"] = 0
                break
            elif user_input == 1:
                user_choice.append("Math Field : Yes")
                job_prediction.input["Math Field"] = 1
                break
            else:
                print("Vui lòng nhập lại từ 0 - 1:\n")

    # Câu 11: Machine Learning
    def eleventh_question(self):
        print("---> Bạn có kiến thức về Machine Learning, Deep Learning không?")
        print("0: Không")
        print("1: Có")
        while True:
            user_input = int(input("Nhập số từ 0 - 1 để trả lời:\n"))

            if user_input == 0:
                user_choice.append("Machine Learning : No")
                job_prediction.input["Skills Field"] = 7
                break
            elif user_input == 1:
                user_choice.append("Machine Learning : Yes")
                job_prediction.input["Skills Field"] = 3
                break
            else:
                print("Vui lòng nhập lại từ 0 - 1:\n")

    # Câu 12: Protocol
    def twelfth_question(self):
        print("---> Bạn có các kiến thức về hạ tầng mạng, các giao thức không?")
        print("0: Không")
        print("1: Có")
        while True:
            user_input = int(input("Nhập số từ 0 - 1 để trả lời:\n"))

            if user_input == 0:
                user_choice.append("Tầng mang, Giao thức : No")
                job_prediction.input["Skills Field"] = 7
                break
            elif user_input == 1:
                user_choice.append("Tầng mang, Giao thức : Yes")
                job_prediction.input["Skills Field"] = 5
                break
            else:
                print("Vui lòng nhập lại từ 0 - 1:\n")

    # Câu 13: Cloud
    def thirdteen_question(self):
        print(
            "---> Bạn có khả năng làm việc với các dịch vụ cloud như:Azure, AWS Cloud,.. không?"
        )
        print("0: Không")
        print("1: Có")
        while True:
            user_input = int(input("Nhập số từ 0 - 1 để trả lời:\n"))

            if user_input == 0:
                user_choice.append("Cloud : No")
                job_prediction.input["Cloud Field"] = 0
                break
            elif user_input == 1:
                user_choice.append("Cloud : Yes")
                job_prediction.input["Cloud Field"] = 1
                break
            else:
                print("Vui lòng nhập lại từ 0 - 1:\n")

    # Câu 14: Network
    def fourthteen_question(self):
        print("---> Bạn có hiểu biết về Network: LAN, WAN,... không?")
        print("0: Không")
        print("1: Có")
        while True:
            user_input = int(input("Nhập số từ 0 - 1 để trả lời:\n"))

            if user_input == 0:
                user_choice.append("Network : No")
                job_prediction.input["Network Field"] = 0
                break
            elif user_input == 1:
                user_choice.append("Network : Yes")
                job_prediction.input["Network Field"] = 1
                break
            else:
                print("Vui lòng nhập lại từ 0 - 1:\n")

    # Câu 15: Security
    def fifteen_question(self):
        print(
            "---> Bạn có kinh nghiệm trong việc xây dựng và triển khai kế hoạch phản ứng khi có sự cố an ninh không?"
        )
        print("0: Không")
        print("1: Có")
        while True:
            user_input = int(input("Nhập số từ 0 - 1 để trả lời:\n"))

            if user_input == 0:
                user_choice.append("Security : No")
                job_prediction.input["Security Field"] = 0
                break
            elif user_input == 1:
                user_choice.append("Security : Yes")
                job_prediction.input["Security Field"] = 1
                break
            else:
                print("Vui lòng nhập lại từ 0 - 1:\n")

    # Câu 16: Database
    def sixteen_question(self):
        print(
            "---> Bạn biết sử dụng hệ cơ sở dữ liệu nào sau đây(chọn hệ cơ sở dữ liệu bạn thành thạo nhất)?"
        )
        print("0: SQL Server")
        print("1: MySQL")
        print("2: MongoDB")
        print("3: Oracle Database")
        print("4: PostgreSQL")
        print("5: Redis")
        print("6: Tôi không biết sử dụng")
        while True:
            user_input = int(input("Nhập số từ 0 - 6 để trả lời:\n"))

            if user_input == 0:
                user_choice.append("Database : SQL Server")
                job_prediction.input["Database Field"] = 0
                break
            elif user_input == 1:
                user_choice.append("Database : MySQL")
                job_prediction.input["Database Field"] = 1
                break
            elif user_input == 2:
                user_choice.append("Database : MongoDB")
                job_prediction.input["Database Field"] = 2
                break
            elif user_input == 3:
                user_choice.append("Database : Oracle Database")
                job_prediction.input["Database Field"] = 3
                break
            elif user_input == 4:
                user_choice.append("Database : PostgreSQL")
                job_prediction.input["Database Field"] = 4
                break
            elif user_input == 5:
                user_choice.append("Database : Redis")
                job_prediction.input["Database Field"] = 5
                break
            elif user_input == 6:
                user_choice.append("Database : UnKnown")
                job_prediction.input["Database Field"] = 6
                break
            else:
                print("Vui lòng nhập lại từ 0 - 6:\n")

    # Câu 17: CI/CD
    def eleventeen_question(self):
        print("---> Bạn có hiểu biết về quy trình triển khai CI/CD không?")
        print("0: Không")
        print("1: Có")
        while True:
            user_input = int(input("Nhập số từ 0 - 1 để trả lời:\n"))

            if user_input == 0:
                user_choice.append("CI/CD : No")
                job_prediction.input["CI/CD Field"] = 0
                break
            elif user_input == 1:
                user_choice.append("CI/CD : Yes")
                job_prediction.input["CI/CD Field"] = 1
                break
            else:
                print("Vui lòng nhập lại từ 0 - 1:\n")

    # Câu 18: Ops
    def eightteen_question(self):
        print(
            "---> Bạn đã từng làm việc với Docker, Kubernetes, Jenkins,... bao giờ chưa?"
        )
        print("0: Không")
        print("1: Có")
        while True:
            user_input = int(input("Nhập số từ 0 - 1 để trả lời:\n"))

            if user_input == 0:
                user_choice.append("Ops : No")
                job_prediction.input["Skills Field"] = 7
                break
            elif user_input == 1:
                user_choice.append("Ops : Yes")
                job_prediction.input["Skills Field"] = 2
                break
            else:
                print("Vui lòng nhập lại từ 0 - 1:\n")

    # Câu 19: Kinh tế
    def ninteen_question(self):
        print(
            "---> Bạn có các kiến thức về các ngành khác ngoài công nghệ thông tin không?(ví dụ: marketing, thương mại điển tử,....)"
        )
        print("0: Không")
        print("1: Có")
        while True:
            user_input = int(input("Nhập số từ 0 - 1 để trả lời:\n"))

            if user_input == 0:
                user_choice.append("Economy : No")
                job_prediction.input["Skills Field"] = 7
                break
            elif user_input == 1:
                user_choice.append("Economy : Yes")
                job_prediction.input["Skills Field"] = 4
                break
            else:
                print("Vui lòng nhập lại từ 0 - 1:\n")

    # Câu 20: SIEM
    def twenty_question(self):
        print(
            "---> Bạn có hiểu biết về SIEM(Security Information and Event Management) không?"
        )
        print("0: Không")
        print("1: Có")
        while True:
            user_input = int(input("Nhập số từ 0 - 1 để trả lời:\n"))

            if user_input == 0:
                user_choice.append("SIEM : No")
                job_prediction.input["Tools Field"] = 8
                break
            elif user_input == 1:
                user_choice.append("SIEM : Yes")
                job_prediction.input["Tools Field"] = 7
                break
            else:
                print("Vui lòng nhập lại từ 0 - 1:\n")

    # Câu 21: OWASP
    def twenty_one_question(self):
        print(
            "---> Bạn có hiểu biết về OWASP Top 10 và các kỹ thuật bảo vệ ứng dụng web không?"
        )
        print("0: Không")
        print("1: Có")
        while True:
            user_input = int(input("Nhập số từ 0 - 1 để trả lời:\n"))

            if user_input == 0:
                user_choice.append("OWASP : No")
                job_prediction.input["OWASP Top 10 Field"] = 0
                break
            elif user_input == 1:
                user_choice.append("OWASP : Yes")
                job_prediction.input["OWASP Top 10 Field"] = 1
                break
            else:
                print("Vui lòng nhập lại từ 0 - 1:\n")

    # Câu 22: Operate
    def twenty_two_question(self):
        print(
            "---> Bạn có hiểu biết về các hệ điều hành như Linux, MacOs, Ubuntu,... không?"
        )
        print("0: Không")
        print("1: Có")
        while True:
            user_input = int(input("Nhập số từ 0 - 1 để trả lời:\n"))

            if user_input == 0:
                user_choice.append("Operate : No")
                job_prediction.input["Operate Field"] = 7
                break
            elif user_input == 1:
                user_choice.append("Operate : Yes")
                job_prediction.input["Operate Field"] = 6
                break
            else:
                print("Vui lòng nhập lại từ 0 - 1:\n")

# Input:
# - menu_choice: lựa chọn chức năng từ 1-7
# - account_id: mã sổ tiết kiệm (str)
# - customer_name: tên khách hàng (str)
# - balance: số tiền gửi (int)
# - term_months: kỳ hạn gửi (int)
# - interest_rate: lãi suất năm (float)
# - actual_months: số tháng thực gửi (int)

# Output:
# - Danh sách sổ tiết kiệm
# - Thông báo mở sổ, cập nhật, tất toán thành công
# - Tiền lãi dự kiến và tổng tiền nhận
# - Kết quả kiểm tra rút trước hạn
# - Các thông báo lỗi khi dữ liệu không hợp lệ

# Giải pháp:
# - Dùng list chứa dictionary để lưu thông tin sổ tiết kiệm
# - Dùng strip() và upper() để chuẩn hóa mã sổ
# - Kiểm tra trùng mã sổ trước khi thêm mới
# - Dùng isdigit() để kiểm tra số tiền gửi và kỳ hạn
# - Dùng try-except để kiểm tra lãi suất dạng số thực
# - Chỉ cho phép thao tác với sổ có trạng thái active
# - Khi tất toán chỉ cập nhật trạng thái thành closed
# - Tính lãi theo công thức yêu cầu của đề bài
# - Kiểm tra điều kiện rút trước hạn theo số tháng thực gửi

# Thuật toán:
# - Hiển thị menu
# - Nhận lựa chọn người dùng
# - Thực hiện chức năng tương ứng
# - Kiểm tra dữ liệu đầu vào
# - Cập nhật danh sách sổ tiết kiệm
# - Quay lại menu cho đến khi chọn thoát

saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")

    menu_choice = input("Nhập lựa chọn của bạn: ").strip()

    if menu_choice == "1":
        if len(saving_accounts) == 0:
            print("Danh sách sổ tiết kiệm hiện đang trống")
        else:
            print("\nDanh sách sổ tiết kiệm:")

            for index, account in enumerate(saving_accounts, start=1):
                print(
                    f"{index}. Mã sổ: {account['account_id']} | "
                    f"Khách hàng: {account['customer_name']} | "
                    f"Số tiền gửi: {account['balance']} | "
                    f"Kỳ hạn: {account['term_months']} tháng | "
                    f"Lãi suất: {account['interest_rate']}%/năm | "
                    f"Trạng thái: {account['status']}"
                )

    elif menu_choice == "2":
        account_id = input(
            "Nhập mã sổ tiết kiệm: "
        ).strip().upper()

        customer_name = input(
            "Nhập tên khách hàng: "
        ).strip()

        if customer_name == "":
            print("Tên khách hàng không được để trống")
            continue

        duplicate = False

        for account in saving_accounts:
            if account["account_id"] == account_id:
                duplicate = True
                break

        if duplicate:
            print("Mã sổ tiết kiệm đã tồn tại!")
            continue

        balance_input = input(
            "Nhập số tiền gửi: "
        ).strip()

        term_input = input(
            "Nhập kỳ hạn gửi theo tháng: "
        ).strip()

        if (
            not balance_input.isdigit()
            or not term_input.isdigit()
            or int(balance_input) <= 0
            or int(term_input) <= 0
        ):
            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
            continue

        rate_input = input(
            "Nhập lãi suất năm: "
        ).strip()

        try:
            interest_rate = float(rate_input)

            if interest_rate <= 0:
                print("Lãi suất không hợp lệ!")
                continue

        except ValueError:
            print("Lãi suất không hợp lệ!")
            continue

        saving_accounts.append({
            "account_id": account_id,
            "customer_name": customer_name,
            "balance": int(balance_input),
            "term_months": int(term_input),
            "interest_rate": interest_rate,
            "status": "active"
        })

        print("Mở sổ tiết kiệm thành công")

    elif menu_choice == "3":
        account_id = input(
            "Nhập mã sổ tiết kiệm cần cập nhật: "
        ).strip().upper()

        found = False

        for account in saving_accounts:
            if account["account_id"] == account_id:
                found = True

                if account["status"] == "closed":
                    print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
                    break

                customer_name = input(
                    "Nhập tên khách hàng mới: "
                ).strip()

                if customer_name == "":
                    print("Tên khách hàng không được để trống")
                    break

                balance_input = input(
                    "Nhập số tiền gửi mới: "
                ).strip()

                term_input = input(
                    "Nhập kỳ hạn mới theo tháng: "
                ).strip()

                if (
                    not balance_input.isdigit()
                    or not term_input.isdigit()
                    or int(balance_input) <= 0
                    or int(term_input) <= 0
                ):
                    print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                    break

                rate_input = input(
                    "Nhập lãi suất năm mới: "
                ).strip()

                try:
                    interest_rate = float(rate_input)

                    if interest_rate <= 0:
                        print("Lãi suất không hợp lệ!")
                        break

                except ValueError:
                    print("Lãi suất không hợp lệ!")
                    break

                account["customer_name"] = customer_name
                account["balance"] = int(balance_input)
                account["term_months"] = int(term_input)
                account["interest_rate"] = interest_rate

                print("Cập nhật sổ tiết kiệm thành công")
                break

        if not found:
            print("Không tìm thấy mã sổ tiết kiệm!")

    elif menu_choice == "4":
        account_id = input(
            "Nhập mã sổ tiết kiệm cần tất toán/xóa: "
        ).strip().upper()

        found = False

        for account in saving_accounts:
            if account["account_id"] == account_id:
                found = True

                account["status"] = "closed"

                print("Tất toán sổ tiết kiệm thành công")
                break

        if not found:
            print("Không tìm thấy mã sổ tiết kiệm")

    elif menu_choice == "5":
        account_id = input(
            "Nhập mã sổ tiết kiệm cần tính lãi: "
        ).strip().upper()

        found = False

        for account in saving_accounts:
            if account["account_id"] == account_id:
                found = True

                if account["status"] == "closed":
                    print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                    break

                interest = (
                    account["balance"]
                    * account["interest_rate"]
                    / 100
                    * account["term_months"]
                    / 12
                )

                total_amount = (
                    account["balance"] + interest
                )

                print(f"Tiền lãi dự kiến: {interest:,.0f}")
                print(f"Tổng tiền nhận: {total_amount:,.0f}")
                break

        if not found:
            print("Không tìm thấy mã sổ tiết kiệm")

    elif menu_choice == "6":
        account_id = input(
            "Nhập mã sổ tiết kiệm cần kiểm tra: "
        ).strip().upper()

        found = False

        for account in saving_accounts:
            if account["account_id"] == account_id:
                found = True

                if account["status"] == "closed":
                    print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                    break

                actual_months_input = input(
                    "Nhập số tháng thực gửi: "
                ).strip()

                if (
                    not actual_months_input.isdigit()
                    or int(actual_months_input) <= 0
                ):
                    print("Số tháng thực gửi không hợp lệ!")
                    break

                actual_months = int(actual_months_input)

                if actual_months < account["term_months"]:
                    applied_rate = 0.5
                    print("Khách hàng rút trước hạn")
                else:
                    applied_rate = account["interest_rate"]
                    print("Khách hàng đủ điều kiện hưởng lãi đúng hạn")

                interest = (
                    account["balance"]
                    * applied_rate
                    / 100
                    * actual_months
                    / 12
                )

                total_amount = (
                    account["balance"] + interest
                )

                print(f"Tiền lãi thực nhận: {interest:,.0f}")
                print(f"Tổng tiền thực nhận: {total_amount:,.0f}")
                break

        if not found:
            print("Không tìm thấy mã sổ tiết kiệm")

    elif menu_choice == "7":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại")
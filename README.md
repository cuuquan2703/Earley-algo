---
Họ và tên: Đặng Huỳnh Cửu Quân
MSSV: 20120354
---

# Ghi chú

- Earley3.py là một mã nguồn độc lập dành cho thuật toán Earley3 trên github của Tomer Filiba
- Source đã được cài đặt sẵn vào folder
- Link source code: [https://github.com/tomerfiliba/tau/blob/master/earley3.py](https://github.com/tomerfiliba/tau/blob/master/earley3.py)

# Hướng dẫn

- Tạo text và Rule trong file Earley_test.py
- Cách tạo Rule:
  - Khởi tạo class `Rule` truyền vào tham số đầu là tên Rule, các tham số sau là production của rule đó
    VD: S -> NP PP; S -> VP
    -> Khởi tạo Rule
    ```python
      S = Rule("S",Production(NP),Production(PP),Production(VP))
    ```
  - Nên khởi tạo các Rule độc lập trước ( không có phụ thuộc vào Rule khác ) mới có thể khởi tạo các Rule khác nhờ vào method `add` của class `Rule`
- Gọi hàm `parse()` với hai tham số:
  - Rule gốc: S;
  - Text
- Hàm `build_tree` phục vụ cho việc tạo cây

# Debug.txt

- Để thuận tiện trong quá trình tìm hiểu thuật toán, em có print ra đẻ debug xem từng bước làm
- Nhận thấy sự cần thiết nên em đã để tạo 1 file Debug.txt để theo dõi quá trình handle thuật toán
- Trong đó [Predict, Scan, Compete] để chỉ các bước tương ứng trong thuật toán Earley
- Các biến có ngoặc nhọn {value} thể hiện các tham số cho các hàm `Predict`, `Scan`, và `Complete`
  - {col} để chỉ column hiện tại
  - {state} state hiện tại đang xét của column đó
  - {rule} tên rule

# Tài liệu tham khảo:

- [Earley Parser - Wikipedia](https://en.wikipedia.org/wiki/Earley_parser)
- [Earley algorithm - University of Washington](https://courses.washington.edu/ling571/ling571_fall_2010/slides/parsing_earley.pdf)
- [Earley3.py](https://github.com/tomerfiliba/tau/blob/master/earley3.py)

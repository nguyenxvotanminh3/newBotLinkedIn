# Bot_Pthon_LinkeIN
# Tool linkedin
``````
Download project về máy
``````
Chuẩn bị 

(Lưu ý trong thư mục Content.csv chỉ dùng row 0 vì set mặc định như thế, chưa chỉnh sửa để chọn row theo ý thích )
``````
1.Một tấm ảnh đặt tên chữ tiếng anh, không bắt đầu bằng 't' , ví dụ : test ( lỗi ) , nên đặt theo pic1 , pic2, pic3
``````
``````
2.Lưu ảnh vào máy, lấy đường dẫn chính xác đến ảnh. Ví dụ ảnh ở ổ D thư mục 'code' tên anh 'pic1' thì lấy dường đãn là 'D:\code\pic1.jpg'
``````
``````
3.Vào thư mục recouses -> Content.csv paste link ảnh
``````
 ![image](https://github.com/nguyenxvotanminh3/newBotLinkedIn/assets/91356207/add679e5-b3e9-4821-a5de-15514ac774ee)

 ``````
Lưu ý nếu bạn dùng pycham làm ide thì sẽ dễ chỉnh sửa hơn
``````
``````
-chọn vào kiểu dữ liệu data
``````
![image](https://github.com/nguyenxvotanminh3/newBotLinkedIn/assets/91356207/6c74ff36-155b-41c1-b7cc-4d560733c976)
``````
-tìm đến cột Imgae và paste link ảnh
``````
![image](https://github.com/nguyenxvotanminh3/newBotLinkedIn/assets/91356207/f02bfcc4-33fe-4a6c-a9e3-f1f690ddeeaa)

``````
4.Nếu bạn muốn chỉnh sửa tag cũng được, cú pháp viết tên tag như sau :  tên,tên,tên,tên ( cứ viết tên lên tên kế đó là phẩy, đừng để khoảng cách vì mình chưa test nếu có dấu cách thì sao)
5.Enter tất cả
6.Nếu muốn tự động điền tên đăng nhập và mật khẩu thì vào  recouses -> Account.cfg
``````
``````
7. Chỉnh sửa tên đăng nhập và mật khẩu , kệ api đi
``````
****![image](https://github.com/nguyenxvotanminh3/newBotLinkedIn/assets/91356207/b04dd191-e95b-4292-b4be-6032ed351954)

``````
*Lưu ý: dùng 1 tài khoản test mới , test chung 1 tài khoản dễ bị khóa, làm ơn đấy T_T
``````

# Chạy tools:

Hiện chưa có file .exe để chạy , nên test trong ide
``````
1. Mở ide
``````
``````
2. Chọn vào LinkedInToolUi.py
``````
![image](https://github.com/nguyenxvotanminh3/newBotLinkedIn/assets/91356207/003b999c-ecea-4d88-ad1b-d0a67613933f)

``````
3.Bấm chạy
``````
``````
4.Nó sẽ hiện 2 cửa sổ , 1 cửa sổ để login, 1 cửa sổ để post( hiện đang phát triển post theo row nên chưa cần phải điền chữ )
``````
![image](https://github.com/nguyenxvotanminh3/newBotLinkedIn/assets/91356207/d2024439-bb96-4286-af52-ec46dff8e3e0)
![image](https://github.com/nguyenxvotanminh3/newBotLinkedIn/assets/91356207/2f45877c-8dbd-4b0f-af04-91ede9b5c9c5)
``````
Basic login : tự lead đến trang đăng nhập, bạn chỉ cần tự đăng nhập
Auto login : chuyển bạn đến trang đăng nhập, tự điền mật khẩu, 1 vài lúc nó tự enter vào luôn, không thì bạn bấm enter vào trang chính.
5.Tắt cửa sổ đăng nhập cho gọn, sau đó chọn AutoPostLinkedIn , nó sẽ tự up ảnh, tag, và đăng content
** Lưu ý : Quan trọng thì nhắc 3 lần , file Content.vsc chỉ láy được row 0 , làm ơn hãy paste đúng vào row đó vì mình mới để mặc định row đó để test thôi, Xin cảm ơn bạn đã tin dùng!
``````

# Thoát
Nhấn vào nút "Quit"

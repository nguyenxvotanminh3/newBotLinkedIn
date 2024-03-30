# Bot_Pthon_LinkeIN
``````

Download project về máy
``````
#Phần 1 post : 


``````

1.Chuẩn bị một tấm ảnh đặt tên chữ tiếng anh, nên đặt theo pic1 , pic2, pic3
``````
``````
2.Lưu ảnh vào máy, lấy đường dẫn chính xác đến ảnh. Ví dụ ảnh ở ổ D thư mục 'code' tên anh 'pic1' thì lấy dường đãn là 'D:\code\pic1.jpg'
``````
``````
3.Vào thư mục dist -> recouses -> Content.csv
* Chọn mở bằng Excel hay 1 IDE như vscode đều được
``````
``````
4. paste vào cột Image
``````
![image](https://github.com/nguyenxvotanminh3/newBotLinkedIn/assets/91356207/108c974c-eaba-4bc3-837d-a5e9e90614dd)


``````
5.Nếu bạn muốn chỉnh sửa tag cũng được, cú pháp viết tên tag như sau :  tên,tên,tên,tên 
``````
![image](https://github.com/nguyenxvotanminh3/newBotLinkedIn/assets/91356207/7b4bc6fc-11a1-4baa-8855-89c28a0f8b0e)


``````
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


``````
1. Vào thư mục dist -> NewLkUi.exe
``````
![image](https://github.com/nguyenxvotanminh3/newBotLinkedIn/assets/91356207/0caee351-a081-4368-953a-b47ecaebba8b)


``````
2. Click vào NewLkUi.exe

``````

``````
3.Chờ 1 tí tí 
``````
``````
4.Nó sẽ hiện cửa sổ giao diện
``````
![image](https://github.com/nguyenxvotanminh3/newBotLinkedIn/assets/91356207/3589dd5e-86e9-4c4a-8da3-a69f0922478a)

``````
5.Bấm auto login để tự động đăng nhập ( Nếu nó tự điền mật khẩu nhưng không chuyển sang trang chủ thì bấm log in bằng tay ) 
``````

``````
6. Điền entryROw ( bắt đầu post từ đây ) và endRow ( Kết thúc ở đây )

``````
![image](https://github.com/nguyenxvotanminh3/newBotLinkedIn/assets/91356207/f0f24293-b216-4981-acaf-94b1301a86c2)


``````
7. Kiểm tra trên cửa sổ xem đúng không, nếu không đúng thì cứ nhập lại rồi bấm kiểm tra tiếp

``````

![image](https://github.com/nguyenxvotanminh3/newBotLinkedIn/assets/91356207/ad6283c1-1422-4479-8b16-c47194adf955)

``````
8. Chọn mode đăng bài

``````

![image](https://github.com/nguyenxvotanminh3/newBotLinkedIn/assets/91356207/78b875f2-39c1-4171-8fa4-c19c5a5d5375)

``````
9. Nếu dùng timer post , thì chọn thêm open input time 

``````
![image](https://github.com/nguyenxvotanminh3/newBotLinkedIn/assets/91356207/b4a1800b-a7a0-4900-8460-86b2ec30aad4)

![image](https://github.com/nguyenxvotanminh3/newBotLinkedIn/assets/91356207/a5ecab7b-c5e3-4f07-a34d-78bd4f842bb9)




``````

10. Bấm AutoPost

``````
![image](https://github.com/nguyenxvotanminh3/newBotLinkedIn/assets/91356207/389668fd-ca6c-401b-91ba-1d178b5df1cd)



``````

``````
# Phần 2 : Connect 

``````
1. Vào thư mục dist -> recourses -> mở file url_linkedin.csv
``````
![image](https://github.com/nguyenxvotanminh3/newBotLinkedIn/assets/91356207/7701acc9-f766-4738-bdab-e217f9315884)


``````
2.Cột LinkedIn_Link chứa link của người muốn connect , cột status chứa status 
``````

``````
3. Khi mới nhập link , mặc định để status là 1 chữ gì đó, ví dụ : null
``````
![image](https://github.com/nguyenxvotanminh3/newBotLinkedIn/assets/91356207/f5529b67-9ccc-4982-869c-fa4471ff294d)
``````
4. Lưu lại và tắt excel, sau đó bật phần mềm lên
``````
``````
5. Sau khi login, bấm auto connect và chờ
``````
![image](https://github.com/nguyenxvotanminh3/newBotLinkedIn/assets/91356207/bfc2e9ee-5a97-4ac6-90be-7bc669ca047b)

``````
5. Sau khi bot chạy xong, bật file url_linkedin.csv lên để kiểm tra
``````

``````
Sẽ có 4 trường hợp xảy ra trong Status :
1.Pending : Người connect đã được gửi connect và đang đợi được connect
2.Connected : Người connecti đã được gửi và đã connect ( Thường xuất hiện khi chạy để kiểm tra connect, lần đầu sẽ chỉ hiện pending ) 
3.Not connected : Lỗi connect hoặc vấn đề gì đó chưa được fix
4.Null : Link lỗi hoặc một lỗi khác
``````
# Thoát
Nhấn vào nút "X" để tắt tất cả
 

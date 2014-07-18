
Cài đặt wordpress từ xa bằng fabric trên Ubuntu:
================================================


Trước khi sử dụng :
------------------

**Giới thiệu qua về Fabric và Wordpress**<br>
  -Fabric là một thư viện và các câu lệnh được viết bằng python để giúp nhưng người quản trị có thể nhanh chóng thực hiện các task vụ thông qua ssh remote.<br>
  -ta có thể cài đặt fabric bằng lênh (ubuntu):<br>
  `sudo apt-get install fabric`<br>
  <br>
  -Wordpress là một framework của php gíup người dùng có thể tạp các blog đẹp và nhanh chóng .
  
**Giới thiệu bài Lab**<br>
  trong lab này sẽ hướng dẫn mọi người sử dụng Fabric để cài đặt từ xa wordpress framework.<br><br>
**Yêu Cầu các gói**<br>
> sudo apt-get install git
  
Bắt đầu Cài đặt
---------------
Trên Terminal lần lượt chạy các lệnh: 
  >  git clone https://github.com/bekeomut/Fabric-Wordpress<br>
  cd Fabric-Wordpress<br>
  fab deploy
  
  
sau khi chạy lệnh . nhập một số thông tin cần thiết trên terminal => done !

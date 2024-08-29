# Crawl-Data
Lấy dữ liệu xe ô tô trên trang web Sàn bốn bánh

Dữ liệu sau khi được crawl về sẽ lưu trong car.csv

File cleanningData.py dùng để lấy dữ liệu từ car.csv, làm sạch dữ liệu xong chuyển qua clean_car.csv

File ingestionTosql.py dùng để đưa dữ từ file clean_car.csv vào CSDL Mysql 

File crawl.bat được tạo ra để chạy tự động cho quá trình crawl dữ liệu

# Tạo task tự động chạy file .bat mỗi phút trên window
schtasks /create /tn "Run Batch File Every Minute" /tr "D:\C\Crawl_data\Crawl-Data\crawl.bat" /sc minute /mo 1 /f

schtasks /delete /tn "Run Batch File Every Minute" /f

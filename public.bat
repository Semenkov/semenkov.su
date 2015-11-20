pelican --ignore-cache -q -s pelican_public_conf.py
SET ftp_host=ftp.semenkov.1gb.ru
SET ftp_user=1gb_semenkov
SET ftp_pwd=8f47bef65rty
SET source_dir=D:\inetpub\wwwroot\semenkov_upload
ncftpput -R -u %ftp_user% -p %ftp_pwd%  %ftp_host% /http %source_dir%\*.*
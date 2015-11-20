pelican --ignore-cache -q -s pelican_public_conf.py
SET ftp_host=ftp.semenkov.1gb.ru
SET ftp_user=1gb_semenkov
SET ftp_pwd=8f47bef65rty
SET source_dir=C:\inetpub\wwwroot\semenkov_upload
ncftpput -u %ftp_user% -p %ftp_pwd%  %ftp_host% /http web.config
ncftpput -u %ftp_user% -p %ftp_pwd%  %ftp_host% /http %source_dir%\*.*
ncftpput -R -u %ftp_user% -p %ftp_pwd%  %ftp_host% /http/theme %source_dir%\theme\*.*
ncftpput -R -u %ftp_user% -p %ftp_pwd%  %ftp_host% /http/extra %source_dir%\extra\*.*
ncftpput -R -u %ftp_user% -p %ftp_pwd%  %ftp_host% /http/tag %source_dir%\tag\*.*
ncftpput -R -u %ftp_user% -p %ftp_pwd%  %ftp_host% /http/category %source_dir%\category\*.*	
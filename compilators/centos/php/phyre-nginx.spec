Name:           phyre-php
Version:        8.2
Release:        1%{?dist}
Summary:       Phyre PHP - Web server for PhyrePanel

License:       GPL
URL:    https://phyrepanel.com
Source0: https://nginx.org/download/nginx-1.25.5.tar.gz
Source1: logrotate
Source2: nginx.conf
Source3: nginx.default.conf
Source4: nginx.service
Source5: nginx.upgrade.sh
Source6: nginx.suse.logrotate
Source7: nginx-debug.service
Source8: nginx.copyright
Source9: nginx.check-reload.sh

%description
Phyre Nginx is a web server for PhyrePanel.

%prep
# we have no source, so nothing here

%build
tar -xzf $RPM_SOURCE_DIR/nginx-1.25.5.tar.gz -C $RPM_BUILD_DIR
cd nginx-1.25.5
./configure --prefix=/usr/local/phyre/nginx

%make_install
mv $RPM_BUILD_ROOT/usr/local/phyre/nginx/sbin/nginx $RPM_BUILD_ROOT/usr/local/phyre/nginx/sbin/phyre-nginx
rm -rf $RPM_BUILD_ROOT/usr/local/phyre/nginx/sbin/nginx.old
wget https://raw.githubusercontent.com/PhyreApps/PhyrePanelNGINX/main/compilators/debian/nginx/nginx.conf -O $RPM_BUILD_ROOT/usr/local/phyre/nginx/conf/nginx.conf

%files
/usr/local/phyre/nginx

%changelog
* Tue May 03 2024 Phyre PHP Packaging <phyre-nginx-packaging@phyrepanel.com> - 1.25.5-1%{?dist}.ngx
- 1.25.5-1
- Initial release of Phyre PHP 1.25.5

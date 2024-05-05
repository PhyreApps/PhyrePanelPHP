Name:           phyre-php
Version:        8.2
Release:        1%{?dist}
Summary:       Phyre PHP - Web server for PhyrePanel

License:       GPL
URL:    https://phyrepanel.com
Source0: http://de2.php.net/distributions/php-8.2.0.tar.gz

%description
Phyre PHP for executing phyre panel

%prep
# we have no source, so nothing here

%build
tar -xzf $RPM_SOURCE_DIR/php-8.2.0.tar.gz -C $RPM_BUILD_DIR
cd php-8.2.0
./buildconf --force
./configure --prefix=/usr/local/phyre/php \
				--with-libdir=lib/$(arch)-linux-gnu \
				--enable-fpm --with-fpm-user=phyreweb --with-fpm-group=phyreweb \
				--with-openssl \
				--with-mysqli \
      				--with-pdo-mysql=mysqlnd \
        			--with-mysqli=mysqlnd \
		    		--with-pdo-sqlite \
		    		--with-pdo-pgsql \
				--with-gettext \
				--with-curl \
				--enable-intl \
				--with-zip \
				--with-zlib \
				--with-gmp \
				--with-sodium \
				--with-freetype \
			  	--enable-sockets \
				--enable-mbstring \
				--with-libdir=lib/$(arch)-linux-gnu
php
%make_install

wget https://raw.githubusercontent.com/PhyreApps/PhyrePanelPHP/main/compilators/debian/php/php-fpm.conf -O $RPM_BUILD_ROOT/usr/local/phyre/php/conf/php-fpm.conf

%files
/usr/local/phyre/php

%changelog
* Tue May 05 2024 Phyre PHP Packaging <phyre-nginx-packaging@phyrepanel.com> - 8.2
- Initial release of Phyre PHP 8.2

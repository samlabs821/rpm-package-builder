%define nginx_module_openresty_headers_more 0.33
%define nginx_version 1.19.2
%define debug_package %{nil}

Name: nginx-module-openresty-headers-more
Version: %{nginx_version}+%{nginx_module_openresty_headers_more}
Release: 2%{?dist}
Summary: nginx openresty headers more shared module
License: BSD
URL: https://github.com/openresty/headers-more-nginx-module
Source0: https://nginx.org/download/nginx-%{nginx_version}.tar.gz
Source1: %{url}/archive/v%{nginx_module_openresty_headers_more}/headers-more-nginx-module-v%{nginx_module_openresty_headers_more}.tar.gz
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: pcre-devel
BuildRequires: zlib-devel
Requires: nginx = 1:%{nginx_version}

%description
Set and clear input and output headers...more than "add"!

%prep
%setup -q -n nginx-%{nginx_version}
%setup -T -D -b 1 -n headers-more-nginx-module-%{nginx_module_openresty_headers_more}

%build
cd %{_builddir}/nginx-%{nginx_version}
./configure --with-compat --add-dynamic-module=../headers-more-nginx-module-%{nginx_module_openresty_headers_more}
%make_build modules

%install
%{__install} -d %{buildroot}%{_libdir}/nginx/modules

%{__install} -m 755 %{_builddir}/nginx-%{nginx_version}/objs/ngx_http_headers_more_filter_module.so \
  %{buildroot}%{_libdir}/nginx/modules/ngx_http_headers_more_filter_module.so

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/nginx/modules/*.so

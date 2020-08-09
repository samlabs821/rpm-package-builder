%define nginx_module_openresty_headers_more 0.33
%define nginx_version 1.18.0
%define debug_package %{nil}

Summary: nginx openresty headers more shared module
Name: nginx-module-openresty-headers-more
Version: %{nginx_version}+%{nginx_module_openresty_headers_more}
Release: 1%{?dist}
URL: https://github.com/openresty/headers-more-nginx-module
License: BSD

Source0: https://nginx.org/download/nginx-%{nginx_version}.tar.gz
Source1: https://github.com/openresty/headers-more-nginx-module/archive/v%{nginx_module_openresty_headers_more}/headers-more-nginx-module-v%{nginx_module_openresty_headers_more}.tar.gz

Requires: nginx = 1:%{nginx_version}
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: pcre-devel
BuildRequires: zlib-devel

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}

%prep
%setup -q -n nginx-%{nginx_version}
%setup -T -D -b 1 -n headers-more-nginx-module-%{nginx_module_openresty_headers_more}

%build
cd %{_builddir}/nginx-%{nginx_version}
./configure --with-compat --add-dynamic-module=../headers-more-nginx-module-%{nginx_module_openresty_headers_more}
make modules

%install
%{__rm} -rf %{buildroot}

%{__install} -Dm755 %{_builddir}/nginx-%{nginx_version}/objs/ngx_http_headers_more_filter_module.so \
    $RPM_BUILD_ROOT%{_libdir}/nginx/modules/ngx_http_headers_more_filter_module.so

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/nginx/modules/*.so

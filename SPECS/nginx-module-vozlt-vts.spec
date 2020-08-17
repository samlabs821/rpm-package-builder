%define nginx_module_vozlt_vts_version 0.1.18
%define nginx_version 1.19.2
%define debug_package %{nil}

Name: nginx-module-vozlt-vts
Version: %{nginx_version}+%{nginx_module_vozlt_vts_version}
Release: 2%{?dist}
Summary: nginx vozlt vts shared module
License: BSD
URL: https://github.com/vozlt/nginx-module-vts
Source0: https://nginx.org/download/nginx-%{nginx_version}.tar.gz
Source1: %{url}/archive/v%{nginx_module_vozlt_vts_version}/nginx-module-vts-v%{nginx_module_vozlt_vts_version}.tar.gz
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: pcre-devel
BuildRequires: zlib-devel
Requires: nginx = 1:%{nginx_version}

%description
Nginx virtual host traffic status module.

%prep
%setup -q -n nginx-%{nginx_version}
%setup -T -D -b 1 -n nginx-module-vts-%{nginx_module_vozlt_vts_version}

%build
cd %{_builddir}/nginx-%{nginx_version}
./configure --with-compat --add-dynamic-module=../nginx-module-vts-%{nginx_module_vozlt_vts_version}
%make_build modules

%install
%{__install} -d %{buildroot}%{_libdir}/nginx/modules

%{__install} -m 755 %{_builddir}/nginx-%{nginx_version}/objs/ngx_http_vhost_traffic_status_module.so \
  %{buildroot}%{_libdir}/nginx/modules/ngx_http_vhost_traffic_status_module.so

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/nginx/modules/*.so

%define nginx_module_vozlt_stream_sts_version 0.1.1
%define nginx_module_vozlt_sts_version 0.1.1
%define nginx_version 1.19.2
%define debug_package %{nil}

Name: nginx-module-vozlt-stream-sts
Version: %{nginx_version}+%{nginx_module_vozlt_stream_sts_version}
Release: 1%{?dist}
Summary: nginx vozlt stream sts shared module
License: BSD
URL: https://github.com/vozlt/nginx-module-stream-sts
Source0: https://nginx.org/download/nginx-%{nginx_version}.tar.gz
Source1: %{url}/archive/v%{nginx_module_vozlt_stream_sts_version}/nginx-module-stream-sts-v%{nginx_module_vozlt_stream_sts_version}.tar.gz
Source2: https://github.com/vozlt/nginx-module-sts/archive/v%{nginx_module_vozlt_sts_version}/nginx-module-sts-v%{nginx_module_vozlt_sts_version}.tar.gz
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: pcre-devel
BuildRequires: zlib-devel
Requires: nginx = 1:%{nginx_version}
Requires: nginx-module-vozlt-sts = 1:%{nginx_module_vozlt_sts_version}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Nginx stream server traffic status core module

%prep
%setup -q -n nginx-%{nginx_version}
%setup -T -D -b 1 -q -n nginx-module-stream-sts-%{nginx_module_vozlt_stream_sts_version}
%setup -T -D -b 2 -q -n nginx-module-sts-%{nginx_module_vozlt_sts_version}

%build
cd %{_builddir}/nginx-%{nginx_version}
./configure --with-compat --with-stream --add-dynamic-module=../nginx-module-stream-sts-%{nginx_module_vozlt_stream_sts_version} --add-dynamic-module=../nginx-module-sts-%{nginx_module_vozlt_sts_version}
%make_build modules

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_libdir}/nginx/modules
%{__install} -m 755 %{_builddir}/nginx-%{nginx_version}/objs/ngx_stream_server_traffic_status_module.so \
  %{buildroot}%{_libdir}/nginx/modules/ngx_stream_server_traffic_status_module.so

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/nginx/modules/*.so

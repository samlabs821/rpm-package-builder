%define nginx_module_vozlt_vts_version 0.1.18
%define nginx_version 1.19.2
%define debug_package %{nil}

Summary: nginx vozlt vts shared module
Name: nginx-module-vozlt-vts
Version: %{nginx_version}+%{nginx_module_vozlt_vts_version}
Release: 1%{?dist}
URL: https://github.com/vozlt/nginx-module-vts
License: BSD

Source0: https://nginx.org/download/nginx-%{nginx_version}.tar.gz
Source1: https://github.com/vozlt/nginx-module-vts/archive/v%{nginx_module_vozlt_vts_version}/nginx-module-vts-v%{nginx_module_vozlt_vts_version}.tar.gz

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
%setup -T -D -b 1 -n nginx-module-vts-%{nginx_module_vozlt_vts_version}

%build
cd %{_builddir}/nginx-%{nginx_version}
./configure --with-compat --add-dynamic-module=../nginx-module-vts-%{nginx_module_vozlt_vts_version}
make modules

%install
%{__rm} -rf %{buildroot}

%{__install} -Dm755 %{_builddir}/nginx-%{nginx_version}/objs/ngx_http_vhost_traffic_status_module.so \
    $RPM_BUILD_ROOT%{_libdir}/nginx/modules/ngx_http_vhost_traffic_status_module.so

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/nginx/modules/*.so

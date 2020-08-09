%define knyar_lua_nginx_prometheus_version 0.20200523
%define lua_version 5.1
%define debug_package %{nil}

Summary: knyar lua nginx prometheus
Name: knyar-lua-nginx-prometheus
Version: %{knyar_lua_nginx_prometheus_version}
Release: 1%{?dist}
License: BSD
URL: https://github.com/knyar/nginx-lua-prometheus

Source: https://github.com/knyar/nginx-lua-prometheus/archive/%{knyar_lua_nginx_prometheus_version}/nginx-lua-prometheus-%{knyar_lua_nginx_prometheus_version}.tar.gz

Requires: nginx, lua = %{lua_version}

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}

%prep
%setup -q -n nginx-lua-prometheus-%{knyar_lua_nginx_prometheus_version}

%install
%{__rm} -rf %{buildroot}
%{__install} -d $RPM_BUILD_ROOT/usr/share/lua/%{lua_version}

%{__install} -Dm755 %{_builddir}/nginx-lua-prometheus-%{knyar_lua_nginx_prometheus_version}/*.lua \
    $RPM_BUILD_ROOT/usr/share/lua/%{lua_version}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/share/lua/%{lua_version}/*.lua

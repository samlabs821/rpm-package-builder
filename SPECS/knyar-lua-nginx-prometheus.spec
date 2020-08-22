%define lua_version 5.1
%define debug_package %{nil}

Name: knyar-lua-nginx-prometheus
Version: 0.20200523
Release: 2%{?dist}
Summary: knyar lua nginx prometheus
License: MIT
URL: https://github.com/knyar/nginx-lua-prometheus
Source: %{url}/archive/%{version}/nginx-lua-prometheus-%{version}.tar.gz
Requires: nginx
Requires: lua = %{lua_version}
BuildArch: noarch

%description
This is a Lua library that can be used with Nginx to keep track of metrics and expose them on a separate web page to be pulled by Prometheus.

%prep
%setup -q -n nginx-lua-prometheus-%{version}

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_datadir}/lua/%{lua_version}
%{__install} -m 755 %{_builddir}/nginx-lua-prometheus-%{version}/*.lua \
  %{buildroot}%{_datadir}/lua/%{lua_version}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/lua/%{lua_version}/*.lua

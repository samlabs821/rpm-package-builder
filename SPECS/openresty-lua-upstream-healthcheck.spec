%define lua_version 5.1
%define debug_package %{nil}

Name: openresty-lua-upstream-healthcheck
Version: 0.06
Release: 2%{?dist}
Summary: openresty lua upstream healthcheck
License: BSD
URL: https://github.com/openresty/lua-resty-upstream-healthcheck
Source: %{url}/archive/v%{version}/lua-resty-upstream-healthcheck-v%{version}.tar.gz
Requires: nginx, lua = %{lua_version}
BuildArch: noarch

%description
Health-checker for Nginx upstream servers.

%prep
%setup -q -n lua-resty-upstream-healthcheck-%{version}

%install
%{__install} -d %{buildroot}%{_datadir}/lua/%{lua_version}/resty
%{__install} -d %{buildroot}%{_datadir}/lua/%{lua_version}/resty/upstream

%{__install} -m 755 %{_builddir}/lua-resty-upstream-healthcheck-%{version}/lib/resty/upstream/*.lua \
  %{buildroot}%{_datadir}/lua/%{lua_version}/resty/upstream

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/lua/%{lua_version}/resty/upstream/*.lua

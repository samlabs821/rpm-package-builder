%define lua_version 5.1
%define debug_package %{nil}

Name: openresty-lua-lrucache
Version: 0.10
Release: 2%{?dist}
Summary: openresty lua lrucache
License: BSD
URL: https://github.com/openresty/lua-resty-lrucache
Source: %{url}/archive/v%{version}/lua-resty-lrucache-v%{version}.tar.gz
Requires: nginx
Requires: lua = %{lua_version}
BuildArch: noarch

%description
This library implements a simple LRU cache for OpenResty and the ngx_lua module.

%prep
%setup -q -n lua-resty-lrucache-%{version}

%install
%{__install} -d %{buildroot}%{_datadir}/lua/%{lua_version}/resty/
%{__install} -d %{buildroot}%{_datadir}/lua/%{lua_version}/resty/lrucache

%{__install} -m 755 %{_builddir}/lua-resty-lrucache-%{version}/lib/resty/*.lua \
    %{buildroot}%{_datadir}/lua/%{lua_version}/resty
%{__install} -m 755 %{_builddir}/lua-resty-lrucache-%{version}/lib/resty/lrucache/*.lua \
    %{buildroot}%{_datadir}/lua/%{lua_version}/resty/lrucache

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/lua/%{lua_version}/resty/*.lua
%{_datadir}/lua/%{lua_version}/resty/lrucache/*.lua
